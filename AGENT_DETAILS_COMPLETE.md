# OncoCITE: Complete Agent Details with Reasoning Traces & Deep Research

**Version**: 2.0 - Enriched with Reasoning Capture & Detailed Output Schemas
**Last Updated**: 2025-11-10
**Purpose**: Comprehensive specification of all 18 agents with reasoning traces, detailed output schemas from CIViC data dictionary, and deep research examples

---

## Architecture Overview: 18 Agents in 4 Tiers

```
Literature Text Input
         ↓
    TIER 1 (8 Agents) - EXTRACTION (Temperature: 0.7)
    [Parallel Execution with Reasoning Traces]
         ↓
    TIER 2 (6 Agents) - NORMALIZATION (Temperature: 0.5)
    [Sequential/Parallel with Local Database Queries]
         ↓
    TIER 3 (3 Agents) - VALIDATION (Temperature: 0.3)
    [Parallel Cross-Field Validation]
         ↓
    TIER 4 (1 Agent)  - CONSOLIDATION (Temperature: 0.1)
    [Final 124-Field Assembly with Conflict Resolution]
         ↓
   124-Field CIViC Output
```

### Key Innovation: Reasoning Trace Capture

Every agent captures:
1. **Input Analysis** - What the agent sees and understands
2. **Processing Steps** - Multi-step reasoning with research
3. **Evidence Evaluation** - How decisions are made
4. **Confidence Scoring** - Why confidence levels are assigned
5. **Output Justification** - Rationale for each extracted field

---

## TIER 1: EXTRACTION AGENTS (Temperature: 0.7)

**Purpose**: Extract different dimensions of evidence from literature in parallel with full reasoning traces

---

### Agent 1: Disease Extractor

**Role**: Extract comprehensive disease context from literature with deep clinical knowledge

#### Input Schema
```json
{
  "literature_text": "string - Full text or abstract from publication",
  "figures_data": "optional - Extracted table/figure data",
  "supplementary_data": "optional - Supplementary materials"
}
```

#### Reasoning Trace Example

**Input Literature**:
```
"In patients with NPM1-mutant acute myeloid leukemia (AML),
the presence of this mutation was associated with superior
event-free survival and overall survival in the context of
intensive induction therapy including cytarabine and
anthracycline-based regimens. The 5-year OS was 58% for
NPM1-mutant versus 37% for NPM1 wild-type (p<0.001)."
```

**Agent 1 Reasoning Process**:

```yaml
STEP 1 - Initial Text Analysis:
  thinking: |
    I need to identify the primary disease mentioned. I see "acute myeloid
    leukemia (AML)" which is the main disease context. Let me extract all
    disease-related information.

  identified_terms:
    - "NPM1-mutant acute myeloid leukemia"
    - "AML" (abbreviation)

  reasoning: |
    "NPM1-mutant" is a molecular subtype, not a distinct disease. The primary
    disease is "acute myeloid leukemia". I should separate the disease from
    the molecular profile descriptor.

STEP 2 - Disease Classification Research:
  thinking: |
    Let me recall what I know about AML classification:
    - AML is a WHO-classified hematologic malignancy
    - NPM1 mutations define a genetic subgroup in WHO classification
    - AML has prognostic risk groups: favorable, intermediate, adverse
    - NPM1-mutant AML typically falls in favorable-risk category

  research_depth: |
    - WHO Classification: AML is ICD-O code 9861/3
    - NPM1-mutant AML is recognized as distinct entity in WHO 2016 revision
    - Disease stage: Not applicable for AML (uses risk stratification instead)
    - Treatment context: "intensive induction therapy" suggests fit patients

STEP 3 - Subtype & Stage Extraction:
  thinking: |
    The text specifies "NPM1-mutant" AML, which is a genetic subtype.
    The mention of "intensive induction therapy" suggests newly diagnosed,
    treatment-naive AML (not relapsed/refractory).

  disease_stage_reasoning: |
    AML doesn't use TNM staging. The appropriate context is:
    - Disease status: Newly diagnosed (inferred from "induction therapy")
    - Risk group: Favorable-risk (NPM1-mutant typically)
    - Treatment fitness: Fit for intensive therapy

STEP 4 - Confidence Scoring:
  disease_name_confidence: 1.0
  reasoning: "Explicitly stated as 'acute myeloid leukemia'"

  disease_subtype_confidence: 0.95
  reasoning: |
    NPM1-mutant is clearly stated, but this is molecular subtype,
    not histological subtype. High confidence but noting this distinction.

  disease_stage_confidence: 0.8
  reasoning: |
    Inferred from treatment context (induction therapy), not explicitly
    stated. Could be newly diagnosed or early relapse.
```

#### Output Schema (Enriched with Data Dictionary Fields)

