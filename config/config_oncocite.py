"""
Configuration file for OncoCITE 18-Agent System
Supports both OpenAI Agents SDK and Qwen-Agent Framework
"""

import os
from dataclasses import dataclass
from typing import Optional, Literal


@dataclass
class OncoCITEConfig:
    """Configuration settings for OncoCITE system"""

    # Framework Selection
    agent_framework: Literal["openai", "qwen"] = "qwen"  # Choose: "openai" or "qwen"

    # OpenAI API Configuration (for OpenAI framework)
    openai_api_key: Optional[str] = None
    default_model: str = "gpt-4o"
    reasoning_model: str = "o1"  # For complex reasoning tasks
    fast_model: str = "gpt-4o-mini"  # For simple extractions

    # Qwen API Configuration (for Qwen-Agent framework)
    dashscope_api_key: Optional[str] = None
    qwen_model: str = "qwen-max-latest"  # DashScope model name
    qwen_model_server: Optional[str] = None  # For local deployment: e.g., "http://localhost:8000/v1"
    qwen_model_local: str = "Qwen2.5-7B-Instruct"  # Local model name if using vLLM/Ollama

    # Agent Configuration
    use_parallel_tools: bool = True
    max_tokens: int = 4000
    max_input_tokens: int = 58000  # For Qwen models
    temperature_extraction: float = 0.7  # Tier 1
    temperature_normalization: float = 0.5  # Tier 2
    temperature_validation: float = 0.3  # Tier 3
    temperature_consolidation: float = 0.1  # Tier 4

    # Pipeline Configuration
    enable_tier1: bool = True
    enable_tier2: bool = True
    enable_tier3: bool = True
    enable_tier4: bool = True

    # Data paths
    data_directory: str = "/home/user/Final_Dataset_Civic"
    civic_data_file: str = "all_combined_extracted_data_with_source_counts.xlsx"
    output_directory: str = "output"

    # Logging
    verbose: bool = True
    log_file: str = "oncocite_pipeline.log"

    # Performance
    batch_size: int = 10  # For batch processing
    timeout_seconds: int = 300  # 5 minutes per operation

    # Validation thresholds
    min_confidence_score: float = 0.7
    require_human_review_below: float = 0.5

    def __post_init__(self):
        """Load API keys from environment if not provided"""
        if self.openai_api_key is None:
            self.openai_api_key = os.getenv("OPENAI_API_KEY")

        if self.dashscope_api_key is None:
            self.dashscope_api_key = os.getenv("DASHSCOPE_API_KEY")

        # Warn based on selected framework
        if self.agent_framework == "openai" and not self.openai_api_key:
            print("⚠️  WARNING: OPENAI_API_KEY not found in environment (required for OpenAI framework)")
        elif self.agent_framework == "qwen" and not self.dashscope_api_key and not self.qwen_model_server:
            print("⚠️  WARNING: DASHSCOPE_API_KEY not found and no local model server configured (required for Qwen framework)")

    def get_qwen_llm_config(self) -> dict:
        """
        Get LLM configuration for Qwen-Agent framework

        Returns:
            dict: LLM configuration for Qwen-Agent
        """
        if self.qwen_model_server:
            # Use local deployment (vLLM, Ollama, etc.)
            return {
                'model': self.qwen_model_local,
                'model_server': self.qwen_model_server,
                'api_key': 'EMPTY',
                'generate_cfg': {
                    'max_input_tokens': self.max_input_tokens,
                }
            }
        else:
            # Use DashScope
            return {
                'model': self.qwen_model,
                'model_type': 'qwen_dashscope',
                'api_key': self.dashscope_api_key,
                'generate_cfg': {
                    'max_input_tokens': self.max_input_tokens,
                }
            }

    @classmethod
    def from_env(cls):
        """Create configuration from environment variables"""
        agent_framework = os.getenv("ONCOCITE_AGENT_FRAMEWORK", "qwen")

        config = cls(
            agent_framework=agent_framework,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
            default_model=os.getenv("ONCOCITE_DEFAULT_MODEL", "gpt-4o"),
            qwen_model=os.getenv("ONCOCITE_QWEN_MODEL", "qwen-max-latest"),
            qwen_model_server=os.getenv("ONCOCITE_QWEN_MODEL_SERVER"),
            qwen_model_local=os.getenv("ONCOCITE_QWEN_MODEL_LOCAL", "Qwen2.5-7B-Instruct"),
            verbose=os.getenv("ONCOCITE_VERBOSE", "true").lower() == "true"
        )

        return config


# Default configuration instance
DEFAULT_CONFIG = OncoCITEConfig()


# CIViC Evidence Type Mappings
EVIDENCE_TYPES = {
    "PREDICTIVE": "Therapy sensitivity/resistance",
    "PROGNOSTIC": "Patient outcome association",
    "DIAGNOSTIC": "Disease diagnosis/classification",
    "PREDISPOSING": "Cancer predisposition/risk",
    "ONCOGENIC": "Tumor pathogenesis involvement",
    "FUNCTIONAL": "Protein functional impact"
}

# Evidence Levels
EVIDENCE_LEVELS = {
    "A": "Validated - FDA/guideline recognized",
    "B": "Clinical - Trials, cohort studies",
    "C": "Case Study - Individual patient reports",
    "D": "Preclinical - In vitro/in vivo studies"
}

# AMP/ASCO/CAP Tiers
AMP_TIERS = {
    "I": "Strong clinical significance",
    "II": "Potential clinical significance",
    "III": "Unknown clinical significance",
    "IV": "Benign or likely benign"
}

# Ontology endpoints (for future API integration)
ONTOLOGY_ENDPOINTS = {
    "DOID": "https://disease-ontology.org",
    "NCIt": "https://ncit.nci.nih.gov",
    "HGVS": "https://varnomen.hgvs.org",
    "SO": "http://www.sequenceontology.org",
    "HPO": "https://hpo.jax.org",
    "DrugBank": "https://go.drugbank.com",
    "ClinicalTrials": "https://clinicaltrials.gov"
}
