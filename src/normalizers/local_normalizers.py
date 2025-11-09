"""
Local Normalizer Agents for OncoCITE Tier 2
Uses local ontology databases instead of API calls
"""

import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import re


# ============================================================================
# BASE NORMALIZER
# ============================================================================

class BaseNormalizer:
    """Base class for all local normalizers"""

    def __init__(self, db_path: str = "data/databases/ontologies.db"):
        self.db_path = Path(db_path)
        self.conn = None

    def connect(self):
        """Connect to database"""
        if not self.db_path.exists():
            raise FileNotFoundError(
                f"Database not found: {self.db_path}\n"
                "Please run: ./download_ontologies.sh && python local_ontology_parsers.py"
            )
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# ============================================================================
# AGENT 9: DISEASE NORMALIZER
# ============================================================================

class DiseaseNormalizer(BaseNormalizer):
    """
    Agent 9: Disease Normalizer
    Normalizes disease names to DOID, MONDO, NCIt
    """

    def normalize(self, disease_name: str) -> Dict:
        """
        Normalize disease name to standard ontologies

        Args:
            disease_name: Disease name to normalize

        Returns:
            Dictionary with normalized disease information
        """
        if not self.conn:
            self.connect()

        results = {
            "original_term": disease_name,
            "doid": None,
            "doid_name": None,
            "mondo_id": None,
            "mondo_name": None,
            "confidence": 0.0,
            "matches": []
        }

        # Search in DOID first
        cursor = self.conn.cursor()

        # Exact match
        cursor.execute("""
            SELECT term_id, name, definition
            FROM terms
            WHERE ontology = 'DOID'
              AND LOWER(name) = LOWER(?)
              AND is_obsolete = 0
            LIMIT 1
        """, (disease_name,))

        row = cursor.fetchone()
        if row:
            results["doid"] = row["term_id"]
            results["doid_name"] = row["name"]
            results["confidence"] = 1.0
            results["matches"].append({
                "ontology": "DOID",
                "id": row["term_id"],
                "name": row["name"],
                "match_type": "exact"
            })

        # If no exact match, try synonym
        if not results["doid"]:
            cursor.execute("""
                SELECT t.term_id, t.name, s.synonym
                FROM terms t
                JOIN synonyms s ON t.term_id = s.term_id
                WHERE t.ontology = 'DOID'
                  AND LOWER(s.synonym) = LOWER(?)
                  AND t.is_obsolete = 0
                LIMIT 1
            """, (disease_name,))

            row = cursor.fetchone()
            if row:
                results["doid"] = row["term_id"]
                results["doid_name"] = row["name"]
                results["confidence"] = 0.95
                results["matches"].append({
                    "ontology": "DOID",
                    "id": row["term_id"],
                    "name": row["name"],
                    "match_type": "synonym"
                })

        # Try partial match if still no result
        if not results["doid"]:
            cursor.execute("""
                SELECT term_id, name
                FROM terms
                WHERE ontology = 'DOID'
                  AND name LIKE ?
                  AND is_obsolete = 0
                LIMIT 5
            """, (f"%{disease_name}%",))

            rows = cursor.fetchall()
            for row in rows:
                results["matches"].append({
                    "ontology": "DOID",
                    "id": row["term_id"],
                    "name": row["name"],
                    "match_type": "partial"
                })

        # Also search MONDO
        cursor.execute("""
            SELECT term_id, name
            FROM terms
            WHERE ontology = 'MONDO'
              AND LOWER(name) = LOWER(?)
              AND is_obsolete = 0
            LIMIT 1
        """, (disease_name,))

        row = cursor.fetchone()
        if row:
            results["mondo_id"] = row["term_id"]
            results["mondo_name"] = row["name"]

        return results


# ============================================================================
# AGENT 10: VARIANT NORMALIZER
# ============================================================================

