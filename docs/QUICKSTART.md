# OncoCITE Quick Start Guide

## 5-Minute Setup

### Step 1: Install Dependencies

```bash
pip install openai-agents pandas openpyxl python-dotenv pydantic rich
```

### Step 2: Set API Key

```bash
export OPENAI_API_KEY='your-openai-api-key-here'
```

### Step 3: Run a Simple Test

Create `test_oncocite.py`:

```python
import asyncio
from oncocite_agents import OncoCITEOrchestrator

async def quick_test():
    # Sample text
    text = """
    EGFR L858R mutation in lung adenocarcinoma patients
    treated with gefitinib showed 70% response rate.
    """

    # Initialize and run
    orchestrator = OncoCITEOrchestrator(verbose=True)
    result = await orchestrator.process_literature(text)

    # Display results
    print(f"\nExtracted Evidence Type: {result.evidence_type}")
    print(f"Variant: {result.variant_names}")
    print(f"Disease: {result.disease_name}")

asyncio.run(quick_test())
```

Run it:
```bash
python test_oncocite.py
```

## What You Get

The system will:
1. Extract entities (disease, variant, therapy, evidence, outcomes)
2. Normalize to ontologies (DOID, HGVS, NCIt, etc.)
3. Validate cross-field consistency
4. Consolidate into structured 124-field output

## Agent Execution Flow

```
Input Text
    ↓
TIER 1 (Agents 1-8): Extract 8 entity types in parallel
    ↓
TIER 2 (Agents 9-14): Normalize to standard vocabularies
    ↓
TIER 3 (Agents 15-17): Validate and disambiguate
    ↓
TIER 4 (Agent 18): Consolidate and resolve conflicts
    ↓
Structured Output (124 fields)
```

## View Agent Activity

Enable verbose mode to see all 18 agents in action:

```python
orchestrator = OncoCITEOrchestrator(verbose=True)
```

You'll see output like:
```
[2024-01-15T10:30:00] 🟢 Agent_1_Disease_Extractor started
[2024-01-15T10:30:01] 🔧 Tool: extract_disease
[2024-01-15T10:30:02] ✅ Tool extract_disease completed
[2024-01-15T10:30:02] 🔴 Agent_1_Disease_Extractor completed (1.5s)
...
```

## Batch Processing

Process multiple evidence items:

```python
from demo_oncocite import demo_batch_processing
import asyncio

# Process 5 items from CIViC database
asyncio.run(demo_batch_processing(num_samples=5))
```

## Configuration

Customize in `config_oncocite.py`:

```python
# Use faster model for testing
DEFAULT_CONFIG.default_model = "gpt-4o-mini"

# Adjust confidence thresholds
DEFAULT_CONFIG.min_confidence_score = 0.6

# Change temperature for extraction
DEFAULT_CONFIG.temperature_extraction = 0.8
```

## Next Steps

1. **Read full documentation**: `README_ONCOCITE.md`
2. **Run comprehensive demo**: `python demo_oncocite.py`
3. **Explore individual agents**: See `oncocite_agents.py`
4. **Process your own data**: Modify `demo_oncocite.py`

## Troubleshooting

**Import Error?**
```bash
# Make sure you're in the right directory
cd Final_Dataset_Civic
python -c "import oncocite_agents; print('OK')"
```

**API Timeout?**
```python
# Increase timeout
DEFAULT_CONFIG.timeout_seconds = 600
```

**Want to test a single agent?**
```python
from oncocite_agents import create_tier1_extraction_agents
from agents import Runner

agents = create_tier1_extraction_agents()
disease_agent = agents['disease_extractor']

result = await Runner.run(
    disease_agent,
    "Extract disease from: metastatic lung adenocarcinoma"
)
print(result.final_output)
```

## Example Output

```json
{
  "evidence_type": "PREDICTIVE",
  "evidence_level": "B",
  "disease_name": "Lung Adenocarcinoma",
  "disease_doid": "DOID:3910",
  "variant_names": ["L858R"],
  "variant_hgvs_descriptions": ["p.Leu858Arg"],
  "therapy_names": ["Gefitinib"],
  "evidence_significance": "SENSITIVITY",
  "confidence_score": 0.92
}
```

---

**Ready to extract precision oncology knowledge at scale!** 🚀
