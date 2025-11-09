"""
Comprehensive Test Suite for OncoCITE 18-Agent System
Tests all 4 tiers and the complete pipeline
"""

import asyncio
import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Check for API key in environment
if not os.getenv('OPENAI_API_KEY'):
    print("❌ ERROR: OPENAI_API_KEY environment variable not set")
    print("Please set your API key: export OPENAI_API_KEY='your-key-here'")
    exit(1)

print("="*80)
print("ONCOCITE 18-AGENT SYSTEM - COMPREHENSIVE TEST SUITE")
print("="*80)
print(f"Test Start Time: {datetime.now().isoformat()}")
print("="*80)

# Import system components
try:
    from src.agents.oncocite_agents import (
        OncoCITEOrchestrator,
        create_tier1_extraction_agents,
        create_tier2_normalization_agents,
        create_tier3_validation_agents,
        create_tier4_consolidation_agent,
        ExtractionContext
    )
    from agents import Runner
    print("✅ All imports successful")
except Exception as e:
    print(f"❌ Import error: {e}")
    exit(1)


# Test Data Samples
SAMPLE_TEXTS = {
    "predictive_evidence": """
        BACKGROUND: EGFR T790M is a common resistance mutation in non-small cell lung cancer (NSCLC).

        METHODS: We conducted a phase III clinical trial (NCT02296125) with 419 patients with advanced
        NSCLC harboring the EGFR T790M mutation. Patients were randomized to receive osimertinib (80 mg
        daily) or platinum-pemetrexed chemotherapy.

        RESULTS: The median progression-free survival (PFS) was 10.1 months (95% CI: 8.3-12.3) in the
        osimertinib group versus 4.4 months (95% CI: 4.2-5.6) in the chemotherapy group (HR 0.30,
        p<0.001). Overall response rate (ORR) was 71% vs 31% (p<0.001).

        CONCLUSIONS: Osimertinib demonstrates superior efficacy compared to chemotherapy in EGFR T790M
        positive NSCLC patients.
    """,

    "diagnostic_evidence": """
        The World Health Organization (WHO) classification defines acute myeloid leukemia with mutated
        NPM1 as a provisional entity. NPM1 mutations are detected in approximately 30% of adult AML
        cases and are particularly common in cytogenetically normal AML. The presence of NPM1 mutation
        should be tested in clinical trials and is recommended for testing in all patients with
        cytogenetically normal AML according to NCCN guidelines.
    """,

    "prognostic_evidence": """
        In a cohort study of 406 patients with chronic lymphocytic leukemia (CLL), TP53 mutations were
        detected in 12% of patients. Patients with TP53 mutations had significantly worse overall
        survival (median OS: 2.5 years) compared to TP53 wild-type patients (median OS: 8.2 years,
        p<0.001). The 5-year survival rate was 15% for TP53 mutated vs 65% for TP53 wild-type.
    """
}


async def test_tier1_individual_agents():
    """Test individual Tier 1 extraction agents"""
    print("\n" + "="*80)
    print("TEST 1: TIER 1 INDIVIDUAL AGENTS")
    print("="*80)

    agents = create_tier1_extraction_agents()
    sample_text = SAMPLE_TEXTS["predictive_evidence"]

    tests = [
        ("Disease Extractor", agents['disease_extractor'], "Extract disease information"),
        ("Variant Extractor", agents['variant_extractor'], "Extract variant information"),
        ("Therapy Extractor", agents['therapy_extractor'], "Extract therapy information"),
        ("Evidence Extractor", agents['evidence_extractor'], "Extract evidence classification"),
    ]

    results = {}

    for agent_name, agent, instruction in tests:
        print(f"\n🔬 Testing {agent_name}...")
        try:
            result = await Runner.run(
                agent,
                f"{instruction} from this text:\n\n{sample_text[:500]}"
            )
            results[agent_name] = {
                "status": "✅ SUCCESS",
                "output": str(result.final_output)[:200] + "..."
            }
            print(f"   ✅ {agent_name} completed")
            print(f"   Output preview: {str(result.final_output)[:100]}...")
        except Exception as e:
            results[agent_name] = {
                "status": "❌ FAILED",
                "error": str(e)
            }
            print(f"   ❌ {agent_name} failed: {e}")

    return results