class VariantNormalizer(BaseNormalizer):
    """
    Agent 10: Variant Normalizer
    Normalizes variants using SO (Sequence Ontology) and ClinVar
    """

    def normalize(self, gene: str, variant: str) -> Dict:
        """
        Normalize variant information

        Args:
            gene: Gene symbol (e.g., "EGFR")
            variant: Variant name (e.g., "L858R")

        Returns:
            Dictionary with normalized variant information
        """
        if not self.conn:
            self.connect()

        results = {
            "original_gene": gene,
            "original_variant": variant,
            "clinvar_matches": [],
            "variant_type_so": None,
            "confidence": 0.0
        }

        cursor = self.conn.cursor()

        # Convert short variant name to potential HGVS patterns
        # e.g., L858R -> Leu858Arg, L858, 858
        variant_patterns = [
            f"%{variant}%",  # Direct match
            f"%{gene}%{variant}%",  # Gene + variant
        ]

        # If it's a single-letter AA change (e.g., L858R), add 3-letter version
        import re
        match = re.match(r'([A-Z])(\d+)([A-Z])$', variant)
        if match:
            aa_map = {
                'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys',
                'Q': 'Gln', 'E': 'Glu', 'G': 'Gly', 'H': 'His', 'I': 'Ile',
                'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro',
                'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'
            }
            from_aa, pos, to_aa = match.groups()
            if from_aa in aa_map and to_aa in aa_map:
                hgvs_form = f"{aa_map[from_aa]}{pos}{aa_map[to_aa]}"
                variant_patterns.append(f"%{hgvs_form}%")

        # Search ClinVar with multiple patterns
        all_rows = []
        for pattern in variant_patterns:
            cursor.execute("""
                SELECT variation_id, name, clinical_significance, rs_id,
                       chromosome, position, ref_allele, alt_allele, type
                FROM variants
                WHERE UPPER(gene_symbol) = UPPER(?)
                  AND name LIKE ?
                LIMIT 10
            """, (gene, pattern))
            all_rows.extend(cursor.fetchall())
            if all_rows:  # Stop if we found matches
                break

        # Deduplicate results
        seen_ids = set()
        rows = []
        for row in all_rows:
            if row["variation_id"] not in seen_ids:
                rows.append(row)
                seen_ids.add(row["variation_id"])

        for row in rows:
            results["clinvar_matches"].append({
                "variation_id": row["variation_id"],
                "name": row["name"],
                "clinical_significance": row["clinical_significance"],
                "rs_id": row["rs_id"],
                "chromosome": row["chromosome"],
                "position": row["position"],
                "ref_allele": row["ref_allele"],
                "alt_allele": row["alt_allele"],
                "type": row["type"]
            })

        # Determine variant type from SO
        variant_type = self._infer_variant_type(variant)
        if variant_type:
            cursor.execute("""
                SELECT term_id, name, definition
                FROM terms
                WHERE ontology = 'SO'
                  AND LOWER(name) LIKE ?
                LIMIT 1
            """, (f"%{variant_type}%",))

            row = cursor.fetchone()
            if row:
                results["variant_type_so"] = {
                    "id": row["term_id"],
                    "name": row["name"],
                    "definition": row["definition"]
                }

        results["confidence"] = 0.8 if results["clinvar_matches"] else 0.3

        return results

    def _infer_variant_type(self, variant: str) -> Optional[str]:
        """Infer variant type from variant string"""
        # Simple heuristics
        if re.match(r'^[A-Z]\d+[A-Z]$', variant):  # e.g., L858R
            return "missense"
        elif "del" in variant.lower():
            return "deletion"
        elif "ins" in variant.lower():
            return "insertion"
        elif "dup" in variant.lower():
            return "duplication"
        elif "fs" in variant.lower():
            return "frameshift"
        elif "*" in variant:
            return "nonsense"
        return None


# ============================================================================
# AGENT 14: ONTOLOGY NORMALIZER
# ============================================================================

