"""
Local Ontology Parsers for OncoCITE Tier 2 Normalization
Parses OBO/OWL files and builds searchable local databases
"""

import re
import sqlite3
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass, field
from collections import defaultdict
import gzip


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class OBOTerm:
    """Represents a single term from an OBO ontology"""
    id: str
    name: str
    definition: str = ""
    synonyms: List[str] = field(default_factory=list)
    xrefs: List[str] = field(default_factory=list)
    is_a: List[str] = field(default_factory=list)
    namespace: str = ""
    is_obsolete: bool = False
    alt_ids: List[str] = field(default_factory=list)

    def __repr__(self):
        return f"OBOTerm(id='{self.id}', name='{self.name}')"


# ============================================================================
# OBO PARSER
# ============================================================================

class OBOParser:
    """
    Fast parser for OBO (Open Biomedical Ontologies) format files
    Handles: DOID, SO, GO, HPO, MONDO
    """

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.terms: Dict[str, OBOTerm] = {}
        self.name_to_id: Dict[str, str] = {}
        self.synonym_to_id: Dict[str, List[str]] = defaultdict(list)

    def parse(self) -> Dict[str, OBOTerm]:
        """Parse OBO file and return dictionary of terms"""

        print(f"📖 Parsing {self.filepath.name}...")

        current_term = None
        in_term = False

        with open(self.filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()

                # Start of new term
                if line == "[Term]":
                    if current_term and current_term.id:
                        self._add_term(current_term)
                    current_term = OBOTerm(id="", name="")
                    in_term = True
                    continue

                # End of term section
                elif line.startswith("[") and line != "[Term]":
                    if current_term and current_term.id:
                        self._add_term(current_term)
                    current_term = None
                    in_term = False
                    continue

                # Skip if not in term
                if not in_term or not current_term:
                    continue

                # Parse term fields
                if ":" not in line:
                    continue

                key, value = line.split(":", 1)
                value = value.strip()

                if key == "id":
                    current_term.id = value

                elif key == "name":
                    current_term.name = value

                elif key == "def":
                    # Extract definition (remove quotes and metadata)
                    match = re.match(r'"([^"]+)"', value)
                    if match:
                        current_term.definition = match.group(1)

                elif key == "synonym":
                    # Extract synonym text
                    match = re.match(r'"([^"]+)"', value)
                    if match:
                        current_term.synonyms.append(match.group(1))

                elif key == "xref":
                    current_term.xrefs.append(value)

                elif key == "is_a":
                    # Extract parent ID
                    parent_id = value.split("!")[0].strip()
                    current_term.is_a.append(parent_id)

                elif key == "namespace":
                    current_term.namespace = value

                elif key == "is_obsolete":
                    current_term.is_obsolete = (value.lower() == "true")

                elif key == "alt_id":
                    current_term.alt_ids.append(value)

        # Add last term
        if current_term and current_term.id:
            self._add_term(current_term)

        print(f"  ✅ Parsed {len(self.terms)} terms")
        return self.terms

    def _add_term(self, term: OBOTerm):
        """Add term to indices"""
        if term.is_obsolete:
            return

        self.terms[term.id] = term

        # Index by name (lowercased for matching)
        name_lower = term.name.lower()
        self.name_to_id[name_lower] = term.id

        # Index synonyms
        for synonym in term.synonyms:
            syn_lower = synonym.lower()
            self.synonym_to_id[syn_lower].append(term.id)

        # Index alt IDs
        for alt_id in term.alt_ids:
            self.terms[alt_id] = term  # Point alt ID to same term

    def get_term_by_id(self, term_id: str) -> Optional[OBOTerm]:
        """Get term by ID"""
        return self.terms.get(term_id)

    def get_term_by_name(self, name: str) -> Optional[OBOTerm]:
        """Get term by exact name match"""
        name_lower = name.lower()
        term_id = self.name_to_id.get(name_lower)
        if term_id:
            return self.terms[term_id]
        return None

    def search_by_synonym(self, synonym: str) -> List[OBOTerm]:
        """Search for terms by synonym"""
        syn_lower = synonym.lower()
        term_ids = self.synonym_to_id.get(syn_lower, [])
        return [self.terms[tid] for tid in term_ids]

    def fuzzy_search(self, query: str, limit: int = 10) -> List[Tuple[OBOTerm, float]]:
        """Fuzzy search for terms (returns term and similarity score)"""
        query_lower = query.lower()
        results = []

        for term in self.terms.values():
            if term.is_obsolete:
                continue

            # Exact match
            if term.name.lower() == query_lower:
                results.append((term, 1.0))
                continue

            # Contains match
            if query_lower in term.name.lower():
                score = len(query) / len(term.name)
                results.append((term, score * 0.9))
                continue

            # Synonym match
            for syn in term.synonyms:
                if query_lower in syn.lower():
                    score = len(query) / len(syn)
                    results.append((term, score * 0.8))
                    break

        # Sort by score and limit
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:limit]