async def test_tier2_normalization():
    """Test Tier 2 normalization agents"""
    print("\n" + "="*80)
    print("TEST 2: TIER 2 NORMALIZATION AGENTS")
    print("="*80)

    agents = create_tier2_normalization_agents()

    # Sample extracted data to normalize
    test_data = {
        "Disease Normalizer": {
            "agent": agents['disease_normalizer'],
            "input": '{"disease_name": "Non-small cell lung cancer", "disease_subtype": "adenocarcinoma"}'
        },
        "Variant Normalizer": {
            "agent": agents['variant_normalizer'],
            "input": '{"gene_name": "EGFR", "variant_name": "T790M", "variant_type": "missense"}'
        },
        "Therapy Normalizer": {
            "agent": agents['therapy_normalizer'],
            "input": '{"drug_names": ["Osimertinib"], "treatment_line": "second-line"}'
        }
    }

    results = {}

    for agent_name, data in test_data.items():
        print(f"\n🔗 Testing {agent_name}...")
        try:
            result = await Runner.run(
                data['agent'],
                f"Normalize this information:\n{data['input']}"
            )
            results[agent_name] = {
                "status": "✅ SUCCESS",
                "output": str(result.final_output)[:200] + "..."
            }
            print(f"   ✅ {agent_name} completed")
            print(f"   Output preview: {str(result.final_output)[:100]}...")
        except Exception as e:
            results[agent_name] = {
                "status": "❌ FAILED",
                "error": str(e)
            }
            print(f"   ❌ {agent_name} failed: {e}")

    return results


async def test_tier3_validation():
    """Test Tier 3 validation agents"""
    print("\n" + "="*80)
    print("TEST 3: TIER 3 VALIDATION AGENTS")
    print("="*80)

    agents = create_tier3_validation_agents()

    # Sample data for validation
    validation_input = {
        "disease": {"name": "NSCLC", "doid": "DOID:3908"},
        "variant": {"gene": "EGFR", "name": "T790M", "hgvs": "p.Thr790Met"},
        "therapy": {"drug": "Osimertinib", "class": "EGFR inhibitor"},
        "evidence": {"type": "PREDICTIVE", "direction": "SUPPORTS", "significance": "SENSITIVITY"}
    }

    print(f"\n✓ Testing Cross-field Validator...")
    try:
        result = await Runner.run(
            agents['cross_field_validator'],
            f"Validate consistency of this data:\n{json.dumps(validation_input, indent=2)}"
        )
        print(f"   ✅ Cross-field validation completed")
        print(f"   Output preview: {str(result.final_output)[:150]}...")
        validation_result = {
            "status": "✅ SUCCESS",
            "output": str(result.final_output)[:200]
        }
    except Exception as e:
        print(f"   ❌ Validation failed: {e}")
        validation_result = {
            "status": "❌ FAILED",
            "error": str(e)
        }

    return {"Cross-field Validator": validation_result}


async def test_full_pipeline():
    """Test the complete 4-tier pipeline"""
    print("\n" + "="*80)
    print("TEST 4: FULL PIPELINE (ALL 4 TIERS)")
    print("="*80)

    orchestrator = OncoCITEOrchestrator(verbose=True)
    sample_text = SAMPLE_TEXTS["predictive_evidence"]

    print(f"\n📄 Input Text Preview:")
    print("-" * 80)
    print(sample_text[:300] + "...")
    print("-" * 80)

    try:
        print("\n🚀 Starting full pipeline execution...\n")
        result = await orchestrator.process_literature(sample_text)

        print("\n" + "="*80)
        print("✅ FULL PIPELINE COMPLETED SUCCESSFULLY")
        print("="*80)

        # Display key results
        print("\n📊 EXTRACTED STRUCTURED DATA:")
        print("-" * 80)

        output_dict = result.model_dump()

        # Display non-null fields
        print("\n🔍 Key Extracted Fields:")
        for key, value in output_dict.items():
            if value is not None:
                # Format the output
                if isinstance(value, str) and len(value) > 100:
                    print(f"  • {key}: {value[:100]}...")
                elif isinstance(value, list) and len(value) > 0:
                    print(f"  • {key}: {value}")
                elif not isinstance(value, (list, dict)) or value:
                    print(f"  • {key}: {value}")

        # Summary statistics
        total_fields = len(output_dict)
        filled_fields = sum(1 for v in output_dict.values() if v is not None)
        completeness = (filled_fields / total_fields) * 100

        print("\n📈 PIPELINE STATISTICS:")
        print(f"  • Total schema fields: {total_fields}")
        print(f"  • Filled fields: {filled_fields}")
        print(f"  • Field completeness: {completeness:.1f}%")

        return {
            "status": "✅ SUCCESS",
            "completeness": completeness,
            "filled_fields": filled_fields,
            "total_fields": total_fields,
            "sample_output": {k: v for k, v in list(output_dict.items())[:10] if v is not None}
        }

    except Exception as e:
        print(f"\n❌ PIPELINE FAILED: {e}")
        import traceback
        traceback.print_exc()
        return {
            "status": "❌ FAILED",
            "error": str(e)
        }