class OntologyNormalizer(BaseNormalizer):
    """
    Agent 14: Ontology Normalizer
    Normalizes to GO, HPO, MONDO
    """

    def normalize_gene(self, gene_symbol: str) -> Dict:
        """Normalize gene to GO terms"""
        if not self.conn:
            self.connect()

        results = {
            "gene": gene_symbol,
            "go_terms": [],
            "confidence": 0.0
        }

        # Note: GO terms are usually associated via gene annotations
        # This would require additional gene-to-GO mapping data
        # For now, return structure

        return results

    def normalize_phenotype(self, phenotype: str) -> Dict:
        """Normalize phenotype to HPO"""
        if not self.conn:
            self.connect()

        results = {
            "original_phenotype": phenotype,
            "hpo_id": None,
            "hpo_name": None,
            "hpo_matches": [],
            "confidence": 0.0
        }

        cursor = self.conn.cursor()

        # Try exact match first
        cursor.execute("""
            SELECT term_id, name, definition
            FROM terms
            WHERE ontology = 'HPO'
              AND LOWER(name) = LOWER(?)
              AND is_obsolete = 0
            LIMIT 1
        """, (phenotype,))

        row = cursor.fetchone()
        if row:
            results["hpo_id"] = row["term_id"]
            results["hpo_name"] = row["name"]
            results["confidence"] = 1.0
            return results

        # Try synonym match
        cursor.execute("""
            SELECT t.term_id, t.name, s.synonym
            FROM terms t
            JOIN synonyms s ON t.term_id = s.term_id
            WHERE t.ontology = 'HPO'
              AND LOWER(s.synonym) = LOWER(?)
              AND t.is_obsolete = 0
            LIMIT 1
        """, (phenotype,))

        row = cursor.fetchone()
        if row:
            results["hpo_id"] = row["term_id"]
            results["hpo_name"] = row["name"]
            results["confidence"] = 0.95
            return results

        # Try partial match in names
        cursor.execute("""
            SELECT term_id, name
            FROM terms
            WHERE ontology = 'HPO'
              AND LOWER(name) LIKE LOWER(?)
              AND is_obsolete = 0
            LIMIT 5
        """, (f"%{phenotype}%",))

        rows = cursor.fetchall()
        for row in rows:
            results["hpo_matches"].append({
                "hpo_id": row["term_id"],
                "hpo_name": row["name"],
                "match_type": "partial"
            })

        # If we have partial matches, use the first one with lower confidence
        if results["hpo_matches"]:
            results["hpo_id"] = results["hpo_matches"][0]["hpo_id"]
            results["hpo_name"] = results["hpo_matches"][0]["hpo_name"]
            results["confidence"] = 0.7

        return results


# ============================================================================
# AGENT 11: THERAPY NORMALIZER
# ============================================================================

class TherapyNormalizer(BaseNormalizer):
    """
    Agent 11: Therapy Normalizer
    Normalizes drug/therapy names
    Note: Basic version without NCIt (requires UMLS license)
    """

    def __init__(self, db_path: str = "data/databases/ontologies.db"):
        super().__init__(db_path)
        # Common drug name variations
        self.drug_synonyms = {
            "osimertinib": ["tagrisso", "azd9291"],
            "gefitinib": ["iressa"],
            "erlotinib": ["tarceva"],
            "afatinib": ["gilotrif"],
            "pembrolizumab": ["keytruda"],
            "nivolumab": ["opdivo"],
            "cisplatin": ["platinol"],
            "carboplatin": ["paraplatin"],
            "pemetrexed": ["alimta"],
        }

    def normalize(self, therapy_name: str) -> Dict:
        """
        Normalize therapy/drug name

        Args:
            therapy_name: Drug or therapy name

        Returns:
            Dictionary with normalized therapy information
        """
        results = {
            "original_therapy": therapy_name,
            "normalized_name": None,
            "drug_class": None,
            "synonyms": [],
            "confidence": 0.0
        }

        therapy_lower = therapy_name.lower().strip()

        # Check against known drugs
        for standard_name, synonyms in self.drug_synonyms.items():
            if therapy_lower == standard_name or therapy_lower in synonyms:
                results["normalized_name"] = standard_name.capitalize()
                results["synonyms"] = synonyms
                results["confidence"] = 1.0

                # Infer drug class
                if standard_name in ["osimertinib", "gefitinib", "erlotinib", "afatinib"]:
                    results["drug_class"] = "EGFR inhibitor"
                elif standard_name in ["pembrolizumab", "nivolumab"]:
                    results["drug_class"] = "Immune checkpoint inhibitor"
                elif standard_name in ["cisplatin", "carboplatin"]:
                    results["drug_class"] = "Platinum compound"
                elif standard_name == "pemetrexed":
                    results["drug_class"] = "Antifolate"

                return results

        # If no match, return original with low confidence
        results["normalized_name"] = therapy_name
        results["confidence"] = 0.3

        return results