# ============================================================================
# CLINVAR PARSER
# ============================================================================

class ClinVarParser:
    """
    Parser for ClinVar variant_summary.txt file
    TSV format with variant annotations
    """

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.variants: Dict[str, Dict] = {}

    def parse(self, limit: Optional[int] = None) -> Dict[str, Dict]:
        """Parse ClinVar file (optionally limit number of rows)"""

        print(f"📖 Parsing ClinVar ({self.filepath.name})...")

        count = 0
        with open(self.filepath, 'r', encoding='utf-8') as f:
            # Read header
            header = f.readline().strip().split('\t')

            for line_num, line in enumerate(f, 2):
                if limit and count >= limit:
                    break

                fields = line.strip().split('\t')
                if len(fields) < len(header):
                    continue

                row = dict(zip(header, fields))

                # Key fields
                variant_id = row.get('VariationID', '')
                if not variant_id:
                    continue

                # Store relevant fields
                self.variants[variant_id] = {
                    'variation_id': variant_id,
                    'name': row.get('Name', ''),
                    'gene_symbol': row.get('GeneSymbol', ''),
                    'clinical_significance': row.get('ClinicalSignificance', ''),
                    'rs_id': row.get('RS# (dbSNP)', ''),
                    'nsv_id': row.get('nsv/esv (dbVar)', ''),
                    'rcv_accession': row.get('RCVaccession', ''),
                    'chromosome': row.get('Chromosome', ''),
                    'position_vcf': row.get('PositionVCF', ''),
                    'reference_allele': row.get('ReferenceAlleleVCF', ''),
                    'alternate_allele': row.get('AlternateAlleleVCF', ''),
                    'type': row.get('Type', ''),
                    'assembly': row.get('Assembly', ''),
                }

                count += 1

                if count % 100000 == 0:
                    print(f"  ... processed {count:,} variants")

        print(f"  ✅ Parsed {len(self.variants):,} variants")
        return self.variants

    def get_by_variation_id(self, var_id: str) -> Optional[Dict]:
        """Get variant by ClinVar Variation ID"""
        return self.variants.get(var_id)

    def search_by_gene(self, gene_symbol: str) -> List[Dict]:
        """Search variants by gene symbol"""
        gene_upper = gene_symbol.upper()
        return [v for v in self.variants.values()
                if v['gene_symbol'].upper() == gene_upper]


# ============================================================================
# SQLITE DATABASE BUILDER
# ============================================================================

