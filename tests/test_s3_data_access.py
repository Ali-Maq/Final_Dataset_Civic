"""
Test S3 Data Access and Paper Asset Retrieval

Tests access to the actual S3 bucket and validates paper asset structure:
https://ali-bedrock-batch-2025.s3.us-east-1.amazonaws.com/civic_full_extraction/<paper_id>/

Author: OncoCITE Testing Suite
Date: 2025-11-13
"""

import requests
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class PaperAssetMap:
    """Maps expected assets for a paper in S3"""
    paper_id: str
    base_url: str

    @property
    def pdf_url(self) -> str:
        return f"{self.base_url}/{self.paper_id}.pdf"

    @property
    def markdown_url(self) -> str:
        return f"{self.base_url}/extracted_text/clean_document.md"

    @property
    def context_graph_url(self) -> str:
        return f"{self.base_url}/metadata/context_graph.json"

    @property
    def full_output_url(self) -> str:
        return f"{self.base_url}/raw_output/full_output_with_grounding.md"

    def visualization_url(self, page_num: int) -> str:
        return f"{self.base_url}/visualizations/page{page_num}_annotated.jpg"

    def image_url(self, image_name: str) -> str:
        return f"{self.base_url}/extracted_images/{image_name}"


class S3DataTester:
    """Test S3 data access and validate asset structure"""

    def __init__(self, base_s3_url: str = "https://ali-bedrock-batch-2025.s3.us-east-1.amazonaws.com/civic_full_extraction"):
        self.base_s3_url = base_s3_url
        self.test_results = []

    def get_asset_map(self, paper_id: str) -> PaperAssetMap:
        """Generate asset map for a given paper_id"""
        base_url = f"{self.base_s3_url}/{paper_id}"
        return PaperAssetMap(paper_id=paper_id, base_url=base_url)

    def test_url_accessibility(self, url: str, description: str = "") -> Dict:
        """Test if a URL is accessible and return metadata"""
        result = {
            "url": url,
            "description": description,
            "accessible": False,
            "status_code": None,
            "content_type": None,
            "content_length": None,
            "error": None
        }

        try:
            print(f"  Testing: {description or url}")
            response = requests.head(url, timeout=10, allow_redirects=True)
            result["status_code"] = response.status_code
            result["accessible"] = response.status_code == 200
            result["content_type"] = response.headers.get("Content-Type")
            result["content_length"] = response.headers.get("Content-Length")

            if result["accessible"]:
                print(f"    ✅ Accessible ({result['content_type']}, {result['content_length']} bytes)")
            else:
                print(f"    ❌ Not accessible (HTTP {result['status_code']})")

        except requests.RequestException as e:
            result["error"] = str(e)
            print(f"    ❌ Error: {e}")

        self.test_results.append(result)
        return result

    def test_paper_assets(self, paper_id: str) -> Dict:
        """Test all expected assets for a paper"""
        print(f"\n{'='*80}")
        print(f"Testing Paper Assets: {paper_id}")
        print(f"{'='*80}")

        asset_map = self.get_asset_map(paper_id)

        results = {
            "paper_id": paper_id,
            "base_url": asset_map.base_url,
            "assets": {}
        }

        # Test core assets
        print("\n📄 Core Document Assets:")
        results["assets"]["pdf"] = self.test_url_accessibility(
            asset_map.pdf_url,
            f"PDF: {paper_id}.pdf"
        )

        results["assets"]["markdown"] = self.test_url_accessibility(
            asset_map.markdown_url,
            "Markdown: clean_document.md"
        )

        results["assets"]["context_graph"] = self.test_url_accessibility(
            asset_map.context_graph_url,
            "Context Graph: context_graph.json"
        )

        results["assets"]["full_output"] = self.test_url_accessibility(
            asset_map.full_output_url,
            "Full Output: full_output_with_grounding.md"
        )

        # Test visualizations (try first few pages)
        print("\n🖼️  Visualization Assets:")
        results["assets"]["visualizations"] = []
        for page_num in range(1, 4):  # Test first 3 pages
            viz_result = self.test_url_accessibility(
                asset_map.visualization_url(page_num),
                f"Visualization: page{page_num}_annotated.jpg"
            )
            results["assets"]["visualizations"].append(viz_result)

        # Calculate summary
        total_tests = len(self.test_results)
        accessible = sum(1 for r in self.test_results if r["accessible"])

        print(f"\n{'='*80}")
        print(f"Summary: {accessible}/{total_tests} assets accessible ({accessible/total_tests*100:.1f}%)")
        print(f"{'='*80}\n")

        results["summary"] = {
            "total_tests": total_tests,
            "accessible": accessible,
            "inaccessible": total_tests - accessible,
            "success_rate": accessible / total_tests if total_tests > 0 else 0
        }

        return results

    def fetch_markdown_content(self, paper_id: str) -> Optional[str]:
        """Fetch and return markdown content from S3"""
        asset_map = self.get_asset_map(paper_id)
        url = asset_map.markdown_url

        try:
            print(f"\n📥 Fetching markdown content from: {url}")
            response = requests.get(url, timeout=30)

            if response.status_code == 200:
                content = response.text
                print(f"✅ Successfully fetched {len(content)} characters")
                print(f"   Preview: {content[:200]}...")
                return content
            else:
                print(f"❌ Failed to fetch (HTTP {response.status_code})")
                return None

        except requests.RequestException as e:
            print(f"❌ Error fetching markdown: {e}")
            return None

    def fetch_context_graph(self, paper_id: str) -> Optional[Dict]:
        """Fetch and parse context graph JSON"""
        asset_map = self.get_asset_map(paper_id)
        url = asset_map.context_graph_url

        try:
            print(f"\n📥 Fetching context graph from: {url}")
            response = requests.get(url, timeout=30)

            if response.status_code == 200:
                data = response.json()
                print(f"✅ Successfully parsed context graph")
                print(f"   Keys: {list(data.keys())}")
                return data
            else:
                print(f"❌ Failed to fetch (HTTP {response.status_code})")
                return None

        except requests.RequestException as e:
            print(f"❌ Error fetching context graph: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing JSON: {e}")
            return None


def test_sample_papers():
    """Test a sample of papers from the S3 bucket"""

    # Sample paper IDs to test (you can add real paper IDs here)
    sample_paper_ids = [
        "PMID_29151359",  # Example: FLAURA trial (osimertinib)
        "PMID_26412456",  # Example: another trial
        "PMID_123456",    # Test non-existent paper
    ]

    tester = S3DataTester()

    all_results = []

    for paper_id in sample_paper_ids:
        result = tester.test_paper_assets(paper_id)
        all_results.append(result)

        # If accessible, try fetching content
        if result["summary"]["accessible"] > 0:
            markdown = tester.fetch_markdown_content(paper_id)
            if markdown:
                result["markdown_preview"] = markdown[:500]

            context = tester.fetch_context_graph(paper_id)
            if context:
                result["context_graph_keys"] = list(context.keys())

    # Save results
    output_file = "s3_test_results.json"
    with open(output_file, "w") as f:
        json.dump(all_results, indent=2, fp=f)

    print(f"\n✅ Test results saved to: {output_file}")

    return all_results


if __name__ == "__main__":
    print("="*80)
    print("S3 Data Access Tester")
    print("Testing: https://ali-bedrock-batch-2025.s3.us-east-1.amazonaws.com")
    print("="*80)

    results = test_sample_papers()

    print("\n" + "="*80)
    print("TESTING COMPLETE")
    print("="*80)