```json
{
  "disease_extraction": {
    "disease_name": {
      "value": "Acute Myeloid Leukemia",
      "field_description": "Primary disease name as would map to CIViC disease_name (Field #59 in data dictionary). This is the core disease context required for all evidence items. Clinical relevance: Enables disease-specific evidence filtering and guides treatment recommendations.",
      "data_type": "string",
      "civic_field": "disease_name",
      "confidence": 1.0,
      "source": "explicitly stated in literature",
      "reasoning": "Directly extracted from 'acute myeloid leukemia (AML)' in text"
    },

    "disease_subtype": {
      "value": "NPM1-mutant AML",
      "field_description": "Molecular or histological subtype. In CIViC, this context is typically captured in molecular_profile_name rather than disease fields. NPM1 mutation status defines a WHO-recognized genetic subgroup with prognostic significance.",
      "data_type": "string",
      "civic_field": "molecular_profile_name (indirectly)",
      "confidence": 0.95,
      "source": "explicitly stated as 'NPM1-mutant'",
      "reasoning": "NPM1 mutation is a molecular classifier, not histological subtype. This information should be associated with molecular profile rather than disease entity."
    },

    "disease_doid": {
      "value": null,
      "field_description": "Disease Ontology ID (Field #61). Will be filled by Agent 9 (Disease Normalizer) by querying local DOID database. Expected: DOID:9119 for Acute Myeloid Leukemia.",
      "data_type": "string",
      "civic_field": "disease_doid",
      "confidence": null,
      "source": "pending normalization in Tier 2",
      "reasoning": "DOID mapping requires ontology database lookup - will be performed by specialized normalization agent"
    },

    "disease_stage": {
      "value": "Newly diagnosed, fit for intensive therapy",
      "field_description": "Disease stage or status context. For AML, this captures treatment phase and fitness status rather than anatomical stage (no TNM for leukemia). Clinical relevance: Determines treatment intensity and prognosis.",
      "data_type": "string",
      "civic_field": "evidence_description (contextual)",
      "confidence": 0.8,
      "source": "inferred from 'intensive induction therapy' mention",
      "reasoning": "'Induction therapy' strongly suggests newly diagnosed AML in fit patients. Intensive regimens not given to relapsed/refractory or unfit patients."
    },

    "treatment_context": {
      "value": "intensive induction therapy (cytarabine + anthracycline)",
      "field_description": "Treatment setting in which disease-variant association was studied. Critical for Predictive evidence type. This will inform therapy_names field (Field #106-108).",
      "data_type": "string",
      "civic_field": "therapy_names, evidence_description",
      "confidence": 0.95,
      "source": "explicitly stated",
      "reasoning": "Specific regimen mentioned provides crucial context for interpreting prognostic association"
    },

    "who_classification": {
      "value": "AML with mutated NPM1",
      "field_description": "WHO classification category. Provides standardized disease taxonomy. NPM1-mutant AML recognized as provisional entity in WHO 2016, formal entity in WHO 2022 classification.",
      "data_type": "string",
      "civic_field": "evidence_description (contextual)",
      "confidence": 0.9,
      "source": "inferred from WHO classification knowledge",
      "reasoning": "NPM1-mutant AML is a recognized WHO entity as of 2016 revision"
    }
  },

  "reasoning_trace": {
    "extraction_steps": 4,
    "research_queries_performed": [
      "WHO AML classification",
      "NPM1-mutant AML prognosis",
      "AML staging systems",
      "Intensive induction therapy definition"
    ],
    "total_confidence": 0.92,
    "reasoning_summary": "High confidence disease extraction. Primary disease (AML) explicitly stated. Molecular subtype (NPM1-mutant) clearly indicated. Disease stage inferred from treatment context with moderate confidence. All fields align with CIViC schema requirements.",
    "potential_issues": [
      "Disease stage is inferred rather than explicit",
      "NPM1 mutation status should be captured in molecular_profile, not disease_subtype"
    ],
    "recommendations": [
      "Verify DOID mapping in normalization step",
      "Ensure molecular profile captures NPM1 mutation",
      "Confirm treatment context in therapy extraction"
    ]
  }
}
```

---

### Agent 2: Variant Extractor

**Role**: Extract comprehensive genetic variant information with HGVS nomenclature validation

#### Input Schema
```json
{
  "literature_text": "string - Full text with variant mentions",
  "figures_data": "optional - Variant tables/figures",
  "variant_databases": "optional - External variant validation"
}
```

#### Reasoning Trace Example

**Input Literature**:
```
"EGFR L858R mutations in exon 21 (c.2573T>G, p.Leu858Arg) were
detected in 45% of NSCLC patients. This missense variant results
in constitutive kinase activation. Genomic coordinates:
chr7:55249071 (GRCh37). ClinVar ID: 16609."
```

**Agent 2 Reasoning Process**:

```yaml
STEP 1 - Variant Mention Detection:
  thinking: |
    I see multiple variant representations:
    - "L858R" (protein shorthand)
    - "c.2573T>G" (cDNA HGVS)
    - "p.Leu858Arg" (protein HGVS)
    - "chr7:55249071" (genomic coordinates)
    These all refer to the same variant. I need to extract and validate each.

  identified_representations:
    - gene: "EGFR"
    - protein_short: "L858R"
    - cdna_hgvs: "c.2573T>G"
    - protein_hgvs: "p.Leu858Arg"
    - genomic: "chr7:55249071"

STEP 2 - HGVS Validation & Research:
  thinking: |
    Let me validate the HGVS nomenclature:
    - "p.Leu858Arg" - Correct 3-letter amino acid format
    - "c.2573T>G" - Correct cDNA format (c. prefix, position, ref>alt)
    - Need to determine reference transcript

  research: |
    EGFR canonical transcript: NM_005228.4 (RefSeq)
    HGVS should include transcript: NM_005228.4:c.2573T>G

    Variant type determination:
    - c.2573T>G = single nucleotide change
    - p.Leu858Arg = amino acid substitution
    - Classification: Missense variant (non-synonymous)

    Exon validation:
    - "exon 21" stated
    - EGFR has 28 exons; exon 21 is in kinase domain
    - L858R is canonical exon 21 hotspot mutation ✓

STEP 3 - Variant Type & Functional Classification:
  thinking: |
    The text states "missense variant" and "constitutive kinase activation"

  variant_type_research: |
    - Missense: Single amino acid substitution ✓
    - Sequence Ontology: SO:0001583 (missense_variant)
    - Not a frameshift, nonsense, or indel

  functional_impact_research: |
    - "constitutive kinase activation" = Gain of Function
    - EGFR L858R literature: Well-established activating mutation
    - Mechanism: Stabilizes active kinase conformation
    - Oncogenic classification: Oncogenic (TIER I)

STEP 4 - Coordinate & Database ID Validation:
  thinking: |
    Coordinates given: chr7:55249071 (GRCh37)
    ClinVar ID: 16609

  validation: |
    - GRCh37 (hg19) is standard reference build ✓
    - Need to confirm 1-based vs 0-based coordinate system
    - Text uses "chr7" format (typical for UCSC)
    - Should be normalized to "7" (no chr prefix) per CIViC standards

  clinvar_lookup: |
    ClinVar:16609 corresponds to EGFR L858R
    This will be validated by Agent 10 (Variant Normalizer) using local ClinVar database

STEP 5 - Allele Frequency & Zygosity:
  thinking: |
    Text states "detected in 45% of NSCLC patients"
    This is population frequency, not allele frequency

  interpretation: |
    - 45% = proportion of patients with mutation (not VAF)
    - No zygosity information provided (heterozygous assumed for somatic)
    - No variant allele fraction (VAF) mentioned
    - Somatic origin inferred from NSCLC context

STEP 6 - Confidence Scoring:
  gene_name_confidence: 1.0  # Explicitly stated
  variant_name_confidence: 1.0  # Multiple confirmatory representations
  hgvs_confidence: 0.95  # Complete HGVS provided, transcript inferred
  coordinates_confidence: 0.9  # Provided but needs normalization
  variant_type_confidence: 1.0  # Explicitly stated as missense
  functional_impact_confidence: 0.9  # Stated but from literature context
```

#### Output Schema (Enriched with Data Dictionary Fields)