class OntologyDatabaseBuilder:
    """
    Builds SQLite databases from parsed ontologies for fast querying
    """

    def __init__(self, db_path: str = "data/databases/ontologies.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def create_schema(self):
        """Create database schema"""
        cursor = self.conn.cursor()

        # Main terms table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS terms (
                term_id TEXT PRIMARY KEY,
                ontology TEXT NOT NULL,
                name TEXT NOT NULL,
                definition TEXT,
                namespace TEXT,
                is_obsolete INTEGER DEFAULT 0
            )
        """)

        # Synonyms table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS synonyms (
                term_id TEXT NOT NULL,
                synonym TEXT NOT NULL,
                FOREIGN KEY (term_id) REFERENCES terms(term_id)
            )
        """)

        # Cross-references table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS xrefs (
                term_id TEXT NOT NULL,
                xref TEXT NOT NULL,
                FOREIGN KEY (term_id) REFERENCES terms(term_id)
            )
        """)

        # Hierarchical relationships
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS relationships (
                child_id TEXT NOT NULL,
                parent_id TEXT NOT NULL,
                relationship_type TEXT DEFAULT 'is_a',
                FOREIGN KEY (child_id) REFERENCES terms(term_id),
                FOREIGN KEY (parent_id) REFERENCES terms(term_id)
            )
        """)

        # Variants table (ClinVar)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS variants (
                variation_id TEXT PRIMARY KEY,
                name TEXT,
                gene_symbol TEXT,
                clinical_significance TEXT,
                rs_id TEXT,
                rcv_accession TEXT,
                chromosome TEXT,
                position TEXT,
                ref_allele TEXT,
                alt_allele TEXT,
                type TEXT,
                assembly TEXT
            )
        """)

        # Create indices
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_term_name ON terms(name COLLATE NOCASE)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_term_ontology ON terms(ontology)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_synonym ON synonyms(synonym COLLATE NOCASE)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_variant_gene ON variants(gene_symbol)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_variant_rs ON variants(rs_id)")

        self.conn.commit()
        print("✅ Database schema created")

    def insert_ontology(self, ontology_name: str, terms: Dict[str, OBOTerm]):
        """Insert ontology terms into database"""
        cursor = self.conn.cursor()

        print(f"💾 Inserting {ontology_name} ({len(terms)} terms)...")

        for term_id, term in terms.items():
            # Insert main term
            cursor.execute("""
                INSERT OR REPLACE INTO terms
                (term_id, ontology, name, definition, namespace, is_obsolete)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (term.id, ontology_name, term.name, term.definition,
                  term.namespace, int(term.is_obsolete)))

            # Insert synonyms
            for synonym in term.synonyms:
                cursor.execute("""
                    INSERT INTO synonyms (term_id, synonym)
                    VALUES (?, ?)
                """, (term.id, synonym))

            # Insert xrefs
            for xref in term.xrefs:
                cursor.execute("""
                    INSERT INTO xrefs (term_id, xref)
                    VALUES (?, ?)
                """, (term.id, xref))

            # Insert hierarchical relationships
            for parent_id in term.is_a:
                cursor.execute("""
                    INSERT INTO relationships (child_id, parent_id, relationship_type)
                    VALUES (?, ?, 'is_a')
                """, (term.id, parent_id))

        self.conn.commit()
        print(f"  ✅ Inserted {len(terms)} terms")

    def insert_clinvar(self, variants: Dict[str, Dict]):
        """Insert ClinVar variants into database"""
        cursor = self.conn.cursor()

        print(f"💾 Inserting ClinVar ({len(variants):,} variants)...")

        batch_size = 10000
        batch = []

        for var_id, var in variants.items():
            batch.append((
                var['variation_id'],
                var['name'],
                var['gene_symbol'],
                var['clinical_significance'],
                var['rs_id'],
                var['rcv_accession'],
                var['chromosome'],
                var['position_vcf'],
                var['reference_allele'],
                var['alternate_allele'],
                var['type'],
                var['assembly']
            ))

            if len(batch) >= batch_size:
                cursor.executemany("""
                    INSERT OR REPLACE INTO variants
                    (variation_id, name, gene_symbol, clinical_significance,
                     rs_id, rcv_accession, chromosome, position, ref_allele,
                     alt_allele, type, assembly)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, batch)
                self.conn.commit()
                print(f"  ... inserted {len(batch):,} variants")
                batch = []

        # Insert remaining
        if batch:
            cursor.executemany("""
                INSERT OR REPLACE INTO variants
                (variation_id, name, gene_symbol, clinical_significance,
                 rs_id, rcv_accession, chromosome, position, ref_allele,
                 alt_allele, type, assembly)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, batch)
            self.conn.commit()

        print(f"  ✅ Inserted {len(variants):,} variants")


# ============================================================================
# MAIN BUILD FUNCTION
# ============================================================================

def build_local_databases():
    """Main function to build all local databases"""

    print("="*80)
    print("ONCOCITE - Building Local Ontology Databases")
    print("="*80)
    print()

    ontology_dir = Path("data/ontologies")

    # Initialize database builder
    db_builder = OntologyDatabaseBuilder()
    db_builder.connect()
    db_builder.create_schema()

    # Parse and insert each ontology
    ontologies = [
        ("DOID", "doid.obo"),
        ("SO", "so.obo"),
        ("GO", "go.obo"),
        ("HPO", "hp.obo"),
        ("MONDO", "mondo.obo"),
    ]

    for ont_name, filename in ontologies:
        filepath = ontology_dir / filename
        if filepath.exists():
            parser = OBOParser(str(filepath))
            terms = parser.parse()
            db_builder.insert_ontology(ont_name, terms)
        else:
            print(f"⚠️  {filename} not found, skipping")

    # Parse and insert ClinVar (limit to 500k for speed)
    clinvar_path = ontology_dir / "clinvar_summary.txt"
    if clinvar_path.exists():
        clinvar_parser = ClinVarParser(str(clinvar_path))
        variants = clinvar_parser.parse(limit=500000)  # Limit for faster processing
        db_builder.insert_clinvar(variants)
    else:
        print("⚠️  clinvar_summary.txt not found, skipping")

    db_builder.close()

    print()
    print("="*80)
    print("✅ LOCAL DATABASE BUILD COMPLETE")
    print("="*80)
    print(f"Database location: {db_builder.db_path}")
    print()


if __name__ == "__main__":
    build_local_databases()
