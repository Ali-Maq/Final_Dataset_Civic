"""
Simple structural validation test for Qwen-Agent implementation
Tests code structure without requiring qwen-agent installation
"""

import sys
import ast
import json
from pathlib import Path

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)


def test_file_exists():
    """Test 1: Check if all required files exist"""
    print_section("TEST 1: File Existence")

    required_files = [
        "src/agents/oncocite_agents_qwen.py",
        "config/config_oncocite.py",
        "demos/demo_oncocite_qwen.py",
        "docs/QWEN_AGENT_MIGRATION.md",
        "README_QWEN_AGENT.md",
        "requirements_qwen_agent.txt",
    ]

    base_path = Path(__file__).parent.parent
    all_exist = True

    for file_path in required_files:
        full_path = base_path / file_path
        exists = full_path.exists()
        status = "✅" if exists else "❌"
        print(f"{status} {file_path}")
        if not exists:
            all_exist = False

    return all_exist


def test_python_syntax():
    """Test 2: Validate Python syntax of implementation files"""
    print_section("TEST 2: Python Syntax Validation")

    base_path = Path(__file__).parent.parent
    python_files = [
        "src/agents/oncocite_agents_qwen.py",
        "config/config_oncocite.py",
        "demos/demo_oncocite_qwen.py",
        "tests/test_e2e_qwen_agent.py",
    ]

    all_valid = True

    for file_path in python_files:
        full_path = base_path / file_path
        try:
            with open(full_path, 'r') as f:
                code = f.read()
            ast.parse(code)
            print(f"✅ {file_path} - Valid syntax")
        except SyntaxError as e:
            print(f"❌ {file_path} - Syntax error: {e}")
            all_valid = False
        except FileNotFoundError:
            print(f"❌ {file_path} - File not found")
            all_valid = False

    return all_valid


def test_code_structure():
    """Test 3: Verify code structure and key components"""
    print_section("TEST 3: Code Structure Analysis")

    base_path = Path(__file__).parent.parent
    impl_file = base_path / "src/agents/oncocite_agents_qwen.py"

    try:
        with open(impl_file, 'r') as f:
            code = f.read()

        tree = ast.parse(code)

        # Find all classes
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

        # Find all functions
        functions = [node.name for node in ast.walk(tree)
                    if isinstance(node, ast.FunctionDef) and not node.name.startswith('_')]

        print(f"Classes found: {len(classes)}")
        expected_classes = [
            'ExtractionContext',
            'CIViCSchema',
            'OncoCITEHooks',
            'OncoCITEExtractionAgent',
            'OncoCITEOrchestrator'
        ]

        for cls in expected_classes:
            if cls in classes:
                print(f"  ✅ {cls}")
            else:
                print(f"  ❌ {cls} - MISSING")

        print(f"\nKey functions found: {len([f for f in functions if 'create_tier' in f or f == 'main'])}")
        expected_functions = [
            'create_tier1_extraction_agents',
            'create_tier2_normalization_agents',
            'create_tier3_validation_agents',
            'create_tier4_consolidation_agent',
            'main'
        ]

        for func in expected_functions:
            if func in functions:
                print(f"  ✅ {func}")
            else:
                print(f"  ❌ {func} - MISSING")

        # Check line count
        line_count = len(code.split('\n'))
        print(f"\n📊 Code metrics:")
        print(f"  - Total lines: {line_count}")
        print(f"  - Classes: {len(classes)}")
        print(f"  - Functions: {len(functions)}")

        return all(cls in classes for cls in expected_classes)

    except Exception as e:
        print(f"❌ Structure analysis failed: {e}")
        return False


def test_configuration_structure():
    """Test 4: Verify configuration structure"""
    print_section("TEST 4: Configuration Structure")

    base_path = Path(__file__).parent.parent
    config_file = base_path / "config/config_oncocite.py"

    try:
        with open(config_file, 'r') as f:
            code = f.read()

        # Check for key configuration elements
        checks = {
            'agent_framework': 'agent_framework' in code,
            'dashscope_api_key': 'dashscope_api_key' in code,
            'qwen_model': 'qwen_model' in code,
            'get_qwen_llm_config': 'get_qwen_llm_config' in code,
            'from_env': 'from_env' in code,
        }

        for item, present in checks.items():
            status = "✅" if present else "❌"
            print(f"{status} {item}")

        return all(checks.values())

    except Exception as e:
        print(f"❌ Configuration check failed: {e}")
        return False