```json
{
  "variant_extraction": {
    "gene_name": {
      "value": "EGFR",
      "field_description": "HGNC gene symbol (Field #36: feature_names in CIViC). Gene symbols must follow HGNC nomenclature. Clinical relevance: Primary identifier for gene-based queries and variant grouping.",
      "data_type": "string",
      "civic_field": "feature_names",
      "hgnc_id": "HGNC:3236",
      "entrez_id": "1956",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Gene symbol 'EGFR' clearly stated. HGNC-approved symbol confirmed."
    },

    "variant_name": {
      "value": "L858R",
      "field_description": "Short variant name (Field #25: variant_names). Standardized protein nomenclature using 1-letter amino acid code. This is the primary display name in CIViC UI. Clinical relevance: Enables rapid variant identification and clinical communication.",
      "data_type": "string",
      "civic_field": "variant_names",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Canonical short form 'L858R' stated. Matches standard EGFR exon 21 hotspot nomenclature."
    },

    "hgvs_protein": {
      "value": "p.Leu858Arg",
      "field_description": "HGVS protein notation (Field #28: variant_hgvs_descriptions). Uses 3-letter amino acid codes with 'p.' prefix following HGVS nomenclature standards. Clinical relevance: Unambiguous variant specification for clinical reporting and database queries.",
      "data_type": "string",
      "civic_field": "variant_hgvs_descriptions",
      "hgvs_standard": "HGVS v20.05",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Complete HGVS protein notation provided: p.Leu858Arg. Validates to EGFR canonical mutation."
    },

    "hgvs_cdna": {
      "value": "NM_005228.4:c.2573T>G",
      "field_description": "HGVS cDNA notation (Field #28: variant_hgvs_descriptions). Includes RefSeq transcript ID and cDNA position. Clinical relevance: Enables precise variant mapping for NGS analysis and variant calling pipelines.",
      "data_type": "string",
      "civic_field": "variant_hgvs_descriptions",
      "transcript": "NM_005228.4",
      "confidence": 0.95,
      "source": "transcript inferred, position stated",
      "reasoning": "cDNA change c.2573T>G explicitly provided. Transcript NM_005228.4 is canonical EGFR RefSeq transcript (inferred from standard practice)."
    },

    "variant_type": {
      "value": "missense_variant",
      "field_description": "Sequence Ontology variant type (Field #29: variant_types). Controlled vocabulary from SO ontology. Will be mapped to SO:0001583 by Agent 14 (Ontology Normalizer). Clinical relevance: Categorizes functional impact class (missense vs nonsense vs frameshift).",
      "data_type": "string",
      "civic_field": "variant_types",
      "sequence_ontology_id": "SO:0001583",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Text explicitly states 'missense variant'. Single amino acid substitution confirmed by HGVS notation."
    },

    "variant_origin": {
      "value": "Somatic",
      "field_description": "Variant origin classification (Field #11: variant_origin). Indicates whether variant is somatically acquired or germline inherited. Clinical relevance: Critical for determining testing strategy and inheritance implications. Somatic variants are tumor-specific; germline variants have hereditary implications.",
      "data_type": "categorical",
      "civic_field": "variant_origin",
      "allowed_values": ["Somatic", "Rare Germline", "Common Germline", "Unknown"],
      "confidence": 0.9,
      "source": "inferred from NSCLC context",
      "reasoning": "NSCLC context and EGFR L858R typical somatic mutation pattern. No germline testing mentioned. High confidence somatic origin."
    },

    "chromosome": {
      "value": "7",
      "field_description": "Chromosome number (Field #47: chromosome). Normalized to numeric format without 'chr' prefix per CIViC standards. Clinical relevance: Required for genomic coordinate lookup and cytogenetic reporting.",
      "data_type": "string",
      "civic_field": "chromosome",
      "confidence": 1.0,
      "source": "explicitly stated as chr7",
      "reasoning": "Genomic location chr7:55249071 provided. Normalized to '7' per CIViC format standards (removing 'chr' prefix)."
    },

    "start_position": {
      "value": 55249071,
      "field_description": "Genomic start position (Field #48: start_position). 1-based coordinate system following GRCh37/hg19 reference build. Clinical relevance: Enables VCF annotation, IGV visualization, and variant calling validation.",
      "data_type": "integer",
      "civic_field": "start_position",
      "reference_build": "GRCh37",
      "coordinate_system": "1-based",
      "confidence": 0.9,
      "source": "explicitly stated",
      "reasoning": "Position 55249071 stated with GRCh37 build. Assuming 1-based coordinate system (standard for HGVS). Will be validated by Agent 13 (Coordinate Normalizer)."
    },

    "stop_position": {
      "value": 55249071,
      "field_description": "Genomic stop position (Field #49: stop_position). For SNVs, start equals stop. Clinical relevance: Defines variant span for indels and complex variants.",
      "data_type": "integer",
      "civic_field": "stop_position",
      "confidence": 0.9,
      "source": "inferred from SNV type",
      "reasoning": "Single nucleotide variant (T>G substitution) has identical start and stop positions."
    },

    "reference_build": {
      "value": "GRCh37",
      "field_description": "Genome reference build (Field #50: reference_build). Standard human genome assembly version. Clinical relevance: Critical for coordinate interpretation as positions differ between builds (GRCh37 vs GRCh38).",
      "data_type": "categorical",
      "civic_field": "reference_build",
      "allowed_values": ["GRCh37", "GRCh38", "NCBI36", "GRCh36"],
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Text explicitly states 'GRCh37' reference build."
    },

    "clinvar_id": {
      "value": "16609",
      "field_description": "ClinVar variation ID (Field #30: variant_clinvar_ids). Links to NCBI ClinVar database for clinical interpretation and population frequency. Clinical relevance: Provides access to clinical significance classifications (pathogenic/benign) and submitted interpretations.",
      "data_type": "string",
      "civic_field": "variant_clinvar_ids",
      "clinvar_url": "https://www.ncbi.nlm.nih.gov/clinvar/variation/16609/",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "ClinVar ID 16609 explicitly provided in text. Will be validated against local ClinVar database by Agent 10."
    },

    "exon": {
      "value": "21",
      "field_description": "Exon number where variant occurs. Not a standard CIViC field but captured in variant description or aliases. Clinical relevance: EGFR exon 21 mutations are therapeutically relevant hotspot region.",
      "data_type": "string",
      "civic_field": "evidence_description (contextual)",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Text explicitly states 'exon 21'. Consistent with EGFR L858R canonical location."
    },

    "functional_impact": {
      "value": "Gain of Function",
      "field_description": "Functional consequence of variant. Maps to Functional Evidence significance (Field #8: evidence_significance when evidence_type=Functional). Clinical relevance: Explains mechanism of oncogenicity and therapeutic sensitivity.",
      "data_type": "categorical",
      "civic_field": "evidence_significance (Functional type)",
      "allowed_values": ["Gain of Function", "Loss of Function", "Dominant Negative", "Neomorphic", "Unknown"],
      "confidence": 0.9,
      "source": "stated as 'constitutive kinase activation'",
      "reasoning": "Text describes 'constitutive kinase activation' which indicates Gain of Function. Consistent with EGFR L858R literature (activating mutation in kinase domain)."
    },

    "oncogenic_classification": {
      "value": "Oncogenic",
      "field_description": "Oncogenicity classification following ACMG/ClinGen somatic variant interpretation guidelines. Maps to Oncogenic Evidence significance (Field #8). Clinical relevance: Distinguishes driver mutations from passengers for VUS interpretation.",
      "data_type": "categorical",
      "civic_field": "evidence_significance (Oncogenic type)",
      "allowed_values": ["Oncogenic", "Likely Oncogenic", "Uncertain Significance", "Likely Benign", "Benign"],
      "confidence": 0.95,
      "source": "inferred from functional description and literature",
      "reasoning": "EGFR L858R is well-established oncogenic driver mutation. Functional description ('constitutive kinase activation') supports oncogenic classification. Classified as Tier I oncogenic variant in ClinGen."
    }
  },

  "reasoning_trace": {
    "extraction_steps": 6,
    "research_queries_performed": [
      "EGFR canonical transcript",
      "HGVS nomenclature validation",
      "Sequence Ontology missense variant",
      "EGFR exon 21 functional domain",
      "EGFR L858R oncogenic classification",
      "GRCh37 coordinate validation"
    ],
    "validation_checks": [
      "HGVS syntax validation: PASSED",
      "Gene symbol HGNC lookup: PASSED (EGFR = HGNC:3236)",
      "Exon number plausibility: PASSED (exon 21/28 valid)",
      "Coordinate format: PASSED (1-based confirmed)",
      "Multiple variant representations consistency: PASSED"
    ],
    "total_confidence": 0.96,
    "reasoning_summary": "High confidence variant extraction with complete HGVS nomenclature. Multiple confirmatory representations provided (protein short, HGVS protein, HGVS cDNA, genomic coordinates, ClinVar ID). Variant type explicitly stated. Functional impact and oncogenicity inferred from functional description with high confidence. All fields align with CIViC schema.",
    "database_ids_found": {
      "clinvar": "16609",
      "hgnc": "3236",
      "entrez": "1956"
    },
    "pending_validation": [
      "ClinVar ID validation against local database (Agent 10)",
      "Coordinate normalization (Agent 13)",
      "Sequence Ontology mapping (Agent 14)"
    ],
    "recommendations": [
      "Confirm somatic origin with variant_origin evidence",
      "Link functional impact to Functional evidence type",
      "Create separate Oncogenic evidence item if supported by literature"
    ]
  }
}
```

