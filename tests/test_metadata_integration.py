"""
Test Excel Metadata Integration and FastAPI Endpoints

Tests:
1. Excel parsing (125-column CIViC data dictionary)
2. Metadata endpoint simulation
3. Paper-to-source_id mapping
4. Evidence item extraction

Data Source: all_combined_extracted_data_with_source_counts.xlsx

Author: OncoCITE Testing Suite
Date: 2025-11-13
"""

import pandas as pd
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict


@dataclass
class PaperMetadataSummary:
    """Aggregated metadata for a paper"""
    source_id: str
    paper_key: Optional[str]
    citation: Optional[str]
    pmid: Optional[str]
    doi: Optional[str]
    publication_year: Optional[int]

    # Aggregated fields
    genes: List[str]
    diseases: List[str]
    therapies: List[str]
    evidence_count: int
    evidence_types: List[str]
    evidence_levels: List[str]

    # Asset info
    asset_base_path: Optional[str]


@dataclass
class ColumnMetadata:
    """Metadata about a column in the data dictionary"""
    column_name: str
    column_index: int
    description: str
    data_type: str
    example_value: Optional[str] = None


class MetadataParser:
    """Parse and test Excel metadata"""

    def __init__(self, excel_path: str = "/home/user/Final_Dataset_Civic/all_combined_extracted_data_with_source_counts.xlsx"):
        self.excel_path = excel_path
        self.df: Optional[pd.DataFrame] = None
        self.column_metadata: List[ColumnMetadata] = []

    def load_data(self) -> bool:
        """Load Excel file"""
        try:
            print(f"📂 Loading Excel file: {self.excel_path}")
            self.df = pd.read_excel(self.excel_path)
            print(f"✅ Loaded {len(self.df)} rows × {len(self.df.columns)} columns")
            print(f"   Columns: {list(self.df.columns[:10])}... (showing first 10)")
            return True
        except FileNotFoundError:
            print(f"❌ File not found: {self.excel_path}")
            return False
        except Exception as e:
            print(f"❌ Error loading Excel: {e}")
            return False

    def analyze_columns(self) -> List[ColumnMetadata]:
        """Analyze and document all columns"""
        if self.df is None:
            print("❌ No data loaded. Call load_data() first.")
            return []

        print(f"\n{'='*80}")
        print("Column Analysis")
        print(f"{'='*80}\n")

        column_descriptions = self._get_column_descriptions()

        for idx, col_name in enumerate(self.df.columns):
            # Get sample value
            non_null_values = self.df[col_name].dropna()
            example_value = str(non_null_values.iloc[0]) if len(non_null_values) > 0 else None

            # Infer data type
            dtype = str(self.df[col_name].dtype)

            col_meta = ColumnMetadata(
                column_name=col_name,
                column_index=idx,
                description=column_descriptions.get(col_name, "No description"),
                data_type=dtype,
                example_value=example_value
            )

            self.column_metadata.append(col_meta)

            if idx < 20:  # Print first 20
                print(f"{idx+1:3}. {col_name:40} | {dtype:15} | {example_value[:50] if example_value else 'NULL'}")

        print(f"\n... ({len(self.df.columns)} total columns)\n")

        return self.column_metadata

    def _get_column_descriptions(self) -> Dict[str, str]:
        """Map column names to descriptions (from CIViC data dictionary)"""
        # This maps to the 125-field CIViC schema
        # Based on the data dictionary in your docs
        return {
            # Evidence Fields
            "evidence_id": "Unique identifier for the evidence item",
            "evidence_name": "Display name for the evidence",
            "evidence_description": "Detailed description of the evidence",
            "evidence_level": "Evidence level (A/B/C/D/E)",
            "evidence_type": "Type of evidence (PREDICTIVE, PROGNOSTIC, DIAGNOSTIC, etc.)",
            "evidence_direction": "Direction (SUPPORTS, DOES_NOT_SUPPORT)",
            "evidence_rating": "Star rating (1-5)",
            "evidence_significance": "Clinical significance",
            "evidence_status": "Curation status",

            # Disease Fields
            "disease_id": "CIViC disease ID",
            "disease_name": "Primary disease name",
            "disease_doid": "Disease Ontology ID (DOID)",

            # Variant Fields
            "variant_id": "CIViC variant ID",
            "variant_name": "Short variant name",
            "variant_hgvs": "HGVS notation",
            "variant_clinvar_id": "ClinVar ID",

            # Gene Fields
            "gene_id": "Gene identifier",
            "gene_name": "HGNC gene symbol",
            "gene_entrez_id": "Entrez gene ID",

            # Therapy Fields
            "therapy_id": "Therapy identifier",
            "therapy_name": "Drug/therapy name",
            "therapy_ncit_id": "NCI Thesaurus ID",
            "therapy_interaction_type": "COMBINATION, SEQUENTIAL, SUBSTITUTES",

            # Outcome Fields
            "phenotype_id": "Phenotype identifier",
            "phenotype_name": "Phenotype name",
            "phenotype_hpo_id": "Human Phenotype Ontology ID",

            # Source/Provenance Fields
            "source_id": "Source identifier (maps to paper_key)",
            "source_type": "Source type (PubMed, ASH, ASCO, etc.)",
            "citation": "Full citation",
            "pmid": "PubMed ID",
            "doi": "Digital Object Identifier",
            "publication_year": "Year of publication",

            # Trial Fields
            "clinical_trial_id": "Clinical trial identifier (NCT number)",

            # Molecular Profile
            "molecular_profile_id": "Molecular profile ID",
            "molecular_profile_name": "Molecular profile description",

            # Coordinates
            "chromosome": "Chromosome number",
            "start_position": "Genomic start position",
            "stop_position": "Genomic stop position",
            "reference_build": "Genome build (GRCh37, GRCh38)",
        }

    def get_paper_summary(self, source_id: str) -> Optional[PaperMetadataSummary]:
        """Get aggregated summary for a paper by source_id"""
        if self.df is None:
            return None

        # Filter rows for this source_id
        paper_df = self.df[self.df['source_id'] == source_id]

        if len(paper_df) == 0:
            print(f"❌ No data found for source_id: {source_id}")
            return None

        print(f"\n{'='*80}")
        print(f"Paper Summary: {source_id}")
        print(f"{'='*80}")
        print(f"Evidence items: {len(paper_df)}")

        # Aggregate data
        first_row = paper_df.iloc[0]

        # Collect unique genes, diseases, therapies
        genes = paper_df['gene_name'].dropna().unique().tolist() if 'gene_name' in paper_df.columns else []
        diseases = paper_df['disease_name'].dropna().unique().tolist() if 'disease_name' in paper_df.columns else []
        therapies = paper_df['therapy_name'].dropna().unique().tolist() if 'therapy_name' in paper_df.columns else []
        evidence_types = paper_df['evidence_type'].dropna().unique().tolist() if 'evidence_type' in paper_df.columns else []
        evidence_levels = paper_df['evidence_level'].dropna().unique().tolist() if 'evidence_level' in paper_df.columns else []

        # Construct S3 path
        paper_key = first_row.get('paper_key')
        if pd.notna(paper_key):
            asset_base_path = f"https://ali-bedrock-batch-2025.s3.us-east-1.amazonaws.com/civic_full_extraction/{paper_key}"
        else:
            asset_base_path = None

        summary = PaperMetadataSummary(
            source_id=source_id,
            paper_key=str(paper_key) if pd.notna(paper_key) else None,
            citation=str(first_row.get('citation')) if pd.notna(first_row.get('citation')) else None,
            pmid=str(first_row.get('pmid')) if pd.notna(first_row.get('pmid')) else None,
            doi=str(first_row.get('doi')) if pd.notna(first_row.get('doi')) else None,
            publication_year=int(first_row.get('publication_year')) if pd.notna(first_row.get('publication_year')) else None,
            genes=genes,
            diseases=diseases,
            therapies=therapies,
            evidence_count=len(paper_df),
            evidence_types=evidence_types,
            evidence_levels=evidence_levels,
            asset_base_path=asset_base_path
        )

        print(f"\nGenes: {', '.join(genes[:5])}{'...' if len(genes) > 5 else ''}")
        print(f"Diseases: {', '.join(diseases[:3])}{'...' if len(diseases) > 3 else ''}")
        print(f"Therapies: {', '.join(therapies[:3])}{'...' if len(therapies) > 3 else ''}")
        print(f"Evidence Types: {', '.join(evidence_types)}")
        print(f"Asset Path: {asset_base_path}")

        return summary

    def get_all_evidence_for_paper(self, source_id: str) -> List[Dict[str, Any]]:
        """Get all 125-column evidence items for a paper"""
        if self.df is None:
            return []

        paper_df = self.df[self.df['source_id'] == source_id]

        print(f"\n📊 Extracting {len(paper_df)} evidence items for {source_id}")

        # Convert to list of dicts (each dict has all 125 columns)
        evidence_items = paper_df.to_dict(orient='records')

        # Clean NaN values
        for item in evidence_items:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None

        return evidence_items

    def simulate_metadata_endpoint(self, source_id: str, include_evidence: bool = False) -> Dict[str, Any]:
        """Simulate GET /api/metadata/papers/{source_id}?includeEvidence="""

        print(f"\n{'='*80}")
        print(f"Simulating Metadata Endpoint")
        print(f"GET /api/metadata/papers/{source_id}?includeEvidence={include_evidence}")
        print(f"{'='*80}")

        summary = self.get_paper_summary(source_id)

        if not summary:
            return {"error": "Paper not found", "source_id": source_id}

        response = {
            "source_id": source_id,
            "summary": asdict(summary),
            "columns": [col.column_name for col in self.column_metadata],
        }

        if include_evidence:
            response["evidence"] = self.get_all_evidence_for_paper(source_id)

        return response

    def get_all_papers_list(self, limit: int = 100, offset: int = 0) -> List[PaperMetadataSummary]:
        """Simulate GET /api/metadata/papers?limit=&offset="""
        if self.df is None:
            return []

        print(f"\n{'='*80}")
        print(f"Simulating Papers List Endpoint")
        print(f"GET /api/metadata/papers?limit={limit}&offset={offset}")
        print(f"{'='*80}")

        # Get unique source_ids
        unique_sources = self.df['source_id'].dropna().unique()

        print(f"Total unique papers: {len(unique_sources)}")
        print(f"Returning: {offset} to {offset + limit}")

        # Paginate
        paginated_sources = unique_sources[offset:offset + limit]

        summaries = []
        for source_id in paginated_sources:
            summary = self.get_paper_summary(source_id)
            if summary:
                summaries.append(summary)

        return summaries


