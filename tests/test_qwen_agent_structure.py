"""
Basic structure tests for Qwen-Agent implementation
These tests verify the implementation structure without requiring API keys
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")

    try:
        from agents.oncocite_agents_qwen import (
            OncoCITEOrchestrator,
            OncoCITEExtractionAgent,
            OncoCITEHooks,
            ExtractionContext,
            CIViCSchema,
            create_tier1_extraction_agents,
            create_tier2_normalization_agents,
            create_tier3_validation_agents,
            create_tier4_consolidation_agent
        )
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False


def test_config():
    """Test configuration loading"""
    print("\nTesting configuration...")

    try:
        from config.config_oncocite import OncoCITEConfig

        # Create config with qwen framework
        config = OncoCITEConfig(agent_framework="qwen")

        # Test get_qwen_llm_config method
        llm_cfg = config.get_qwen_llm_config()

        assert 'model' in llm_cfg
        assert 'generate_cfg' in llm_cfg

        print("✅ Configuration loading successful")
        print(f"   Default model: {llm_cfg['model']}")
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False


def test_data_models():
    """Test data model initialization"""
    print("\nTesting data models...")

    try:
        from agents.oncocite_agents_qwen import ExtractionContext, CIViCSchema

        # Test ExtractionContext
        context = ExtractionContext(literature_text="Test text")
        assert context.literature_text == "Test text"
        assert context.disease_extraction is None

        # Test CIViCSchema
        schema = CIViCSchema()
        assert schema.evidence_id is None

        # Test with data
        schema_with_data = CIViCSchema(
            evidence_level="A",
            disease_name="Non-small cell lung cancer",
            variant_names=["T790M"]
        )
        assert schema_with_data.evidence_level == "A"
        assert schema_with_data.disease_name == "Non-small cell lung cancer"

        print("✅ Data models working correctly")
        return True
    except Exception as e:
        print(f"❌ Data model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_hooks():
    """Test monitoring hooks"""
    print("\nTesting hooks...")

    try:
        from agents.oncocite_agents_qwen import OncoCITEHooks

        hooks = OncoCITEHooks()

        # Test hook methods
        hooks.on_start("TestAgent")
        assert "TestAgent" in hooks.agent_call_counts
        assert hooks.agent_call_counts["TestAgent"] == 1

        hooks.on_end("TestAgent")

        summary = hooks.get_summary()
        assert summary["total_agents"] == 1

        print("✅ Hooks working correctly")
        return True
    except Exception as e:
        print(f"❌ Hooks test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_agent_structure():
    """Test agent structure (without LLM calls)"""
    print("\nTesting agent structure...")

    try:
        from agents.oncocite_agents_qwen import (
            create_tier1_extraction_agents,
            create_tier2_normalization_agents,
            create_tier3_validation_agents,
            create_tier4_consolidation_agent
        )

        # Mock LLM config
        llm_cfg = {
            'model': 'test-model',
            'model_type': 'qwen_dashscope',
            'api_key': 'test-key',
            'generate_cfg': {
                'max_input_tokens': 58000,
            }
        }

        # Create agents (they will fail if called, but structure should work)
        tier1 = create_tier1_extraction_agents(llm_cfg)
        assert len(tier1) == 8
        assert 'disease_extractor' in tier1
        assert 'variant_extractor' in tier1

        tier2 = create_tier2_normalization_agents(llm_cfg)
        assert len(tier2) == 6
        assert 'disease_normalizer' in tier2

        tier3 = create_tier3_validation_agents(llm_cfg)
        assert len(tier3) == 3
        assert 'cross_field_validator' in tier3

        tier4 = create_tier4_consolidation_agent(llm_cfg)
        assert tier4.name == "Agent_18_Consolidation_ConflictResolution"

        print("✅ Agent structure correct")
        print(f"   Tier 1: {len(tier1)} agents")
        print(f"   Tier 2: {len(tier2)} agents")
        print(f"   Tier 3: {len(tier3)} agents")
        print(f"   Tier 4: 1 agent")
        return True
    except Exception as e:
        print(f"❌ Agent structure test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_orchestrator_init():
    """Test orchestrator initialization (without LLM calls)"""
    print("\nTesting orchestrator initialization...")

    try:
        from agents.oncocite_agents_qwen import OncoCITEOrchestrator

        # Mock LLM config
        llm_cfg = {
            'model': 'test-model',
            'model_type': 'qwen_dashscope',
            'api_key': 'test-key',
            'generate_cfg': {
                'max_input_tokens': 58000,
            }
        }

        orchestrator = OncoCITEOrchestrator(llm_cfg=llm_cfg, verbose=False)

        assert len(orchestrator.tier1_agents) == 8
        assert len(orchestrator.tier2_agents) == 6
        assert len(orchestrator.tier3_agents) == 3
        assert orchestrator.tier4_agent is not None

        print("✅ Orchestrator initialization successful")
        return True
    except Exception as e:
        print(f"❌ Orchestrator initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all tests"""
    print("="*80)
    print("Qwen-Agent Implementation Structure Tests")
    print("="*80)
    print()

    tests = [
        test_imports,
        test_config,
        test_data_models,
        test_hooks,
        test_agent_structure,
        test_orchestrator_init
    ]

    results = []
    for test in tests:
        result = test()
        results.append(result)

    print("\n" + "="*80)
    print("Test Summary")
    print("="*80)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("✅ All tests passed!")
        return True
    else:
        print(f"❌ {total - passed} test(s) failed")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
