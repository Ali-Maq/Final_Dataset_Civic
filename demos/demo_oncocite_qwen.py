"""
Demo script for OncoCITE 18-Agent System with Qwen-Agent Framework

This script demonstrates how to use the OncoCITE system with Qwen models
instead of OpenAI models.

Usage:
    # With DashScope (Alibaba Cloud):
    export DASHSCOPE_API_KEY="your_api_key_here"
    python demo_oncocite_qwen.py

    # With local Qwen deployment (vLLM, Ollama, etc.):
    export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:8000/v1"
    python demo_oncocite_qwen.py
"""

import os
import sys
import json
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from agents.oncocite_agents_qwen import OncoCITEOrchestrator, CIViCSchema
from config.config_oncocite import OncoCITEConfig


def main():
    """Run OncoCITE demo with Qwen-Agent framework"""

    # Sample literature text (clinical trial abstract)
    sample_text = """
    BACKGROUND: EGFR T790M is a common resistance mutation in non-small cell lung cancer (NSCLC)
    that develops after treatment with first-generation EGFR tyrosine kinase inhibitors (TKIs).
    Osimertinib is a third-generation EGFR TKI designed to target this resistance mutation.

    METHODS: We conducted a randomized, open-label, phase III clinical trial (NCT02296125) with
    419 patients with histologically confirmed advanced NSCLC harboring the EGFR T790M mutation.
    Patients were randomized 2:1 to receive either osimertinib (80 mg once daily) or platinum-based
    chemotherapy plus pemetrexed.

    RESULTS: The median progression-free survival (PFS) was significantly longer in the osimertinib
    group compared to chemotherapy: 10.1 months (95% CI: 8.3-12.3) versus 4.4 months (95% CI: 4.2-5.6),
    with a hazard ratio of 0.30 (95% CI: 0.23-0.41; p<0.001). The objective response rate (ORR) was
    also superior: 71% versus 31% (p<0.001). Grade 3 or higher adverse events occurred in 23% of
    patients in the osimertinib group versus 47% in the chemotherapy group. Common adverse events
    in the osimertinib group included diarrhea (42%), rash (34%), and dry skin (31%).

    CONCLUSIONS: Osimertinib demonstrates superior efficacy and improved tolerability compared to
    platinum-pemetrexed chemotherapy in EGFR T790M-positive NSCLC patients who have progressed on
    prior EGFR TKI therapy. These results confirm osimertinib as the standard of care for this
    patient population.

    CLINICAL TRIAL REGISTRATION: ClinicalTrials.gov Identifier NCT02296125
    PUBLICATION: Published in New England Journal of Medicine, 2017
    DOI: 10.1056/NEJMoa1612674
    """

    print("="*80)
    print("OncoCITE 18-Agent System Demo - Qwen-Agent Framework")
    print("="*80)
    print()

    # Load configuration
    config = OncoCITEConfig.from_env()

    # Check if we have the necessary API key or model server
    if not config.dashscope_api_key and not config.qwen_model_server:
        print("❌ ERROR: No DashScope API key or local model server configured!")
        print()
        print("Please either:")
        print("1. Set DASHSCOPE_API_KEY environment variable for DashScope")
        print("   export DASHSCOPE_API_KEY='your_api_key_here'")
        print()
        print("2. Set ONCOCITE_QWEN_MODEL_SERVER for local deployment")
        print("   export ONCOCITE_QWEN_MODEL_SERVER='http://localhost:8000/v1'")
        print()
        return

    # Get LLM configuration
    llm_cfg = config.get_qwen_llm_config()

    print("Configuration:")
    if config.qwen_model_server:
        print(f"  Model Server: {config.qwen_model_server}")
        print(f"  Model: {config.qwen_model_local}")
    else:
        print(f"  Service: DashScope (Alibaba Cloud)")
        print(f"  Model: {config.qwen_model}")
    print()

    # Initialize orchestrator
    print("Initializing OncoCITE orchestrator...")
    orchestrator = OncoCITEOrchestrator(llm_cfg=llm_cfg, verbose=True)
    print()

    # Process literature
    print("Processing literature...")
    print(f"Input text length: {len(sample_text)} characters")
    print()

    try:
        result = orchestrator.process_literature(sample_text)

        # Display results
        print("\n" + "="*80)
        print("FINAL STRUCTURED OUTPUT (124-FIELD CIVIC SCHEMA)")
        print("="*80)
        print()

        result_dict = result.model_dump()

        # Print non-null fields
        print("Extracted Fields:")
        print("-" * 80)
        for key, value in result_dict.items():
            if value is not None:
                if isinstance(value, (dict, list)):
                    print(f"{key}:")
                    print(f"  {json.dumps(value, indent=4)}")
                else:
                    print(f"{key}: {value}")
        print()

        # Save results to file
        output_dir = Path(config.output_directory)
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / "demo_result_qwen.json"

        with open(output_file, 'w') as f:
            json.dump(result_dict, f, indent=2)

        print(f"✅ Results saved to: {output_file}")
        print()

    except Exception as e:
        print(f"\n❌ Error during processing: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