async def test_multiple_evidence_types():
    """Test with different evidence types"""
    print("\n" + "="*80)
    print("TEST 5: MULTIPLE EVIDENCE TYPES")
    print("="*80)

    orchestrator = OncoCITEOrchestrator(verbose=False)  # Less verbose for multiple runs

    results = {}

    for evidence_type, text in SAMPLE_TEXTS.items():
        print(f"\n🧪 Testing {evidence_type}...")
        try:
            result = await orchestrator.process_literature(text)
            results[evidence_type] = {
                "status": "✅ SUCCESS",
                "evidence_type_detected": result.evidence_type,
                "disease": result.disease_name,
                "confidence": result.confidence_score
            }
            print(f"   ✅ {evidence_type} processed successfully")
            print(f"   Detected type: {result.evidence_type}")
        except Exception as e:
            results[evidence_type] = {
                "status": "❌ FAILED",
                "error": str(e)
            }
            print(f"   ❌ {evidence_type} failed: {e}")

    return results


async def run_all_tests():
    """Run all test suites"""
    print("\n" + "="*80)
    print("🧪 RUNNING COMPLETE TEST SUITE")
    print("="*80)

    all_results = {}

    # Test 1: Tier 1 Individual Agents
    try:
        all_results['tier1_agents'] = await test_tier1_individual_agents()
    except Exception as e:
        print(f"❌ Tier 1 test suite failed: {e}")
        all_results['tier1_agents'] = {"error": str(e)}

    # Test 2: Tier 2 Normalization
    try:
        all_results['tier2_normalization'] = await test_tier2_normalization()
    except Exception as e:
        print(f"❌ Tier 2 test suite failed: {e}")
        all_results['tier2_normalization'] = {"error": str(e)}

    # Test 3: Tier 3 Validation
    try:
        all_results['tier3_validation'] = await test_tier3_validation()
    except Exception as e:
        print(f"❌ Tier 3 test suite failed: {e}")
        all_results['tier3_validation'] = {"error": str(e)}

    # Test 4: Full Pipeline
    try:
        all_results['full_pipeline'] = await test_full_pipeline()
    except Exception as e:
        print(f"❌ Full pipeline test failed: {e}")
        all_results['full_pipeline'] = {"error": str(e)}

    # Test 5: Multiple Evidence Types (optional, may be skipped to save API calls)
    print("\n⏭️  Skipping Test 5 (Multiple Evidence Types) to conserve API usage")
    print("   You can enable this test by uncommenting in the code")
    # all_results['multiple_types'] = await test_multiple_evidence_types()

    # Final Summary
    print("\n" + "="*80)
    print("📋 TEST SUITE SUMMARY")
    print("="*80)

    # Count successes and failures
    total_tests = 0
    passed_tests = 0

    for suite_name, suite_results in all_results.items():
        if isinstance(suite_results, dict) and 'error' not in suite_results:
            suite_total = len(suite_results)
            suite_passed = sum(1 for r in suite_results.values()
                             if isinstance(r, dict) and r.get('status', '').startswith('✅'))
            print(f"\n{suite_name.upper()}: {suite_passed}/{suite_total} passed")
            total_tests += suite_total
            passed_tests += suite_passed
        else:
            print(f"\n{suite_name.upper()}: FAILED")

    print("\n" + "="*80)
    print(f"OVERALL: {passed_tests}/{total_tests} tests passed ({(passed_tests/total_tests*100):.1f}%)")
    print("="*80)

    # Save results
    output_file = f"test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)

    print(f"\n💾 Full test results saved to: {output_file}")
    print(f"Test End Time: {datetime.now().isoformat()}")

    return all_results


if __name__ == "__main__":
    print("\n🚀 Starting OncoCITE System Tests...")
    print("⚠️  Note: This will make multiple API calls to OpenAI")
    print("⏱️  Estimated time: 2-5 minutes\n")

    # Run all tests
    results = asyncio.run(run_all_tests())

    print("\n✅ All tests completed!")
    print("="*80)
