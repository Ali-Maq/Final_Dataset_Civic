"""
OncoCITE: 18-Agent Collaborative Architecture for Precision Oncology Knowledge Extraction
Built using OpenAI Agents SDK

Architecture Overview:
- Tier 1 (Agents 1-8): Extraction - Extract core entities from literature
- Tier 2 (Agents 9-14): Normalization - Ground entities to standardized ontologies
- Tier 3 (Agents 15-17): Validation - Cross-field consistency and disambiguation
- Tier 4 (Agent 18): Consolidation - Conflict resolution and reasoning
"""

from agents import Agent, Runner, AgentHooks, RunContextWrapper, Tool, function_tool, ModelSettings, AgentOutputSchema
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pydantic import BaseModel
import json
import asyncio
from datetime import datetime


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class ExtractionContext:
    """Context passed between agents during extraction workflow"""
    literature_text: str
    figures_data: Optional[Dict] = None
    tables_data: Optional[Dict] = None
    supplementary_data: Optional[Dict] = None

    # Tier 1 outputs (Extraction)
    disease_extraction: Optional[Dict] = None
    variant_extraction: Optional[Dict] = None
    therapy_extraction: Optional[Dict] = None
    evidence_extraction: Optional[Dict] = None
    outcomes_extraction: Optional[Dict] = None
    phenotype_extraction: Optional[Dict] = None
    assertion_extraction: Optional[Dict] = None
    provenance_extraction: Optional[Dict] = None

    # Tier 2 outputs (Normalization)
    disease_normalization: Optional[Dict] = None
    variant_normalization: Optional[Dict] = None
    therapy_normalization: Optional[Dict] = None
    trial_normalization: Optional[Dict] = None
    coordinate_normalization: Optional[Dict] = None
    ontology_normalization: Optional[Dict] = None

    # Tier 3 outputs (Validation)
    cross_field_validation: Optional[Dict] = None
    evidence_disambiguation: Optional[Dict] = None
    significance_classification: Optional[Dict] = None

    # Tier 4 output (Consolidation)
    consolidated_result: Optional[Dict] = None

    # Metadata
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    confidence_scores: Dict[str, float] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


class CIViCSchema(BaseModel):
    """124-Field CIViC Schema Output Model"""
    # Evidence Fields (18)
    evidence_id: Optional[str] = None
    evidence_name: Optional[str] = None
    evidence_description: Optional[str] = None
    evidence_level: Optional[str] = None  # A, B, C, D
    evidence_type: Optional[str] = None  # PREDICTIVE, PROGNOSTIC, DIAGNOSTIC, PREDISPOSING, ONCOGENIC, FUNCTIONAL
    evidence_direction: Optional[str] = None  # SUPPORTS, DOES_NOT_SUPPORT
    evidence_rating: Optional[float] = None
    evidence_significance: Optional[str] = None
    evidence_status: Optional[str] = None
    therapy_interaction_type: Optional[str] = None
    variant_origin: Optional[str] = None

    # Disease Fields (18)
    disease_id: Optional[int] = None
    disease_name: Optional[str] = None
    disease_doid: Optional[str] = None
    disease_display_name: Optional[str] = None
    disease_url: Optional[str] = None

    # Variant Fields (24)
    variant_ids: Optional[List[int]] = None
    variant_names: Optional[List[str]] = None
    variant_aliases: Optional[List[str]] = None
    variant_hgvs_descriptions: Optional[List[str]] = None
    variant_clinvar_ids: Optional[List[str]] = None
    variant_coordinates: Optional[Dict] = None

    # Therapy Fields (31)
    therapy_ids: Optional[List[int]] = None
    therapy_names: Optional[List[str]] = None
    therapy_ncit_ids: Optional[List[str]] = None
    therapy_aliases: Optional[List[str]] = None

    # Outcomes Fields (15)
    phenotype_ids: Optional[List[int]] = None
    phenotype_names: Optional[List[str]] = None
    phenotype_hpo_ids: Optional[List[str]] = None

    # Trial Fields (8)
    source_id: Optional[int] = None
    source_type: Optional[str] = None
    citation: Optional[str] = None
    clinical_trial_ids: Optional[List[str]] = None

    # Provenance Fields (6)
    pmid: Optional[str] = None
    confidence_score: Optional[float] = None
    extraction_timestamp: Optional[str] = None

    # Molecular Profile Fields
    molecular_profile_id: Optional[int] = None
    molecular_profile_name: Optional[str] = None
    molecular_profile_score: Optional[float] = None
    molecular_profile_is_complex: Optional[bool] = None


# ============================================================================
# MONITORING HOOKS
# ============================================================================

