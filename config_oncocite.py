"""
Configuration file for OncoCITE 18-Agent System
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class OncoCITEConfig:
    """Configuration settings for OncoCITE system"""

    # OpenAI API Configuration
    openai_api_key: Optional[str] = None
    default_model: str = "gpt-4o"
    reasoning_model: str = "o1"  # For complex reasoning tasks
    fast_model: str = "gpt-4o-mini"  # For simple extractions

    # Agent Configuration
    use_parallel_tools: bool = True
    max_tokens: int = 4000
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
        """Load API key from environment if not provided"""
        if self.openai_api_key is None:
            self.openai_api_key = os.getenv("OPENAI_API_KEY")
            if not self.openai_api_key:
                print("⚠️  WARNING: OPENAI_API_KEY not found in environment")

    @classmethod
    def from_env(cls):
        """Create configuration from environment variables"""
        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            default_model=os.getenv("ONCOCITE_DEFAULT_MODEL", "gpt-4o"),
            verbose=os.getenv("ONCOCITE_VERBOSE", "true").lower() == "true"
        )


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