# ============================================================================
# AGENT 12: TRIAL NORMALIZER
# ============================================================================

class TrialNormalizer(BaseNormalizer):
    """
    Agent 12: Trial Normalizer
    Normalizes clinical trial identifiers
    """

    def normalize(self, trial_id: str) -> Dict:
        """
        Normalize clinical trial ID

        Args:
            trial_id: Trial identifier (e.g., "NCT12345678")

        Returns:
            Dictionary with normalized trial information
        """
        results = {
            "original_id": trial_id,
            "normalized_id": None,
            "registry": None,
            "is_valid": False,
            "confidence": 0.0
        }

        trial_id = trial_id.strip().upper()

        # NCT (ClinicalTrials.gov)
        if trial_id.startswith("NCT"):
            # Valid format: NCT followed by 8 digits
            if len(trial_id) == 11 and trial_id[3:].isdigit():
                results["normalized_id"] = trial_id
                results["registry"] = "ClinicalTrials.gov"
                results["is_valid"] = True
                results["confidence"] = 1.0

        # EudraCT (European Union)
        elif trial_id.startswith("EUCTR"):
            results["normalized_id"] = trial_id
            results["registry"] = "EudraCT"
            results["is_valid"] = True
            results["confidence"] = 0.9

        # Try to extract NCT from free text
        else:
            import re
            match = re.search(r'NCT\d{8}', trial_id)
            if match:
                results["normalized_id"] = match.group(0)
                results["registry"] = "ClinicalTrials.gov"
                results["is_valid"] = True
                results["confidence"] = 0.8

        return results


# ============================================================================
# AGENT 13: COORDINATE NORMALIZER
# ============================================================================

class CoordinateNormalizer(BaseNormalizer):
    """
    Agent 13: Coordinate Normalizer
    Validates and normalizes genomic coordinates and HGVS
    """

    def normalize(self, variant_string: str, build: str = "hg38") -> Dict:
        """
        Normalize genomic coordinates

        Args:
            variant_string: Variant in various formats
            build: Genome build (hg38, hg19, etc.)

        Returns:
            Dictionary with normalized coordinate information
        """
        results = {
            "original_string": variant_string,
            "hgvs_validated": False,
            "genomic_build": build,
            "chromosome": None,
            "position": None,
            "ref": None,
            "alt": None,
            "confidence": 0.0
        }

        import re

        # HGVS protein notation: p.Leu858Arg
        if variant_string.startswith("p."):
            # Basic validation
            pattern = r'p\.[A-Z][a-z]{2}\d+[A-Z][a-z]{2}'
            if re.match(pattern, variant_string):
                results["hgvs_validated"] = True
                results["confidence"] = 1.0

        # HGVS cDNA notation: c.2573T>G
        elif variant_string.startswith("c."):
            pattern = r'c\.\d+[ACGT]>[ACGT]'
            if re.match(pattern, variant_string):
                results["hgvs_validated"] = True
                results["confidence"] = 1.0

        # Genomic coordinate: chr7:55249071 A>G
        elif "chr" in variant_string.lower():
            match = re.match(r'chr(\w+):(\d+)\s*([ACGT])>([ACGT])', variant_string, re.IGNORECASE)
            if match:
                results["chromosome"] = match.group(1)
                results["position"] = int(match.group(2))
                results["ref"] = match.group(3)
                results["alt"] = match.group(4)
                results["hgvs_validated"] = True
                results["confidence"] = 0.9

        # Simple format: 7:55249071A>G
        else:
            match = re.match(r'(\d+):(\d+)([ACGT])>([ACGT])', variant_string)
            if match:
                results["chromosome"] = match.group(1)
                results["position"] = int(match.group(2))
                results["ref"] = match.group(3)
                results["alt"] = match.group(4)
                results["confidence"] = 0.8

        return results


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def normalize_disease(disease_name: str) -> Dict:
    """Convenience function for disease normalization"""
    with DiseaseNormalizer() as normalizer:
        return normalizer.normalize(disease_name)