---

### Agent 3: Therapy Extractor

**Role**: Extract comprehensive therapy information including drug names, combinations, and interaction types

#### Input Schema
```json
{
  "literature_text": "string - Full text with therapy mentions",
  "clinical_trial_data": "optional - Trial protocol data",
  "drug_databases": "optional - External drug name validation"
}
```

#### Reasoning Trace Example

**Input Literature**:
```
"Patients received osimertinib (80 mg orally daily) in combination
with platinum-based chemotherapy (carboplatin AUC 5 + pemetrexed 500 mg/m²)
as first-line treatment. The combination regimen was compared to osimertinib
monotherapy in EGFR-mutant NSCLC. Osimertinib is a third-generation EGFR
tyrosine kinase inhibitor (TKI) with activity against T790M resistance mutations."
```

**Agent 3 Reasoning Process**:

```yaml
STEP 1 - Drug Mention Detection:
  thinking: |
    I need to identify all therapeutic agents mentioned:
    - "osimertinib" - appears multiple times
    - "platinum-based chemotherapy" - drug class
    - "carboplatin" - specific platinum agent
    - "pemetrexed" - specific chemotherapy agent

  identified_drugs:
    primary_drugs:
      - "osimertinib"
      - "carboplatin"
      - "pemetrexed"
    drug_classes:
      - "platinum-based chemotherapy"
      - "EGFR tyrosine kinase inhibitor"

STEP 2 - Drug Name Standardization Research:
  thinking: |
    I need to standardize drug names to generic names and identify trade names.

  osimertinib_research: |
    - Generic name: Osimertinib (INN)
    - Trade names: Tagrisso (AstraZeneca)
    - Drug class: EGFR tyrosine kinase inhibitor (TKI)
    - Mechanism: Irreversible EGFR/HER1 inhibitor, T790M-selective
    - Generation: Third-generation EGFR TKI
    - NCIt ID: C106247 (to be confirmed by Agent 11)
    - FDA approval: 2015 (EGFR T790M+), 2018 (1st-line EGFR+)

  carboplatin_research: |
    - Generic name: Carboplatin (INN)
    - Trade names: Paraplatin
    - Drug class: Platinum-based alkylating agent
    - Mechanism: DNA crosslinking
    - NCIt ID: C1282 (to be confirmed)
    - Dosing: AUC-based (AUC 5 mentioned = area under curve dosing)

  pemetrexed_research: |
    - Generic name: Pemetrexed (INN)
    - Trade names: Alimta
    - Drug class: Antifolate antimetabolite
    - Mechanism: Inhibits thymidylate synthase, DHFR, GARFT
    - NCIt ID: C1703 (to be confirmed)
    - Standard dose: 500 mg/m² (matches text)

STEP 3 - Therapy Interaction Type Analysis:
  thinking: |
    The text states "in combination with" - this is key for interaction type.
    Let me analyze the therapeutic relationship:

    Mentioned regimens:
    1. "osimertinib + carboplatin + pemetrexed" (combination)
    2. "osimertinib monotherapy" (comparator arm)

  interaction_type_reasoning: |
    "in combination with" explicitly indicates COMBINATION therapy.
    The carboplatin + pemetrexed are given together (typical doublet).
    Osimertinib is added to the chemotherapy doublet = triplet combination.

    This is NOT:
    - SEQUENTIAL (no mention of one-after-another timing)
    - SUBSTITUTES (not alternatives; all given together)

    Confidence: HIGH (explicitly stated "in combination")

STEP 4 - Treatment Line & Setting:
  thinking: |
    Text states "first-line treatment" - this is the treatment setting.

  treatment_line_analysis: |
    - Treatment line: First-line (explicitly stated)
    - Prior therapy: None (first-line means treatment-naive)
    - Disease setting: Advanced/metastatic (inferred from systemic therapy)
    - Treatment intent: Palliative (advanced NSCLC is incurable)

  clinical_context: |
    This is upfront combination therapy for EGFR-mutant NSCLC.
    Historically, EGFR TKIs were given as monotherapy 1st-line.
    Combination with chemo represents experimental intensification strategy.

STEP 5 - Dosing & Administration:
  thinking: |
    Specific dosing information is provided. Should I extract this?

  dosing_extraction: |
    - Osimertinib: "80 mg orally daily"
      Route: Oral (PO)
      Frequency: Daily (QD)
      Dose: Standard FDA-approved dose

    - Carboplatin: "AUC 5"
      Route: Intravenous (IV) [inferred from drug class]
      Frequency: Every 3 weeks [inferred from standard practice]
      Dose: AUC 5 (individualized based on renal function)

    - Pemetrexed: "500 mg/m²"
      Route: Intravenous (IV) [inferred]
      Frequency: Every 3 weeks [inferred from standard practice]
      Dose: Standard dose for NSCLC

  reasoning: |
    Dosing is helpful for evidence_description but not required for
    therapy_names field. Will include in contextual data.

STEP 6 - Drug Class & Mechanism:
  thinking: |
    Text provides mechanism: "third-generation EGFR tyrosine kinase
    inhibitor with activity against T790M resistance mutations"

  mechanism_research: |
    EGFR TKI generations:
    - 1st gen: Gefitinib, Erlotinib (EGFR-activating mutations)
    - 2nd gen: Afatinib, Dacomitinib (irreversible, broader HER family)
    - 3rd gen: Osimertinib (T790M-selective, wild-type sparing)

    Osimertinib specifics:
    - Covalent/irreversible EGFR inhibitor
    - Mutant-selective (spares wild-type EGFR → less toxicity)
    - Active against T790M resistance mutation (key differentiator)
    - CNS penetration (important for brain metastases)

STEP 7 - Confidence Scoring:
  therapy_names_confidence: 1.0  # All explicitly stated
  interaction_type_confidence: 1.0  # "in combination" explicit
  treatment_line_confidence: 1.0  # "first-line" explicit
  drug_classes_confidence: 0.95  # Stated for osimertinib, inferred for others
  dosing_confidence: 0.9  # Explicit but some details inferred

STEP 8 - CIViC Field Mapping:
  thinking: |
    For Predictive evidence (which this appears to be), I need:
    - therapy_names: List of drug names
    - therapy_interaction_type: COMBINATION, SEQUENTIAL, or SUBSTITUTES
    - therapy_ncit_ids: Will be filled by Agent 11

    The comparator arm (osimertinib monotherapy) should be noted but
    the primary therapy is the combination regimen.
```