class OncoCITEHooks(AgentHooks):
    """Hooks for monitoring agent execution and tracking metrics"""

    def __init__(self):
        self.agent_call_counts = {}
        self.tool_call_counts = {}
        self.total_start_time = None
        self.agent_timings = {}

    async def on_start(self, context: RunContextWrapper, agent: Agent):
        timestamp = datetime.now().isoformat()
        agent_name = agent.name

        if agent_name not in self.agent_call_counts:
            self.agent_call_counts[agent_name] = 0
        self.agent_call_counts[agent_name] += 1

        self.agent_timings[agent_name] = datetime.now()
        print(f"[{timestamp}] 🟢 {agent_name} started (call #{self.agent_call_counts[agent_name]})")

    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool):
        tool_name = tool.name
        if tool_name not in self.tool_call_counts:
            self.tool_call_counts[tool_name] = 0
        self.tool_call_counts[tool_name] += 1
        print(f"  🔧 Tool: {tool_name} (call #{self.tool_call_counts[tool_name]})")

    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str):
        print(f"  ✅ Tool {tool.name} completed")

    async def on_end(self, context: RunContextWrapper, agent: Agent, output):
        agent_name = agent.name
        if agent_name in self.agent_timings:
            duration = (datetime.now() - self.agent_timings[agent_name]).total_seconds()
            print(f"[{datetime.now().isoformat()}] 🔴 {agent_name} completed (duration: {duration:.2f}s)")
        else:
            print(f"[{datetime.now().isoformat()}] 🔴 {agent_name} completed")

    def get_summary(self):
        """Get execution summary"""
        return {
            "agent_calls": self.agent_call_counts,
            "tool_calls": self.tool_call_counts,
            "total_agents": len(self.agent_call_counts),
            "total_tools": len(self.tool_call_counts)
        }


# ============================================================================
# TIER 1: EXTRACTION AGENTS (Agents 1-8)
# ============================================================================