def run_comprehensive_test():
    """Run comprehensive metadata integration test"""

    print("="*80)
    print("METADATA INTEGRATION TEST")
    print("="*80)

    parser = MetadataParser()

    # Step 1: Load data
    if not parser.load_data():
        print("\n❌ Cannot proceed without data")
        return

    # Step 2: Analyze columns
    parser.analyze_columns()

    # Step 3: Test sample papers
    sample_source_ids = [
        "1",    # First paper
        "10",   # 10th paper
        "100",  # 100th paper
    ]

    results = {}

    for source_id in sample_source_ids:
        # Test metadata endpoint (without evidence)
        response_summary = parser.simulate_metadata_endpoint(source_id, include_evidence=False)
        results[f"paper_{source_id}_summary"] = response_summary

        # Test metadata endpoint (with full evidence)
        response_full = parser.simulate_metadata_endpoint(source_id, include_evidence=True)
        results[f"paper_{source_id}_full"] = response_full

    # Step 4: Test papers list endpoint
    papers_list = parser.get_all_papers_list(limit=10, offset=0)
    results["papers_list"] = [asdict(p) for p in papers_list]

    # Save results
    output_file = "metadata_test_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n✅ Test results saved to: {output_file}")

    print("\n" + "="*80)
    print("METADATA TEST COMPLETE")
    print("="*80)


if __name__ == "__main__":
    run_comprehensive_test()