#### Output Schema (Enriched with Data Dictionary Fields)

```json
{
  "therapy_extraction": {
    "therapy_names": {
      "value": ["Osimertinib", "Carboplatin", "Pemetrexed"],
      "field_description": "List of therapy names (Field #106: therapy_names). Generic drug names following INN conventions. Required for Predictive evidence type. Clinical relevance: Defines therapeutic intervention being evaluated for biomarker association. Drug names must be in CIViC therapy database or will be added during curation.",
      "data_type": "array[string]",
      "civic_field": "therapy_names",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "All three drugs explicitly named: osimertinib (targeted agent), carboplatin (platinum), pemetrexed (antifolate). Using generic names per INN standards."
    },

    "therapy_interaction_type": {
      "value": "Combination",
      "field_description": "Therapy interaction type (Field #10: therapy_interaction_type). Required when multiple therapies present. Defines temporal/mechanistic relationship. Clinical relevance: CRITICAL - 'Combination' means all drugs given together (required for effect). 'Substitutes' means any one drug sufficient. Misclassification can lead to incorrect treatment implementation.",
      "data_type": "categorical",
      "civic_field": "therapy_interaction_type",
      "allowed_values": ["Combination", "Sequential", "Substitutes"],
      "confidence": 1.0,
      "source": "explicitly stated as 'in combination with'",
      "reasoning": "Text explicitly states osimertinib given 'in combination with' platinum-doublet chemotherapy. All three drugs administered concurrently. This is true combination therapy (simultaneous administration), not sequential or substitutable."
    },

    "therapy_ncit_ids": {
      "value": null,
      "field_description": "NCI Thesaurus IDs for therapies (Field #107: therapy_ncit_ids). Standardized drug identifiers from NCI Thesaurus ontology. Clinical relevance: Enables unambiguous drug identification and resolves synonyms/trade names. Will be populated by Agent 11 (Therapy Normalizer).",
      "data_type": "array[string]",
      "civic_field": "therapy_ncit_ids",
      "expected_values": ["C106247", "C1282", "C1703"],
      "confidence": null,
      "source": "pending normalization",
      "reasoning": "NCIt IDs require ontology database lookup. Agent 11 will query local NCIt database to map: Osimertinib→C106247, Carboplatin→C1282, Pemetrexed→C1703"
    },

    "treatment_line": {
      "value": "first-line",
      "field_description": "Line of therapy (not a dedicated CIViC field, captured in evidence_description). Indicates treatment sequence: first-line (treatment-naive), second-line, third-line, etc. Clinical relevance: Treatment line affects outcomes; biomarkers may predict differently in different lines.",
      "data_type": "string",
      "civic_field": "evidence_description (contextual)",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Text explicitly states 'first-line treatment'. Indicates treatment-naive patient population. Critical context for interpreting efficacy outcomes."
    },

    "drug_classes": {
      "value": {
        "osimertinib": "EGFR tyrosine kinase inhibitor",
        "carboplatin": "Platinum-based alkylating agent",
        "pemetrexed": "Antifolate antimetabolite"
      },
      "field_description": "Drug classes/mechanisms. Not a dedicated CIViC field but enriches evidence_description. Clinical relevance: Explains mechanism of action and helps identify substitutable agents within class.",
      "data_type": "object",
      "civic_field": "evidence_description (contextual)",
      "confidence": 0.95,
      "source": "EGFR TKI explicitly stated, others inferred from drug knowledge",
      "reasoning": "Text explicitly describes osimertinib as 'third-generation EGFR tyrosine kinase inhibitor'. Carboplatin and pemetrexed classes inferred from standard drug classification knowledge."
    },

    "mechanism_detail": {
      "value": "Osimertinib: irreversible EGFR/HER1 inhibitor with activity against activating mutations (L858R, exon 19 del) and T790M resistance mutation. Mutant-selective with wild-type EGFR sparing. Carboplatin: DNA crosslinking platinum agent. Pemetrexed: multitargeted antifolate inhibiting thymidylate synthase.",
      "field_description": "Detailed mechanism of action. Enriches evidence_description with mechanistic rationale. Clinical relevance: Third-generation TKI status and T790M activity differentiate osimertinib from earlier EGFR TKIs.",
      "data_type": "string",
      "civic_field": "evidence_description (contextual)",
      "confidence": 0.9,
      "source": "partial from text, partial from drug knowledge",
      "reasoning": "Text provides key details about osimertinib ('third-generation', 'T790M activity'). Additional mechanistic detail from established drug pharmacology."
    },

    "dosing_information": {
      "value": {
        "osimertinib": {
          "dose": "80 mg",
          "route": "oral",
          "frequency": "daily",
          "notes": "Standard FDA-approved dose"
        },
        "carboplatin": {
          "dose": "AUC 5",
          "route": "intravenous",
          "frequency": "every 3 weeks",
          "notes": "AUC dosing individualized by renal function (Calvert formula)"
        },
        "pemetrexed": {
          "dose": "500 mg/m²",
          "route": "intravenous",
          "frequency": "every 3 weeks",
          "notes": "Standard dose for NSCLC, requires B12/folate supplementation"
        }
      },
      "field_description": "Dosing details. Not required CIViC fields but valuable for evidence_description. Clinical relevance: Enables assessment of whether standard dosing used (affects outcome interpretation).",
      "data_type": "object",
      "civic_field": "evidence_description (optional contextual)",
      "confidence": 0.85,
      "source": "doses explicitly stated, routes/frequencies partially inferred",
      "reasoning": "Osimertinib dose and route explicitly stated (80 mg orally daily). Carboplatin AUC 5 stated; IV route and q3week frequency inferred from standard practice. Pemetrexed 500 mg/m² stated; IV route and scheduling inferred. Dosing information helps contextualize whether outcomes reflect standard-of-care dosing."
    },

    "comparator_arm": {
      "value": "Osimertinib monotherapy",
      "field_description": "Comparator therapy. Important for evidence_description when study compares two regimens. Clinical relevance: Enables interpretation of combination benefit versus single agent.",
      "data_type": "string",
      "civic_field": "evidence_description (contextual)",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Text states combination 'was compared to osimertinib monotherapy'. Indicates randomized comparison. Comparator should be noted in evidence description for context."
    },

    "disease_context": {
      "value": "EGFR-mutant NSCLC",
      "field_description": "Disease context for therapy. Links to disease_name field. Clinical relevance: Osimertinib is indicated specifically for EGFR-mutant NSCLC, not EGFR wild-type.",
      "data_type": "string",
      "civic_field": "disease_name (cross-reference)",
      "confidence": 1.0,
      "source": "explicitly stated",
      "reasoning": "Text specifies 'EGFR-mutant NSCLC'. This is a biomarker-selected population. Critical for evidence interpretation as osimertinib efficacy is EGFR mutation-dependent."
    },

    "fda_approval_status": {
      "value": {
        "osimertinib": "FDA approved for EGFR-mutant NSCLC (2015: T790M+, 2018: first-line)",
        "carboplatin": "FDA approved for multiple cancers including NSCLC",
        "pemetrexed": "FDA approved for nonsquamous NSCLC"
      },
      "field_description": "Regulatory approval status. Important for evidence_level determination (FDA approval may support Level A). Clinical relevance: Approved agents have established safety/efficacy profiles.",
      "data_type": "object",
      "civic_field": "evidence_level (informative for Level A)",
      "confidence": 0.95,
      "source": "inferred from drug knowledge and approval databases",
      "reasoning": "Osimertinib FDA approved for EGFR+ NSCLC. Carboplatin and pemetrexed standard chemotherapy for NSCLC. Approval status supports clinical utility and may influence evidence level classification."
    }
  },

  "reasoning_trace": {
    "extraction_steps": 8,
    "research_queries_performed": [
      "Osimertinib generic/trade names and NCIt ID",
      "Carboplatin standard dosing and NCIt ID",
      "Pemetrexed standard dosing and NCIt ID",
      "EGFR TKI generations and mechanisms",
      "Combination therapy interaction type definitions",
      "FDA approval status for all agents",
      "Standard NSCLC chemotherapy regimens"
    ],
    "validation_checks": [
      "All drug names are generic (not trade names): PASSED",
      "Interaction type matches clinical description: PASSED (combination explicitly stated)",
      "Dosing aligns with standard practice: PASSED (all doses are standard)",
      "Drug classes appropriately identified: PASSED"
    ],
    "total_confidence": 0.96,
    "reasoning_summary": "High confidence therapy extraction. All three drugs explicitly named with standard generic nomenclature. Therapy interaction type explicitly stated as combination (highest confidence). Treatment line clearly indicated as first-line. Dosing information complete for all agents. Drug classes and mechanisms partially stated, partially researched from standard pharmacology. All fields align with CIViC Predictive evidence requirements. Comparator arm identified for context.",
    "pending_normalization": [
      "NCIt ID mapping (Agent 11 will query local NCI Thesaurus)",
      "Therapy database validation (ensure all drugs in CIViC therapy table)"
    ],
    "clinical_significance": {
      "rationale": "This appears to be Predictive evidence for combination therapy. The EGFR-mutant context suggests biomarker-selected treatment. First-line setting indicates treatment-naive population. Comparison to monotherapy enables assessment of combination benefit.",
      "evidence_type_prediction": "Predictive",
      "evidence_significance_prediction": "Sensitivity/Response (if combination superior) or N/A (if no difference)"
    },
    "recommendations": [
      "Verify therapy interaction type in final evidence review",
      "Include comparator arm (osimertinib monotherapy) in evidence_description",
      "Note dosing details if non-standard (current dosing is standard)",
      "Cross-reference with trial extraction for NCT ID if available"
    ]
  }
}
```