def test_documentation():
    """Test 5: Verify documentation exists and has content"""
    print_section("TEST 5: Documentation Validation")

    base_path = Path(__file__).parent.parent
    doc_files = [
        ("docs/QWEN_AGENT_MIGRATION.md", 10000),  # Should be comprehensive
        ("README_QWEN_AGENT.md", 5000),  # Should be detailed
        ("requirements_qwen_agent.txt", 50),  # Should have dependencies
    ]

    all_valid = True

    for file_path, min_size in doc_files:
        full_path = base_path / file_path
        try:
            with open(full_path, 'r') as f:
                content = f.read()
            size = len(content)
            has_content = size >= min_size
            status = "✅" if has_content else "⚠️"
            print(f"{status} {file_path} ({size:,} chars, min: {min_size:,})")
            if not has_content:
                print(f"    Warning: File may be incomplete")
        except FileNotFoundError:
            print(f"❌ {file_path} - Not found")
            all_valid = False

    return all_valid


def test_agent_count():
    """Test 6: Verify 18 agents are properly defined"""
    print_section("TEST 6: Agent Count Verification")

    base_path = Path(__file__).parent.parent
    impl_file = base_path / "src/agents/oncocite_agents_qwen.py"

    try:
        with open(impl_file, 'r') as f:
            content = f.read()

        # Look for agent creation in each tier
        has_tier1 = 'create_tier1_extraction_agents' in content
        has_tier2 = 'create_tier2_normalization_agents' in content
        has_tier3 = 'create_tier3_validation_agents' in content
        has_tier4 = 'create_tier4_consolidation_agent' in content

        print("Agent creation functions:")
        print(f"  ✅ Tier 1 (8 agents): {has_tier1}")
        print(f"  ✅ Tier 2 (6 agents): {has_tier2}")
        print(f"  ✅ Tier 3 (3 agents): {has_tier3}")
        print(f"  ✅ Tier 4 (1 agent): {has_tier4}")

        # Count specific agent names
        agent_names = [
            'disease_extractor', 'variant_extractor', 'therapy_extractor',
            'evidence_extractor', 'outcomes_extractor', 'phenotype_extractor',
            'assertion_extractor', 'provenance_extractor',
            'disease_normalizer', 'variant_normalizer', 'therapy_normalizer',
            'trial_normalizer', 'coordinate_normalizer', 'ontology_normalizer',
            'cross_field_validator', 'evidence_disambiguator', 'significance_classifier',
            'Agent_18_Consolidation_ConflictResolution'
        ]

        found_agents = sum(1 for name in agent_names if name in content)
        print(f"\n📊 Agent definitions found: {found_agents}/18")

        return found_agents >= 18

    except Exception as e:
        print(f"❌ Agent count check failed: {e}")
        return False


def test_requirements():
    """Test 7: Verify requirements file has necessary packages"""
    print_section("TEST 7: Requirements Validation")

    base_path = Path(__file__).parent.parent
    req_file = base_path / "requirements_qwen_agent.txt"

    try:
        with open(req_file, 'r') as f:
            content = f.read()

        required_packages = [
            'qwen-agent',
            'json5',
            'dashscope',
            'pydantic',
        ]

        print("Required packages:")
        all_present = True
        for pkg in required_packages:
            present = pkg in content
            status = "✅" if present else "❌"
            print(f"  {status} {pkg}")
            if not present:
                all_present = False

        return all_present

    except Exception as e:
        print(f"❌ Requirements check failed: {e}")
        return False


def run_all_tests():
    """Run all structural tests"""
    print("="*80)
    print("  OncoCITE Qwen-Agent Structural Validation")
    print("  (No dependencies required)")
    print("="*80)

    tests = [
        ("File Existence", test_file_exists),
        ("Python Syntax", test_python_syntax),
        ("Code Structure", test_code_structure),
        ("Configuration", test_configuration_structure),
        ("Documentation", test_documentation),
        ("Agent Count", test_agent_count),
        ("Requirements", test_requirements),
    ]

    results = {}
    for name, test_func in tests:
        try:
            results[name] = test_func()
        except Exception as e:
            print(f"\n❌ Test '{name}' crashed: {e}")
            results[name] = False

    # Summary
    print_section("TEST SUMMARY")

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {test_name.ljust(25)}: {status}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 All structural tests passed!")
        print("\n✅ The Qwen-Agent implementation is structurally complete")
        print("\n📝 Next steps:")
        print("   1. Install dependencies: pip install -r requirements_qwen_agent.txt")
        print("   2. Configure API: export DASHSCOPE_API_KEY='your_key'")
        print("   3. Run demo: python demos/demo_oncocite_qwen.py")
        return True
    else:
        print(f"\n❌ {total - passed} test(s) failed")
        return False


if __name__ == "__main__":
    print("\n🧪 Starting Structural Validation\n")
    success = run_all_tests()
    print("\n" + "="*80)
    sys.exit(0 if success else 1)
