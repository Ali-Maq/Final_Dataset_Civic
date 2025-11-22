"""
End-to-End Pipeline Test with Real Data

Tests the complete oncoCITE pipeline using actual S3 data:
1. Fetch paper from S3
2. Run extraction pipeline
3. Compare with Excel metadata
4. Validate outputs

Author: OncoCITE Testing Suite
Date: 2025-11-13
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import json
import requests
from typing import Dict, Optional
from test_s3_data_access import S3DataTester, PaperAssetMap
from test_metadata_integration import MetadataParser

# Try to import oncoCITE orchestrator
try:
    from src.agents.oncocite_agents import OncoCITEOrchestrator, ExtractionContext, CIViCSchema
    ONCOCITE_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  OncoCITE orchestrator not available: {e}")
    ONCOCITE_AVAILABLE = False


class EndToEndTester:
    """Complete end-to-end pipeline tester"""

    def __init__(self):
        self.s3_tester = S3DataTester()
        self.metadata_parser = MetadataParser()
        self.test_results = {
            "s3_access": {},
            "metadata_validation": {},
            "extraction_pipeline": {},
            "comparison": {}
        }

    async def test_paper_pipeline(self, source_id: str, paper_id: str) -> Dict:
        """
        Test complete pipeline for a paper:
        1. Validate S3 assets exist
        2. Fetch markdown content
        3. Get Excel metadata
        4. Run oncoCITE extraction
        5. Compare results
        """

        print("\n" + "="*80)
        print(f"END-TO-END PIPELINE TEST")
        print(f"Source ID: {source_id} | Paper ID: {paper_id}")
        print("="*80)

        results = {
            "source_id": source_id,
            "paper_id": paper_id,
            "steps": {}
        }

        # STEP 1: Test S3 Access
        print("\n📦 STEP 1: Testing S3 Access")
        print("-" * 80)
        s3_results = self.s3_tester.test_paper_assets(paper_id)
        results["steps"]["s3_access"] = s3_results

        # STEP 2: Fetch Markdown Content
        print("\n📄 STEP 2: Fetching Markdown Content")
        print("-" * 80)
        markdown_content = self.s3_tester.fetch_markdown_content(paper_id)

        if not markdown_content:
            print("❌ Cannot proceed without markdown content")
            results["status"] = "FAILED_NO_CONTENT"
            return results

        results["steps"]["markdown_fetch"] = {
            "success": True,
            "content_length": len(markdown_content),
            "preview": markdown_content[:500]
        }

        # STEP 3: Load Excel Metadata
        print("\n📊 STEP 3: Loading Excel Metadata")
        print("-" * 80)
        if not self.metadata_parser.load_data():
            print("❌ Cannot load Excel metadata")
            results["status"] = "FAILED_NO_METADATA"
            return results

        # Get ground truth from Excel
        excel_metadata = self.metadata_parser.simulate_metadata_endpoint(
            source_id, include_evidence=True
        )
        results["steps"]["metadata_load"] = excel_metadata

        # STEP 4: Run OncoCITE Extraction Pipeline
        print("\n🤖 STEP 4: Running OncoCITE Extraction Pipeline")
        print("-" * 80)

        if not ONCOCITE_AVAILABLE:
            print("⚠️  OncoCITE orchestrator not available - skipping extraction")
            results["steps"]["extraction"] = {"skipped": True, "reason": "OncoCITE not available"}
        else:
            try:
                orchestrator = OncoCITEOrchestrator(verbose=True)
                extraction_result = await orchestrator.process_literature(markdown_content)

                results["steps"]["extraction"] = {
                    "success": True,
                    "output": extraction_result.model_dump() if hasattr(extraction_result, 'model_dump') else str(extraction_result)
                }

                print("✅ Extraction completed successfully")

            except Exception as e:
                print(f"❌ Extraction failed: {e}")
                results["steps"]["extraction"] = {"success": False, "error": str(e)}

        # STEP 5: Compare Results
        print("\n🔍 STEP 5: Comparing Extraction vs Excel Ground Truth")
        print("-" * 80)

        comparison = self.compare_results(
            extracted=results["steps"].get("extraction", {}).get("output"),
            ground_truth=excel_metadata
        )
        results["steps"]["comparison"] = comparison

        # STEP 6: Validation Summary
        print("\n✅ STEP 6: Validation Summary")
        print("-" * 80)
        self.print_validation_summary(results)

        results["status"] = "COMPLETE"
        return results

    def compare_results(self, extracted: Optional[Dict], ground_truth: Dict) -> Dict:
        """Compare extracted data with Excel ground truth"""

        if not extracted:
            return {"status": "NO_EXTRACTION", "matches": {}}

        comparison = {
            "status": "COMPARED",
            "matches": {},
            "mismatches": {},
            "missing_in_extraction": {},
            "extra_in_extraction": {}
        }

        # Get first evidence item from ground truth as representative
        if "evidence" in ground_truth and len(ground_truth["evidence"]) > 0:
            gt_evidence = ground_truth["evidence"][0]

            # Key fields to compare
            key_fields = [
                "disease_name", "gene_name", "variant_name",
                "therapy_name", "evidence_type", "evidence_level",
                "evidence_direction", "pmid"
            ]

            for field in key_fields:
                gt_value = gt_evidence.get(field)
                extracted_value = extracted.get(field)

                if gt_value == extracted_value:
                    comparison["matches"][field] = {
                        "value": gt_value,
                        "match": True
                    }
                else:
                    comparison["mismatches"][field] = {
                        "ground_truth": gt_value,
                        "extracted": extracted_value
                    }

        return comparison

    def print_validation_summary(self, results: Dict):
        """Print formatted validation summary"""

        print("\n" + "="*80)
        print("VALIDATION SUMMARY")
        print("="*80)

        # S3 Access
        s3_summary = results["steps"].get("s3_access", {}).get("summary", {})
        s3_rate = s3_summary.get("success_rate", 0) * 100
        print(f"\n📦 S3 Assets: {s3_rate:.1f}% accessible")

        # Metadata
        metadata = results["steps"].get("metadata_load", {})
        if "summary" in metadata:
            meta_summary = metadata["summary"]
            print(f"📊 Metadata: {meta_summary.get('evidence_count', 0)} evidence items")
            print(f"   Genes: {', '.join(meta_summary.get('genes', [])[:3])}")
            print(f"   Diseases: {', '.join(meta_summary.get('diseases', [])[:2])}")

        # Extraction
        extraction = results["steps"].get("extraction", {})
        if extraction.get("success"):
            print(f"🤖 Extraction: ✅ SUCCESS")
        elif extraction.get("skipped"):
            print(f"🤖 Extraction: ⚠️  SKIPPED ({extraction.get('reason')})")
        else:
            print(f"🤖 Extraction: ❌ FAILED")

        # Comparison
        comparison = results["steps"].get("comparison", {})
        if comparison.get("status") == "COMPARED":
            matches = len(comparison.get("matches", {}))
            mismatches = len(comparison.get("mismatches", {}))
            print(f"🔍 Comparison: {matches} matches, {mismatches} mismatches")

        print("\n" + "="*80)


async def run_test_suite():
    """Run full test suite"""

    print("="*80)
    print("END-TO-END INTEGRATION TEST SUITE")
    print("="*80)

    tester = EndToEndTester()

    # Test papers (add real source_id and paper_id pairs)
    test_cases = [
        {"source_id": "1", "paper_id": "PMID_29151359"},  # Example: Replace with real IDs
    ]

    all_results = []

    for test_case in test_cases:
        result = await tester.test_paper_pipeline(
            source_id=test_case["source_id"],
            paper_id=test_case["paper_id"]
        )
        all_results.append(result)

    # Save results
    output_file = "end_to_end_test_results.json"
    with open(output_file, "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n✅ Full test results saved to: {output_file}")

    print("\n" + "="*80)
    print("TEST SUITE COMPLETE")
    print("="*80)


if __name__ == "__main__":
    asyncio.run(run_test_suite())