def create_tier1_extraction_agents(hooks: Optional[AgentHooks] = None) -> Dict[str, Agent]:
    """
    Create Tier 1 extraction agents that identify core entities from literature
    Agents 1-8: Disease, Variant, Therapy, Evidence, Outcomes, Phenotypes, Assertions, Provenance
    """

    agents = {}

    # Agent 1: Disease Extraction
    agents["disease_extractor"] = Agent(
        name="Agent_1_Disease_Extractor",
        instructions="""You are a specialized agent for extracting disease information from oncology literature.

Your task is to identify and extract:
1. Disease name (primary cancer type)
2. Disease subtypes and stages
3. Histological classifications
4. WHO/ICD classifications
5. Cancer staging information (TNM, FIGO, etc.)

Output format should be JSON with fields:
- disease_name: Primary disease name
- disease_subtype: Specific subtype if mentioned
- disease_stage: Stage information (e.g., "Stage IV", "Metastatic")
- histology: Histological type
- classification_system: WHO, ICD-O, etc.

Be precise and extract only what is explicitly stated in the text.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 2: Variant Extraction
    agents["variant_extractor"] = Agent(
        name="Agent_2_Variant_Extractor",
        instructions="""You are a specialized agent for extracting genetic variant information from oncology literature.

Your task is to identify and extract:
1. Gene names (HUGO symbols)
2. Variant nomenclature (HGVS format when available)
3. Protein changes (p. notation)
4. DNA changes (c. notation)
5. Variant types (SNV, indel, CNV, fusion, etc.)
6. Allele frequencies if mentioned
7. Zygosity information

Output format should be JSON with fields:
- gene_name: HUGO gene symbol
- variant_name: Short variant name (e.g., "V600E")
- hgvs_protein: HGVS protein notation (e.g., "p.Val600Glu")
- hgvs_cdna: HGVS cDNA notation (e.g., "c.1799T>A")
- variant_type: Type of variant
- zygosity: heterozygous/homozygous if stated

Be accurate with molecular nomenclature and follow HGVS standards.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 3: Therapy Extraction
    agents["therapy_extractor"] = Agent(
        name="Agent_3_Therapy_Extractor",
        instructions="""You are a specialized agent for extracting therapy/drug information from oncology literature.

Your task is to identify and extract:
1. Drug names (generic names preferred)
2. Drug combinations
3. Therapy interaction types (combination, substitution, sequential)
4. Dosage and administration routes
5. Treatment lines (first-line, second-line, etc.)
6. Drug classes and mechanisms

Output format should be JSON with fields:
- drug_names: List of drug names
- interaction_type: COMBINATION, SUBSTITUTES, SEQUENTIAL
- treatment_line: e.g., "first-line", "second-line"
- drug_classes: List of drug classes
- dosage_info: Dosage if mentioned

Use current/generic drug names. Avoid trade names unless necessary.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 4: Evidence Extraction
    agents["evidence_extractor"] = Agent(
        name="Agent_4_Evidence_Extractor",
        instructions="""You are a specialized agent for extracting evidence-level information from oncology literature.

Your task is to classify and extract:
1. Evidence level (A: Clinical trials, B: Clinical, C: Case study, D: Preclinical)
2. Evidence type (PREDICTIVE, PROGNOSTIC, DIAGNOSTIC, PREDISPOSING, ONCOGENIC, FUNCTIONAL)
3. Evidence direction (SUPPORTS, DOES_NOT_SUPPORT)
4. Evidence significance (SENSITIVITY, RESISTANCE, POSITIVE, NEGATIVE, etc.)
5. Study design and methodology
6. Patient cohort details (N, demographics)

Output format should be JSON with fields:
- evidence_level: A, B, C, or D
- evidence_type: One of the 6 types
- evidence_direction: SUPPORTS or DOES_NOT_SUPPORT
- significance: Clinical significance
- study_type: e.g., "Phase III trial", "Retrospective study"
- patient_count: Number of patients

Base your classification on published standards (CIViC guidelines).""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 5: Outcomes Extraction
    agents["outcomes_extractor"] = Agent(
        name="Agent_5_Outcomes_Extractor",
        instructions="""You are a specialized agent for extracting clinical outcomes from oncology literature.

Your task is to identify and extract:
1. Response rates (ORR, CR, PR, SD, PD)
2. Survival metrics (OS, PFS, DFS, RFS)
3. Hazard ratios and confidence intervals
4. p-values and statistical significance
5. Response duration
6. Adverse events if relevant

Output format should be JSON with fields:
- response_type: Type of response (ORR, CR, PR, etc.)
- response_rate: Percentage or rate
- survival_metric: OS, PFS, etc.
- median_survival: Median survival time
- hazard_ratio: HR value
- ci_95: Confidence interval
- p_value: Statistical significance

Extract only quantitative outcomes with their statistical measures.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 6: Phenotype Extraction
    agents["phenotype_extractor"] = Agent(
        name="Agent_6_Phenotype_Extractor",
        instructions="""You are a specialized agent for extracting phenotypic information from oncology literature.

Your task is to identify and extract:
1. Associated phenotypes and symptoms
2. Biomarker expressions (IHC, FISH, etc.)
3. Molecular phenotypes
4. Clinical presentations
5. Comorbidities

Output format should be JSON with fields:
- phenotypes: List of observed phenotypes
- biomarker_status: Expression status (positive/negative/amplified)
- clinical_features: Clinical presentations
- associated_conditions: Related conditions

Focus on clinically relevant phenotypic information.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 7: Assertion Extraction
    agents["assertion_extractor"] = Agent(
        name="Agent_7_Assertion_Extractor",
        instructions="""You are a specialized agent for extracting clinical assertions from oncology literature.

Your task is to identify:
1. Author conclusions and clinical assertions
2. Guideline recommendations
3. FDA/regulatory approvals mentioned
4. Clinical actionability statements
5. Strength of recommendations

Output format should be JSON with fields:
- assertion_type: Type of assertion (guideline, regulatory, clinical)
- assertion_text: The actual assertion
- guideline_source: e.g., NCCN, ESMO, FDA
- amp_tier: AMP/ASCO/CAP tier if applicable
- strength: Strong/moderate/weak recommendation

Extract expert consensus and authoritative statements.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 8: Provenance Extraction
    agents["provenance_extractor"] = Agent(
        name="Agent_8_Provenance_Extractor",
        instructions="""You are a specialized agent for extracting source and provenance information.

Your task is to identify and extract:
1. PubMed ID (PMID)
2. DOI
3. Journal name and publication details
4. Authors
5. Publication date
6. Clinical trial IDs (NCT numbers)
7. Exact text spans where information was found

Output format should be JSON with fields:
- pmid: PubMed ID
- doi: Digital Object Identifier
- journal: Journal name
- pub_date: Publication date
- authors: List of authors
- trial_ids: List of NCT or other trial IDs
- text_spans: Relevant quote locations

Ensure accurate attribution and citation information.""",
        model="gpt-4o",
        hooks=hooks
    )

    return agents


# ============================================================================
# TIER 2: NORMALIZATION AGENTS (Agents 9-14)
# ============================================================================

def create_tier2_normalization_agents(hooks: Optional[AgentHooks] = None) -> Dict[str, Agent]:
    """
    Create Tier 2 normalization agents that ground entities to standardized ontologies
    Agents 9-14: DOID/NCIt, HGVS/SO, Drug Ontology, Trial ID, Coordinates, Additional
    """

    agents = {}

    # Agent 9: Disease Normalization (DOID/NCIt)
    agents["disease_normalizer"] = Agent(
        name="Agent_9_Disease_Normalizer_DOID_NCIt",
        instructions="""You are a specialized agent for normalizing disease terms to standardized ontologies.

Your task is to map extracted disease names to:
1. Disease Ontology (DOID) terms
2. NCI Thesaurus (NCIt) codes
3. ICD-O-3 codes
4. SNOMED CT codes

Process:
- Take the extracted disease name
- Find the most specific matching ontology term
- Provide the ontology ID and canonical name
- Handle synonyms and alternative names

Output format should be JSON with fields:
- original_term: Input disease name
- doid: Disease Ontology ID (e.g., "DOID:1324")
- doid_name: Canonical DOID name
- ncit_code: NCIt code (e.g., "C3058")
- ncit_name: NCIt preferred name
- confidence: Confidence in mapping (0-1)

Use exact matching when possible, fuzzy matching when necessary.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 10: Variant Normalization (HGVS/SO)
    agents["variant_normalizer"] = Agent(
        name="Agent_10_Variant_Normalizer_HGVS_SO",
        instructions="""You are a specialized agent for normalizing genetic variants to standard nomenclatures.

Your task is to normalize variants to:
1. HGVS nomenclature (genomic, coding, protein)
2. Sequence Ontology (SO) terms
3. dbSNP IDs (rs numbers)
4. ClinVar IDs
5. Genomic coordinates (hg38, hg19)

Process:
- Take extracted variant information
- Convert to proper HGVS format
- Assign SO term for variant type
- Cross-reference with databases

Output format should be JSON with fields:
- original_variant: Input variant name
- hgvs_genomic: g. notation
- hgvs_coding: c. notation
- hgvs_protein: p. notation
- so_term: Sequence Ontology term
- so_id: SO identifier
- dbsnp_id: rs number if available
- clinvar_id: ClinVar accession

Follow HGVS guidelines strictly (v20.05 or later).""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 11: Therapy Normalization (Drug Ontology)
    agents["therapy_normalizer"] = Agent(
        name="Agent_11_Therapy_Normalizer_DrugOnt",
        instructions="""You are a specialized agent for normalizing drug/therapy names to standardized vocabularies.

Your task is to map drug names to:
1. NCI Thesaurus drug codes (NCIt)
2. RxNorm codes
3. DrugBank IDs
4. ATC codes
5. PubChem CIDs

Process:
- Take extracted drug names
- Normalize to generic names
- Find ontology mappings
- Resolve synonyms and brand names

Output format should be JSON with fields:
- original_drug: Input drug name
- generic_name: Standardized generic name
- ncit_code: NCIt drug code
- rxnorm_code: RxNorm concept ID
- drugbank_id: DrugBank identifier
- atc_code: ATC classification
- drug_class: Pharmacological class

Prefer generic names over brand names.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 12: Trial ID Normalization
    agents["trial_normalizer"] = Agent(
        name="Agent_12_Trial_ID_Normalizer",
        instructions="""You are a specialized agent for normalizing clinical trial identifiers.

Your task is to validate and normalize:
1. ClinicalTrials.gov NCT numbers
2. EudraCT numbers
3. Trial names and acronyms
4. Trial phase information
5. Trial status

Process:
- Extract trial identifiers
- Validate format (NCT########)
- Link to trial registry
- Extract trial metadata

Output format should be JSON with fields:
- original_id: Input trial identifier
- nct_number: Validated NCT number
- trial_name: Official trial name
- trial_acronym: Short name/acronym
- phase: Trial phase (I, II, III, IV)
- status: Active, Completed, etc.
- registry_url: Link to trial registry

Validate NCT format: NCT followed by 8 digits.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 13: Coordinate Normalization
    agents["coordinate_normalizer"] = Agent(
        name="Agent_13_Coordinate_Normalizer",
        instructions="""You are a specialized agent for normalizing genomic coordinates.

Your task is to process and normalize:
1. Genomic coordinates (chr, start, end, ref, alt)
2. Genome build versions (hg19, hg38, GRCh37, GRCh38)
3. Transcript IDs (RefSeq, Ensembl)
4. Exon/intron numbers
5. Coordinate liftover if needed

Process:
- Parse coordinate information
- Standardize to hg38 (primary)
- Provide hg19 for compatibility
- Validate chromosome names
- Cross-reference transcripts

Output format should be JSON with fields:
- chromosome: Chromosome (1-22, X, Y, MT)
- start: Start position (1-based)
- end: End position
- reference_allele: Ref nucleotide
- alternate_allele: Alt nucleotide
- genome_build: hg38 or hg19
- transcript_id: RefSeq or Ensembl ID
- strand: + or -

Use 1-based coordinates following VCF standards.""",
        model="gpt-4o",
        hooks=hooks
    )

    # Agent 14: Additional Ontology Normalization
    agents["ontology_normalizer"] = Agent(
        name="Agent_14_Additional_Ontology_Normalizer",
        instructions="""You are a specialized agent for additional ontology mappings and cross-references.

Your task is to provide additional normalizations:
1. Gene Ontology (GO) terms for functional information
2. Human Phenotype Ontology (HPO) for phenotypes
3. MONDO disease ontology mappings
4. Pathway databases (KEGG, Reactome)
5. Protein databases (UniProt)

Process:
- Take extracted entities
- Map to relevant ontologies
- Provide cross-references
- Link to pathway information

Output format should be JSON with fields:
- entity_type: gene, phenotype, disease, pathway
- entity_name: Original entity
- go_terms: List of relevant GO terms
- hpo_ids: HPO identifiers for phenotypes
- mondo_id: MONDO disease ID
- pathway_ids: KEGG/Reactome IDs
- uniprot_id: UniProt accession

Provide comprehensive ontology coverage.""",
        model="gpt-4o",
        hooks=hooks
    )

    return agents


# ============================================================================
# TIER 3: VALIDATION AGENTS (Agents 15-17)
# ============================================================================

def create_tier3_validation_agents(hooks: Optional[AgentHooks] = None) -> Dict[str, Agent]:
    """
    Create Tier 3 validation agents for quality assurance and disambiguation
    Agents 15-17: Cross-field validation, Evidence disambiguation, Significance classification
    """

    agents = {}

    # Agent 15: Cross-field Consistency Validator
    agents["cross_field_validator"] = Agent(
        name="Agent_15_CrossField_Consistency_Validator",
        instructions="""You are a specialized agent for validating consistency across extracted fields.

Your task is to check for:
1. Disease-therapy compatibility
2. Variant-disease associations
3. Evidence type vs. significance alignment
4. HGVS vs. coordinate consistency
5. Therapy interaction logic
6. Temporal consistency (dates, phases)

Validation checks:
- Does the therapy make sense for this disease?
- Is the variant associated with the stated disease?
- Does evidence direction match significance?
- Do HGVS and coordinates refer to same variant?
- Are drug interactions logically valid?
- Are trial phases and dates consistent?

Output format should be JSON with fields:
- validation_passed: true/false
- consistency_checks: Dict of check results
- conflicts_detected: List of conflicts
- warnings: List of warnings
- suggestions: Recommended fixes

Flag any inconsistencies for human review.""",
        model="gpt-4o",
        hooks=hooks,
        model_settings=ModelSettings(temperature=0.3)  # Lower temperature for validation
    )

    # Agent 16: Evidence Disambiguator
    agents["evidence_disambiguator"] = Agent(
        name="Agent_16_Evidence_Disambiguator",
        instructions="""You are a specialized agent for disambiguating ambiguous evidence statements.

Your task is to resolve ambiguities in:
1. Multiple possible interpretations
2. Contradictory statements within text
3. Unclear pronoun references
4. Ambiguous variant names
5. Multiple diseases mentioned
6. Unclear therapy combinations

Disambiguation strategies:
- Use context clues from surrounding text
- Prioritize main findings over background
- Resolve pronouns to specific entities
- Disambiguate variant names using gene context
- Separate primary disease from metastases
- Parse complex therapy regimens

Output format should be JSON with fields:
- ambiguity_type: Type of ambiguity detected
- original_text: Ambiguous statement
- possible_interpretations: List of interpretations
- selected_interpretation: Chosen interpretation
- confidence: Confidence in disambiguation (0-1)
- reasoning: Explanation of choice

When uncertain, flag for human curation.""",
        model="gpt-4o",
        hooks=hooks,
        model_settings=ModelSettings(temperature=0.2)
    )

    # Agent 17: Significance Classifier
    agents["significance_classifier"] = Agent(
        name="Agent_17_Significance_Classifier",
        instructions="""You are a specialized agent for classifying clinical significance of evidence.

Your task is to determine:
1. Clinical actionability (AMP/ASCO/CAP tiers)
2. Evidence strength (strong, moderate, weak)
3. Variant pathogenicity (for predisposing variants)
4. Variant oncogenicity (for somatic variants)
5. FDA approval status implications
6. Guideline recommendation strength

Classification frameworks:
- AMP/ASCO/CAP tiers (I, II, III, IV)
- ACMG/AMP pathogenicity (Pathogenic, Likely Pathogenic, VUS, Likely Benign, Benign)
- ClinGen Oncogenicity (Oncogenic, Likely Oncogenic, VUS, Likely Benign, Benign)
- Evidence levels (A, B, C, D)

Output format should be JSON with fields:
- amp_tier: AMP/ASCO/CAP tier
- acmg_classification: ACMG pathogenicity (if germline)
- oncogenicity_class: ClinGen oncogenicity (if somatic)
- evidence_strength: Strong/Moderate/Weak
- actionability: Tier I, II, III, or IV
- fda_status: Approved/Investigational/Off-label
- guideline_support: Guideline references

Follow published standards (AMP/ASCO/CAP 2017, ACMG/AMP 2015, ClinGen SVI).""",
        model="gpt-4o",
        hooks=hooks,
        model_settings=ModelSettings(temperature=0.2)
    )

    return agents


# ============================================================================
# TIER 4: CONSOLIDATION AGENT (Agent 18)
# ============================================================================

def create_tier4_consolidation_agent(hooks: Optional[AgentHooks] = None) -> Agent:
    """
    Create Tier 4 consolidation agent for final conflict resolution
    Agent 18: Conflict Resolution & Reasoning
    """

    return Agent(
        name="Agent_18_Consolidation_ConflictResolution",
        instructions="""You are the master consolidation agent responsible for final conflict resolution and reasoning.

Your responsibilities:
1. Resolve conflicts between agent outputs
2. Apply confidence-weighted voting
3. Generate reasoning chains explaining decisions
4. Produce final structured output (124-field schema)
5. Assign final confidence scores
6. Document all conflicts and resolutions

Conflict resolution strategies:
- Weighted voting based on agent confidence scores
- Source reliability assessment (journal impact, study design)
- Temporal precedence (newer data preferred when contradictory)
- Expert consensus (multiple agents agreeing)
- Ontological constraints (disease-drug compatibility)

Reasoning chain generation:
- Document decision process step-by-step
- Explain why certain interpretations were chosen
- Note alternative interpretations considered
- Justify confidence scores
- Highlight areas of uncertainty

Final output requirements:
- Complete 124-field CIViC schema
- Confidence score for each field (0-1)
- Reasoning chain for key decisions
- List of unresolved ambiguities
- Quality metrics (completeness %, validation status)

Your output is the authoritative final result that will be used for clinical decision support.
Apply rigorous quality standards and flag anything that needs human expert review.""",
        model="gpt-4o",  # Use most capable model for final consolidation
        output_type=AgentOutputSchema(CIViCSchema, strict_json_schema=False),  # Structured output with relaxed schema
        hooks=hooks,
        model_settings=ModelSettings(
            temperature=0.1,  # Very low temperature for consistency
            max_tokens=4000   # Allow detailed reasoning
        )
    )


# ============================================================================
# AGENT ORCHESTRATION
# ============================================================================

class OncoCITEOrchestrator:
    """
    Orchestrates the 18-agent pipeline for literature extraction
    """

    def __init__(self, use_parallel: bool = True, verbose: bool = True):
        self.use_parallel = use_parallel
        self.verbose = verbose
        self.hooks = OncoCITEHooks() if verbose else None

        # Initialize all agents
        self.tier1_agents = create_tier1_extraction_agents(self.hooks)
        self.tier2_agents = create_tier2_normalization_agents(self.hooks)
        self.tier3_agents = create_tier3_validation_agents(self.hooks)
        self.tier4_agent = create_tier4_consolidation_agent(self.hooks)

        print(f"✅ Initialized OncoCITE with 18 agents")
        print(f"   - Tier 1 (Extraction): {len(self.tier1_agents)} agents")
        print(f"   - Tier 2 (Normalization): {len(self.tier2_agents)} agents")
        print(f"   - Tier 3 (Validation): {len(self.tier3_agents)} agents")
        print(f"   - Tier 4 (Consolidation): 1 agent")

    async def run_tier1_extraction(self, context: ExtractionContext) -> ExtractionContext:
        """Run Tier 1 extraction agents in parallel"""
        if self.verbose:
            print("\n" + "="*80)
            print("TIER 1: EXTRACTION")
            print("="*80)

        # Run all tier 1 agents
        tasks = {}
        tasks['disease'] = Runner.run(
            self.tier1_agents['disease_extractor'],
            f"Extract disease information from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['variant'] = Runner.run(
            self.tier1_agents['variant_extractor'],
            f"Extract variant information from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['therapy'] = Runner.run(
            self.tier1_agents['therapy_extractor'],
            f"Extract therapy information from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['evidence'] = Runner.run(
            self.tier1_agents['evidence_extractor'],
            f"Extract evidence information from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['outcomes'] = Runner.run(
            self.tier1_agents['outcomes_extractor'],
            f"Extract clinical outcomes from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['phenotype'] = Runner.run(
            self.tier1_agents['phenotype_extractor'],
            f"Extract phenotype information from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['assertion'] = Runner.run(
            self.tier1_agents['assertion_extractor'],
            f"Extract clinical assertions from this text:\n\n{context.literature_text[:2000]}"
        )
        tasks['provenance'] = Runner.run(
            self.tier1_agents['provenance_extractor'],
            f"Extract provenance information from this text:\n\n{context.literature_text[:2000]}"
        )

        # Wait for all results
        results = {}
        for key, task in tasks.items():
            result = await task
            results[key] = result.final_output

        # Update context
        context.disease_extraction = {"raw": str(results['disease'])}
        context.variant_extraction = {"raw": str(results['variant'])}
        context.therapy_extraction = {"raw": str(results['therapy'])}
        context.evidence_extraction = {"raw": str(results['evidence'])}
        context.outcomes_extraction = {"raw": str(results['outcomes'])}
        context.phenotype_extraction = {"raw": str(results['phenotype'])}
        context.assertion_extraction = {"raw": str(results['assertion'])}
        context.provenance_extraction = {"raw": str(results['provenance'])}

        return context

    async def run_tier2_normalization(self, context: ExtractionContext) -> ExtractionContext:
        """Run Tier 2 normalization agents"""
        if self.verbose:
            print("\n" + "="*80)
            print("TIER 2: NORMALIZATION")
            print("="*80)

        # Run normalization agents
        tasks = {}
        tasks['disease_norm'] = Runner.run(
            self.tier2_agents['disease_normalizer'],
            f"Normalize this disease information to DOID/NCIt:\n{json.dumps(context.disease_extraction, indent=2)}"
        )
        tasks['variant_norm'] = Runner.run(
            self.tier2_agents['variant_normalizer'],
            f"Normalize this variant information to HGVS/SO:\n{json.dumps(context.variant_extraction, indent=2)}"
        )
        tasks['therapy_norm'] = Runner.run(
            self.tier2_agents['therapy_normalizer'],
            f"Normalize this therapy information:\n{json.dumps(context.therapy_extraction, indent=2)}"
        )
        tasks['trial_norm'] = Runner.run(
            self.tier2_agents['trial_normalizer'],
            f"Normalize trial identifiers:\n{json.dumps(context.provenance_extraction, indent=2)}"
        )

        # Wait for results
        results = {}
        for key, task in tasks.items():
            result = await task
            results[key] = result.final_output

        # Update context
        context.disease_normalization = {"raw": str(results['disease_norm'])}
        context.variant_normalization = {"raw": str(results['variant_norm'])}
        context.therapy_normalization = {"raw": str(results['therapy_norm'])}
        context.trial_normalization = {"raw": str(results['trial_norm'])}

        return context

    async def run_tier3_validation(self, context: ExtractionContext) -> ExtractionContext:
        """Run Tier 3 validation agents"""
        if self.verbose:
            print("\n" + "="*80)
            print("TIER 3: VALIDATION")
            print("="*80)

        # Prepare validation input
        validation_input = {
            "extraction": {
                "disease": context.disease_extraction,
                "variant": context.variant_extraction,
                "therapy": context.therapy_extraction,
                "evidence": context.evidence_extraction,
                "outcomes": context.outcomes_extraction
            },
            "normalization": {
                "disease": context.disease_normalization,
                "variant": context.variant_normalization,
                "therapy": context.therapy_normalization
            }
        }

        # Run validation agents
        cross_field_result = await Runner.run(
            self.tier3_agents['cross_field_validator'],
            f"Validate cross-field consistency:\n{json.dumps(validation_input, indent=2)}"
        )

        evidence_disambig_result = await Runner.run(
            self.tier3_agents['evidence_disambiguator'],
            f"Disambiguate evidence:\n{json.dumps(context.evidence_extraction, indent=2)}"
        )

        significance_result = await Runner.run(
            self.tier3_agents['significance_classifier'],
            f"Classify clinical significance:\n{json.dumps(validation_input, indent=2)}"
        )

        # Update context
        context.cross_field_validation = {"raw": str(cross_field_result.final_output)}
        context.evidence_disambiguation = {"raw": str(evidence_disambig_result.final_output)}
        context.significance_classification = {"raw": str(significance_result.final_output)}

        return context

    async def run_tier4_consolidation(self, context: ExtractionContext) -> CIViCSchema:
        """Run Tier 4 consolidation agent for final output"""
        if self.verbose:
            print("\n" + "="*80)
            print("TIER 4: CONSOLIDATION")
            print("="*80)

        # Prepare comprehensive input for consolidation
        consolidation_input = {
            "tier1_extraction": {
                "disease": context.disease_extraction,
                "variant": context.variant_extraction,
                "therapy": context.therapy_extraction,
                "evidence": context.evidence_extraction,
                "outcomes": context.outcomes_extraction,
                "phenotype": context.phenotype_extraction,
                "assertion": context.assertion_extraction,
                "provenance": context.provenance_extraction
            },
            "tier2_normalization": {
                "disease": context.disease_normalization,
                "variant": context.variant_normalization,
                "therapy": context.therapy_normalization,
                "trial": context.trial_normalization
            },
            "tier3_validation": {
                "cross_field": context.cross_field_validation,
                "disambiguation": context.evidence_disambiguation,
                "significance": context.significance_classification
            },
            "original_text": context.literature_text[:1000]
        }

        # Run consolidation agent
        result = await Runner.run(
            self.tier4_agent,
            f"""Consolidate all agent outputs into final 124-field CIViC schema.

Resolve any conflicts using confidence-weighted voting.
Generate reasoning chains for key decisions.
Produce complete structured output.

Agent outputs:
{json.dumps(consolidation_input, indent=2)}
"""
        )

        # The result.final_output should be a CIViCSchema object
        return result.final_output

    async def process_literature(self, literature_text: str) -> CIViCSchema:
        """
        Main entry point: Process literature through all 4 tiers
        """
        start_time = datetime.now()

        if self.verbose:
            print("\n" + "="*80)
            print("🚀 STARTING ONCOCITE 18-AGENT PIPELINE")
            print("="*80)
            print(f"Input text length: {len(literature_text)} characters")
            print(f"Timestamp: {start_time.isoformat()}")

        # Initialize context
        context = ExtractionContext(literature_text=literature_text)

        try:
            # Run pipeline
            context = await self.run_tier1_extraction(context)
            context = await self.run_tier2_normalization(context)
            context = await self.run_tier3_validation(context)
            final_output = await self.run_tier4_consolidation(context)

            # Calculate duration
            duration = (datetime.now() - start_time).total_seconds()

            if self.verbose:
                print("\n" + "="*80)
                print("✅ PIPELINE COMPLETED SUCCESSFULLY")
                print("="*80)
                print(f"Total duration: {duration:.2f} seconds")

                if self.hooks:
                    summary = self.hooks.get_summary()
                    print(f"\nExecution Summary:")
                    print(f"  - Total agents called: {summary['total_agents']}")
                    print(f"  - Total tool calls: {summary['total_tools']}")

            return final_output

        except Exception as e:
            print(f"\n❌ Error in pipeline: {str(e)}")
            raise


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

async def main():
    """Example usage of OncoCITE system"""

    # Sample literature text (simulated)
    sample_text = """
    BACKGROUND: EGFR T790M is a common resistance mutation in non-small cell lung cancer (NSCLC).

    METHODS: We conducted a phase III clinical trial (NCT02296125) with 419 patients with advanced
    NSCLC harboring the EGFR T790M mutation. Patients were randomized to receive osimertinib (80 mg
    daily) or platinum-pemetrexed chemotherapy.

    RESULTS: The median progression-free survival (PFS) was 10.1 months (95% CI: 8.3-12.3) in the
    osimertinib group versus 4.4 months (95% CI: 4.2-5.6) in the chemotherapy group (HR 0.30,
    p<0.001). Overall response rate (ORR) was 71% vs 31% (p<0.001). Common adverse events in the
    osimertinib group included diarrhea (42%) and rash (34%).

    CONCLUSIONS: Osimertinib demonstrates superior efficacy compared to chemotherapy in EGFR T790M
    positive NSCLC patients, confirming its role as a standard of care for this patient population.
    """

    # Initialize orchestrator
    orchestrator = OncoCITEOrchestrator(verbose=True)

    # Process literature
    result = await orchestrator.process_literature(sample_text)

    # Display results
    print("\n" + "="*80)
    print("FINAL STRUCTURED OUTPUT (124-FIELD CIVIC SCHEMA)")
    print("="*80)
    print(json.dumps(result.model_dump(), indent=2))


if __name__ == "__main__":
    # Note: This requires OPENAI_API_KEY to be set in environment
    print("OncoCITE 18-Agent System - OpenAI Agents SDK Implementation")
    print("To run: asyncio.run(main())")
    print("\nIMPORTANT: Ensure OPENAI_API_KEY is set in your environment")