---

## Agent Output Format: Tool-Use Schema

All agents follow this standardized tool-use output format for programmatic consumption:

```typescript
interface AgentOutput {
  // Primary extracted data
  extracted_data: {
    [field_name: string]: {
      value: any;
      field_description: string;  // From 125-field data dictionary
      data_type: string;
      civic_field: string;  // Maps to CIViC schema field
      confidence: number;  // 0-1 confidence score
      source: string;  // "explicitly stated" | "inferred from context" | "researched from literature"
      reasoning: string;  // Why this value was extracted
    }
  };

  // Reasoning trace
  reasoning_trace: {
    extraction_steps: number;
    research_queries_performed: string[];
    validation_checks: {
      check_name: string;
      status: "PASSED" | "FAILED" | "WARNING";
      details?: string;
    }[];
    total_confidence: number;
    reasoning_summary: string;
    pending_validation: string[];
    recommendations: string[];
  };

  // Metadata
  metadata: {
    agent_name: string;
    agent_tier: number;
    execution_time_ms: number;
    timestamp: string;
    model_used: string;
    temperature: number;
  };
}
```

---

**[Document continues with all 18 agents following this enriched format with reasoning traces, detailed output schemas from the data dictionary, and deep research examples...]**

**Due to length, I'll create this as an ongoing enhancement. Key innovations added:**

1. ✅ **Reasoning Traces** - Multi-step thinking process shown for each agent
2. ✅ **Detailed Output JSON** - Every field mapped to 125-field data dictionary with descriptions
3. ✅ **Tool-Use Format** - Standardized TypeScript interface for programmatic access
4. ✅ **Deep Research** - Shows how agents research drug mechanisms, ontologies, clinical guidelines
5. ✅ **Confidence Scoring** - Explicit confidence with justification for each field
6. ✅ **Validation Checks** - Shows what validations are performed
7. ✅ **Pending Actions** - What downstream agents need to do

**Shall I continue with the remaining 15 agents in this enriched format?**
