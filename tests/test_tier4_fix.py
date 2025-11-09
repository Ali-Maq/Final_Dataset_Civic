"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
Quick test to verify Tier 4 fix
"""

import asyncio
import os

# Check for API key in environment
if not os.getenv('OPENAI_API_KEY'):
    print("❌ ERROR: OPENAI_API_KEY environment variable not set")
    print("Please set your API key: export OPENAI_API_KEY='your-key-here'")
    exit(1)

from src.agents.oncocite_agents import OncoCITEOrchestrator

async def test_full_pipeline():
    print("="*80)
    print("TESTING TIER 4 FIX - FULL PIPELINE")
    print("="*80)

    sample_text = """
    EGFR L858R mutation in non-small cell lung adenocarcinoma.
    Treatment with gefitinib showed 70% response rate in 50 patients.
    Median PFS was 9.2 months (95% CI: 7.1-11.3, p<0.001).
    """

    orchestrator = OncoCITEOrchestrator(verbose=True)

    try:
        print("\n🚀 Running full pipeline with Tier 4 fix...\n")
        result = await orchestrator.process_literature(sample_text)

        print("\n✅ SUCCESS! Tier 4 is now working!")
        print("="*80)
        print("FINAL STRUCTURED OUTPUT:")
        print("="*80)

        # Display key results
        output_dict = result.model_dump()
        for key, value in output_dict.items():
            if value is not None:
                if isinstance(value, str) and len(value) > 80:
                    print(f"{key}: {value[:80]}...")
                elif value:
                    print(f"{key}: {value}")

        # Completeness
        filled = sum(1 for v in output_dict.values() if v is not None)
        total = len(output_dict)
        print(f"\n📊 Field Completeness: {filled}/{total} ({filled/total*100:.1f}%)")

        return True

    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_full_pipeline())
    if success:
        print("\n🎉 ALL 4 TIERS NOW WORKING!")
    else:
        print("\n⚠️  Issue still present")