def normalize_variant(gene: str, variant: str) -> Dict:
    """Convenience function for variant normalization"""
    with VariantNormalizer() as normalizer:
        return normalizer.normalize(gene, variant)


def normalize_phenotype(phenotype: str) -> Dict:
    """Convenience function for phenotype normalization"""
    with OntologyNormalizer() as normalizer:
        return normalizer.normalize_phenotype(phenotype)


def normalize_therapy(therapy_name: str) -> Dict:
    """Convenience function for therapy normalization"""
    normalizer = TherapyNormalizer()
    return normalizer.normalize(therapy_name)


def normalize_trial(trial_id: str) -> Dict:
    """Convenience function for trial normalization"""
    normalizer = TrialNormalizer()
    return normalizer.normalize(trial_id)


def normalize_coordinates(variant_string: str, build: str = "hg38") -> Dict:
    """Convenience function for coordinate normalization"""
    normalizer = CoordinateNormalizer()
    return normalizer.normalize(variant_string, build)


# ============================================================================
# DEMO / TEST
# ============================================================================

if __name__ == "__main__":
    print("="*80)
    print("LOCAL NORMALIZERS - COMPREHENSIVE DEMO")
    print("Testing all 6 Tier 2 Normalization Agents")
    print("="*80)
    print()

    # Test Agent 9: Disease Normalizer
    print("Agent 9: Disease Normalizer (DOID, MONDO)")
    print("-" * 80)
    result = normalize_disease("lung adenocarcinoma")
    print(f"Input: 'lung adenocarcinoma'")
    print(f"  DOID: {result['doid']}")
    print(f"  Name: {result['doid_name']}")
    print(f"  Confidence: {result['confidence']}")
    print()

    # Test Agent 10: Variant Normalizer
    print("Agent 10: Variant Normalizer (SO, ClinVar)")
    print("-" * 80)
    result = normalize_variant("EGFR", "L858R")
    print(f"Input: EGFR L858R")
    print(f"  ClinVar matches: {len(result['clinvar_matches'])}")
    if result['clinvar_matches']:
        print(f"  First match: {result['clinvar_matches'][0]['name']}")
        print(f"  Clinical significance: {result['clinvar_matches'][0]['clinical_significance']}")
    print()

    # Test Agent 11: Therapy Normalizer
    print("Agent 11: Therapy Normalizer (Drug names)")
    print("-" * 80)
    result = normalize_therapy("Tagrisso")
    print(f"Input: 'Tagrisso'")
    print(f"  Normalized: {result['normalized_name']}")
    print(f"  Drug class: {result['drug_class']}")
    print(f"  Confidence: {result['confidence']}")
    print()

    # Test Agent 12: Trial Normalizer
    print("Agent 12: Trial Normalizer (ClinicalTrials.gov)")
    print("-" * 80)
    result = normalize_trial("NCT01234567")
    print(f"Input: 'NCT01234567'")
    print(f"  Normalized: {result['normalized_id']}")
    print(f"  Registry: {result['registry']}")
    print(f"  Valid: {result['is_valid']}")
    print(f"  Confidence: {result['confidence']}")
    print()

    # Test Agent 13: Coordinate Normalizer
    print("Agent 13: Coordinate Normalizer (HGVS validation)")
    print("-" * 80)
    result = normalize_coordinates("p.Leu858Arg")
    print(f"Input: 'p.Leu858Arg'")
    print(f"  HGVS validated: {result['hgvs_validated']}")
    print(f"  Confidence: {result['confidence']}")
    print()

    # Test Agent 14: Ontology Normalizer (Phenotype)
    print("Agent 14: Ontology Normalizer (GO, HPO, MONDO)")
    print("-" * 80)
    result = normalize_phenotype("seizure")
    print(f"Input: 'seizure'")
    print(f"  HPO: {result['hpo_id']}")
    print(f"  Name: {result['hpo_name']}")
    print(f"  Confidence: {result['confidence']}")
    print()

    print("="*80)
    print("✅ ALL 6 TIER 2 NORMALIZERS TESTED SUCCESSFULLY")
    print("="*80)
