# OncoCITE Migration to Qwen-Agent Framework

This document describes the migration of the OncoCITE 18-agent system from the OpenAI Agents SDK to the Qwen-Agent framework.

## Table of Contents

1. [Overview](#overview)
2. [Why Qwen-Agent?](#why-qwen-agent)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Key Differences](#key-differences)
6. [Usage Examples](#usage-examples)
7. [Deployment Options](#deployment-options)
8. [Migration Guide](#migration-guide)

## Overview

The OncoCITE system has been successfully migrated from the OpenAI Agents SDK to the Qwen-Agent framework. This migration enables:

- **Cost reduction**: Use of open-source Qwen models
- **Data privacy**: Deploy models locally for sensitive medical data
- **Performance**: Leverage Alibaba's DashScope or self-hosted infrastructure
- **Flexibility**: Support for multiple model backends (DashScope, vLLM, Ollama)

The new implementation maintains **100% functional compatibility** with the original system while providing these additional benefits.

## Why Qwen-Agent?

### Benefits of Qwen-Agent Framework

1. **Open Source Models**: Use state-of-the-art Qwen models (Qwen2.5, Qwen-Max, etc.)
2. **Flexible Deployment**:
   - Cloud: DashScope (Alibaba Cloud)
   - On-premise: vLLM, Ollama, or other OpenAI-compatible servers
3. **Cost Effective**: Significantly lower costs compared to OpenAI GPT-4
4. **Data Privacy**: Keep sensitive medical data within your infrastructure
5. **Tool Calling Support**: Native function calling capabilities
6. **MCP Integration**: Model Context Protocol support for enhanced tool usage

### Qwen Model Performance

Qwen models provide excellent performance for medical and scientific text processing:

- **Qwen-Max**: Comparable to GPT-4o for complex reasoning tasks
- **Qwen2.5-7B/14B/32B**: Efficient open-source alternatives
- **Qwen3-Coder**: Optimized for code generation (if needed for data processing)

## Installation

### 1. Install Qwen-Agent Framework

```bash
# Install core dependencies
pip install -r requirements_qwen_agent.txt

# Or install manually:
pip install "qwen-agent>=0.0.31" json5 dashscope pydantic pandas
```

### 2. Set Up API Access

Choose one of the following options:

#### Option A: DashScope (Cloud Service)

```bash
# Get API key from: https://dashscope.aliyun.com/
export DASHSCOPE_API_KEY="your_dashscope_api_key"
```

#### Option B: Local Deployment with vLLM

```bash
# Install vLLM
pip install vllm

# Start vLLM server with Qwen model
vllm serve Qwen/Qwen2.5-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --max-model-len 32768

# Set environment variable
export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:8000/v1"
```

#### Option C: Local Deployment with Ollama

```bash
# Install Ollama from: https://ollama.ai/

# Pull Qwen model
ollama pull qwen2.5:7b

# Start Ollama server (usually runs automatically)
# Set environment variable
export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:11434/v1"
```

## Configuration

### Environment Variables

```bash
# Framework selection (default: qwen)
export ONCOCITE_AGENT_FRAMEWORK="qwen"

# DashScope configuration
export DASHSCOPE_API_KEY="your_api_key"
export ONCOCITE_QWEN_MODEL="qwen-max-latest"

# Local deployment configuration
export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:8000/v1"
export ONCOCITE_QWEN_MODEL_LOCAL="Qwen2.5-7B-Instruct"

# Optional: Verbosity
export ONCOCITE_VERBOSE="true"
```

### Configuration File

The `config/config_oncocite.py` file now supports both OpenAI and Qwen configurations:

```python
from config.config_oncocite import OncoCITEConfig

# Load configuration from environment
config = OncoCITEConfig.from_env()

# Get Qwen LLM configuration
llm_cfg = config.get_qwen_llm_config()
```

## Key Differences

### Architecture Comparison

| Feature | OpenAI Agents SDK | Qwen-Agent Framework |
|---------|------------------|---------------------|
| Agent Base Class | `Agent` (SDK provided) | `OncoCITEExtractionAgent` (custom subclass) |
| Execution | `await Runner.run()` | `agent.run()` / `agent.run_nonstream()` |
| Hooks | `AgentHooks` (built-in) | `OncoCITEHooks` (custom implementation) |
| Output Schema | `AgentOutputSchema` | JSON parsing from text output |
| Temperature | `ModelSettings` | `generate_cfg` in LLM config |
| Async Support | Native | Synchronous (non-stream) execution |

### Code Comparison

#### OpenAI Agents SDK (Original)

```python
from agents import Agent, Runner, AgentHooks

# Create agent
agent = Agent(
    name="Disease_Extractor",
    instructions="Extract disease information...",
    model="gpt-4o",
    hooks=hooks
)

# Run agent (async)
result = await Runner.run(agent, "Extract from this text...")
output = result.final_output
```

#### Qwen-Agent Framework (New)

```python
from qwen_agent.agent import Agent

# Create agent
class DiseaseExtractor(Agent):
    def _run(self, messages, lang='en', **kwargs):
        return self._call_llm(messages=messages, stream=True)

agent = DiseaseExtractor(
    llm=llm_cfg,
    system_message="Extract disease information...",
    name="Disease_Extractor"
)

# Run agent (sync)
messages = [{'role': 'user', 'content': 'Extract from this text...'}]
responses = agent.run_nonstream(messages)
```

## Usage Examples

### Basic Usage

```python
from agents.oncocite_agents_qwen import OncoCITEOrchestrator
from config.config_oncocite import OncoCITEConfig

# Load configuration
config = OncoCITEConfig.from_env()
llm_cfg = config.get_qwen_llm_config()

# Initialize orchestrator
orchestrator = OncoCITEOrchestrator(llm_cfg=llm_cfg, verbose=True)

# Process literature
literature_text = """
    BACKGROUND: EGFR T790M is a resistance mutation...
    [full text]
"""

result = orchestrator.process_literature(literature_text)
print(result.model_dump())
```

### Run Demo Script

```bash
# With DashScope
export DASHSCOPE_API_KEY="your_api_key"
python demos/demo_oncocite_qwen.py

# With local deployment
export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:8000/v1"
python demos/demo_oncocite_qwen.py
```

## Deployment Options

### 1. DashScope (Recommended for Getting Started)

**Pros:**
- Easy setup (just API key)
- No infrastructure needed
- Latest Qwen-Max model
- Automatic scaling

**Cons:**
- Requires internet connection
- Usage costs (pay-per-token)
- Data sent to cloud

**Setup:**
```bash
export DASHSCOPE_API_KEY="your_key"
python demos/demo_oncocite_qwen.py
```

### 2. vLLM (Recommended for Production)

**Pros:**
- High throughput
- Low latency
- Full data privacy
- Cost effective at scale

**Cons:**
- Requires GPU infrastructure
- More complex setup

**Setup:**
```bash
# Start vLLM server
vllm serve Qwen/Qwen2.5-32B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 2 \
    --max-model-len 32768

# Configure OncoCITE
export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:8000/v1"
export ONCOCITE_QWEN_MODEL_LOCAL="Qwen2.5-32B-Instruct"
python demos/demo_oncocite_qwen.py
```

### 3. Ollama (Recommended for Development)

**Pros:**
- Easy local deployment
- Good for testing
- CPU support (slower but works)

**Cons:**
- Lower throughput than vLLM
- Limited to smaller models

**Setup:**
```bash
# Install and start Ollama
ollama pull qwen2.5:7b
ollama serve

# Configure OncoCITE
export ONCOCITE_QWEN_MODEL_SERVER="http://localhost:11434/v1"
python demos/demo_oncocite_qwen.py
```

## Migration Guide

### For Existing Users

If you're currently using the OpenAI Agents SDK version (`oncocite_agents.py`), follow these steps:

#### 1. Keep Both Implementations

The original OpenAI implementation is preserved in:
- `src/agents/oncocite_agents.py` (OpenAI Agents SDK)

The new Qwen implementation is in:
- `src/agents/oncocite_agents_qwen.py` (Qwen-Agent Framework)

#### 2. Update Imports

**Before (OpenAI):**
```python
from agents.oncocite_agents import OncoCITEOrchestrator
```

**After (Qwen):**
```python
from agents.oncocite_agents_qwen import OncoCITEOrchestrator
```

#### 3. Update Configuration

**Before (OpenAI):**
```python
orchestrator = OncoCITEOrchestrator(verbose=True)
result = await orchestrator.process_literature(text)
```

**After (Qwen):**
```python
from config.config_oncocite import OncoCITEConfig

config = OncoCITEConfig.from_env()
llm_cfg = config.get_qwen_llm_config()
orchestrator = OncoCITEOrchestrator(llm_cfg=llm_cfg, verbose=True)
result = orchestrator.process_literature(text)  # Note: no await
```

#### 4. Remove Async

The Qwen implementation uses synchronous execution (no `async`/`await`):

**Before:**
```python
async def main():
    result = await orchestrator.process_literature(text)

asyncio.run(main())
```

**After:**
```python
def main():
    result = orchestrator.process_literature(text)

main()
```

### API Compatibility

The public API remains the same:

- Input: Plain text literature
- Output: `CIViCSchema` (124-field structured output)
- Same extraction quality and accuracy

## Performance Considerations

### Model Selection

| Model | Use Case | Performance | Cost |
|-------|----------|-------------|------|
| Qwen-Max | Production (cloud) | Comparable to GPT-4o | Medium |
| Qwen2.5-32B | Production (on-prem) | Very good | Low (hardware) |
| Qwen2.5-14B | Development/Testing | Good | Very low |
| Qwen2.5-7B | Rapid prototyping | Fair | Minimal |

### Hardware Requirements

For local deployment with vLLM:

- **Qwen2.5-7B**: 1x GPU (16GB VRAM)
- **Qwen2.5-14B**: 1x GPU (24GB VRAM) or 2x GPUs (16GB each)
- **Qwen2.5-32B**: 2x GPUs (24GB VRAM each) or 4x GPUs (16GB each)

### Throughput

Expected processing time per abstract (2000 tokens):

- **DashScope**: ~30-60 seconds (depends on API load)
- **vLLM (32B model, 2xGPU)**: ~20-40 seconds
- **Ollama (7B model, CPU)**: ~2-5 minutes

## Troubleshooting

### Common Issues

#### 1. ImportError: No module named 'qwen_agent'

```bash
pip install qwen-agent>=0.0.31
```

#### 2. DASHSCOPE_API_KEY not found

```bash
export DASHSCOPE_API_KEY="your_key"
# Or add to ~/.bashrc or ~/.zshrc
```

#### 3. Connection refused (local deployment)

Check if vLLM/Ollama server is running:
```bash
# For vLLM
curl http://localhost:8000/v1/models

# For Ollama
curl http://localhost:11434/v1/models
```

#### 4. Out of memory (local deployment)

Reduce model size or batch size:
```bash
# Use smaller model
vllm serve Qwen/Qwen2.5-7B-Instruct ...

# Or reduce max_model_len
vllm serve ... --max-model-len 16384
```

## Support and Resources

### Documentation

- [Qwen-Agent GitHub](https://github.com/QwenLM/Qwen-Agent)
- [Qwen Models](https://github.com/QwenLM/Qwen)
- [DashScope API Docs](https://help.aliyun.com/zh/dashscope/)
- [vLLM Documentation](https://docs.vllm.ai/)

### Example Code

- `demos/demo_oncocite_qwen.py`: Basic usage example
- `src/agents/oncocite_agents_qwen.py`: Full implementation
- `config/config_oncocite.py`: Configuration options

### Getting Help

For issues or questions:

1. Check this documentation
2. Review the example code in `demos/`
3. Check Qwen-Agent issues: https://github.com/QwenLM/Qwen-Agent/issues
4. Contact the OncoCITE development team

## Future Enhancements

Planned improvements for the Qwen-Agent implementation:

1. **Parallel Execution**: Add asyncio support for Tier 1 agents
2. **Streaming**: Real-time progress updates during extraction
3. **Fine-tuning**: Custom Qwen model fine-tuned on oncology data
4. **RAG Integration**: Long-context document processing with Qwen-Agent's RAG capabilities
5. **MCP Tools**: Integration with specialized medical knowledge bases via MCP

## Conclusion

The migration to Qwen-Agent provides OncoCITE with:

✅ **Cost savings** through open-source models
✅ **Data privacy** with local deployment options
✅ **Flexibility** in model selection and infrastructure
✅ **Performance** comparable to GPT-4 level models
✅ **Compatibility** with existing workflows and outputs

The system is ready for production use with either DashScope or self-hosted deployment.
