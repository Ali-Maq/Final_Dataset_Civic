"""
Demo script for OncoCITE 18-Agent System
Demonstrates how to use the system with actual CIViC data
"""

import asyncio
import json
import sys
import pandas as pd
from datetime import datetime
from pathlib import Path

# Import OncoCITE system from src/
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agents.oncocite_agents import (
    OncoCITEOrchestrator,
    ExtractionContext,
    CIViCSchema
)
from config.config_oncocite import DEFAULT_CONFIG


def load_civic_data(num_samples: int = 5):
    """Load sample data from CIViC xlsx file"""
    data_file = Path(DEFAULT_CONFIG.data_directory) / DEFAULT_CONFIG.civic_data_file

    print(f"📂 Loading CIViC data from: {data_file}")

    df = pd.read_excel(data_file)
    print(f"✅ Loaded {len(df)} total evidence items")
    print(f"📊 Sampling {num_samples} items for demo")

    # Sample some diverse evidence items
    samples = df.sample(n=min(num_samples, len(df)))

    return samples


def create_literature_text_from_evidence(row):
    """
    Convert a CIViC evidence row into simulated literature text
    In practice, this would be actual PDF/publication text
    """

    # Extract key fields
    evidence_desc = row.get('evidence_description', 'No description available')
    disease = row.get('disease_name', 'Unknown disease')
    variant = row.get('variant_names', 'Unknown variant')
    therapy = row.get('therapy_names', 'No therapy')
    evidence_type = row.get('evidence_type', 'Unknown')
    evidence_level = row.get('evidence_level', 'Unknown')

    # Create simulated abstract/excerpt
    literature_text = f"""
TITLE: Clinical Evidence for {variant} in {disease}

ABSTRACT:
{evidence_desc}

METHODS: This {evidence_level}-level {evidence_type.lower()} evidence was derived from
clinical studies examining {variant} variants in patients with {disease}.

INTERVENTIONS: Treatment involved {therapy if pd.notna(therapy) else 'standard care'}.

RESULTS: The observed clinical outcomes and molecular profile characteristics are
described in the evidence statement above.

CONCLUSIONS: This evidence contributes to understanding the clinical actionability
of {variant} in the context of {disease} treatment decisions.

Keywords: {disease}, {variant}, {therapy if pd.notna(therapy) else 'oncology'},
precision medicine, clinical genomics
"""

    return literature_text.strip()


async def demo_single_extraction(orchestrator, sample_text: str, sample_id: str):
    """
    Demonstrate single literature extraction through all 4 tiers
    """
    print("\n" + "="*80)
    print(f"🔬 PROCESSING SAMPLE: {sample_id}")
    print("="*80)

    print(f"\n📄 Input Text Preview:")
    print("-" * 80)
    print(sample_text[:500] + "..." if len(sample_text) > 500 else sample_text)
    print("-" * 80)

    try:
        # Run the full pipeline
        result = await orchestrator.process_literature(sample_text)

        print(f"\n✅ Extraction completed for {sample_id}")

        # Display key results
        print("\n📋 KEY EXTRACTED FIELDS:")
        print("-" * 80)

        if result.evidence_type:
            print(f"Evidence Type: {result.evidence_type}")
        if result.evidence_level:
            print(f"Evidence Level: {result.evidence_level}")
        if result.disease_name:
            print(f"Disease: {result.disease_name}")
        if result.variant_names:
            print(f"Variants: {', '.join(result.variant_names)}")
        if result.therapy_names:
            print(f"Therapies: {', '.join(result.therapy_names)}")
        if result.confidence_score:
            print(f"Confidence Score: {result.confidence_score:.2%}")

        print("-" * 80)

        return result

    except Exception as e:
        print(f"\n❌ Error processing {sample_id}: {str(e)}")
        return None


async def demo_batch_processing(num_samples: int = 3):
    """
    Demonstrate batch processing of multiple evidence items
    """
    print("\n" + "="*80)
    print("🚀 ONCOCITE DEMO: BATCH PROCESSING")
    print("="*80)
    print(f"Processing {num_samples} evidence items from CIViC database")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("="*80)

    # Load sample data
    samples = load_civic_data(num_samples)

    # Initialize orchestrator
    print("\n🔧 Initializing OncoCITE 18-Agent System...")
    orchestrator = OncoCITEOrchestrator(verbose=True)

    # Process each sample
    results = []
    for idx, (_, row) in enumerate(samples.iterrows(), 1):
        evidence_id = row.get('evidence_id', f'EID{idx}')
        sample_text = create_literature_text_from_evidence(row)

        result = await demo_single_extraction(
            orchestrator,
            sample_text,
            f"Evidence Item {evidence_id}"
        )

        if result:
            results.append({
                'evidence_id': evidence_id,
                'result': result,
                'original_data': row
            })

        # Small delay between samples
        if idx < len(samples):
            print("\n⏸️  Pausing before next sample...")
            await asyncio.sleep(2)

    # Summary
    print("\n" + "="*80)
    print("📊 BATCH PROCESSING SUMMARY")
    print("="*80)
    print(f"Total samples processed: {len(results)}")
    print(f"Successful extractions: {len([r for r in results if r is not None])}")

    # Save results
    output_dir = Path(DEFAULT_CONFIG.output_directory)
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / f"oncocite_demo_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    # Convert results to serializable format
    serializable_results = []
    for r in results:
        serializable_results.append({
            'evidence_id': str(r['evidence_id']),
            'extracted_data': r['result'].model_dump() if r['result'] else None,
            'original_evidence_description': str(r['original_data'].get('evidence_description', ''))
        })

    with open(output_file, 'w') as f:
        json.dump(serializable_results, f, indent=2, default=str)

    print(f"\n💾 Results saved to: {output_file}")

    return results


async def demo_individual_agents():
    """
    Demonstrate individual agent capabilities
    """
    print("\n" + "="*80)
    print("🔍 DEMO: INDIVIDUAL AGENT CAPABILITIES")
    print("="*80)

    from oncocite_agents import (
        create_tier1_extraction_agents,
        create_tier2_normalization_agents,
        create_tier3_validation_agents
    )

    # Test Tier 1 - Disease Extractor
    print("\n📌 Testing Agent 1: Disease Extractor")
    print("-" * 80)

    agents_t1 = create_tier1_extraction_agents()
    disease_agent = agents_t1['disease_extractor']

    sample_text = """
    This phase III trial enrolled 500 patients with metastatic non-small cell lung
    adenocarcinoma (NSCLC). The study focused on stage IV disease with confirmed
    histological diagnosis according to WHO criteria.
    """

    from agents import Runner
    result = await Runner.run(disease_agent, f"Extract disease info from: {sample_text}")
    print(f"Disease extraction result:\n{result.final_output}")

    # Test Tier 2 - Variant Normalizer
    print("\n📌 Testing Agent 10: Variant Normalizer")
    print("-" * 80)

    agents_t2 = create_tier2_normalization_agents()
    variant_agent = agents_t2['variant_normalizer']

    variant_text = """
    {
      "gene_name": "EGFR",
      "variant_name": "L858R",
      "variant_type": "missense"
    }
    """

    result = await Runner.run(variant_agent, f"Normalize this variant: {variant_text}")
    print(f"Variant normalization result:\n{result.final_output}")

    print("\n✅ Individual agent demos completed")


async def main():
    """Main demo entry point"""

    print("\n" + "="*80)
    print("ONCOCITE 18-AGENT SYSTEM - COMPREHENSIVE DEMO")
    print("Built with OpenAI Agents SDK")
    print("="*80)

    # Check API key
    if not DEFAULT_CONFIG.openai_api_key:
        print("\n❌ ERROR: OPENAI_API_KEY not found in environment")
        print("Please set your OpenAI API key:")
        print("  export OPENAI_API_KEY='your-api-key-here'")
        return

    print(f"\n✅ OpenAI API Key configured")
    print(f"Using model: {DEFAULT_CONFIG.default_model}")

    # Choose demo mode
    print("\n" + "="*80)
    print("DEMO OPTIONS:")
    print("="*80)
    print("1. Individual agent capabilities (quick)")
    print("2. Single evidence item extraction (moderate)")
    print("3. Batch processing (comprehensive, slower)")

    # For automated demo, run option 1 (quick)
    demo_choice = "1"

    if demo_choice == "1":
        await demo_individual_agents()
    elif demo_choice == "2":
        samples = load_civic_data(1)
        row = samples.iloc[0]
        text = create_literature_text_from_evidence(row)
        orchestrator = OncoCITEOrchestrator(verbose=True)
        await demo_single_extraction(orchestrator, text, f"EID{row['evidence_id']}")
    elif demo_choice == "3":
        await demo_batch_processing(num_samples=3)

    print("\n" + "="*80)
    print("✅ DEMO COMPLETED")
    print("="*80)


if __name__ == "__main__":
    # Run the demo
    print("🚀 Starting OncoCITE Demo...")
    print("⚠️  Note: This requires a valid OPENAI_API_KEY")

    # Uncomment to run:
    asyncio.run(main())

    # Or use in Jupyter/notebook:
    # await main()
