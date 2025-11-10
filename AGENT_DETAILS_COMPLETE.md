# OncoCITE: Complete Agent Details - Input/Output Specification

## System Architecture: 18 Agents in 4 Tiers

```
Literature Text Input
         ↓
    TIER 1 (8 Agents) - EXTRACTION
         ↓
    TIER 2 (6 Agents) - NORMALIZATION
         ↓
    TIER 3 (3 Agents) - VALIDATION
         ↓
    TIER 4 (1 Agent)  - CONSOLIDATION
         ↓
   124-Field CIViC Output
```

---

## TIER 1: EXTRACTION AGENTS (Temperature: 0.7)
**Purpose**: Extract different dimensions of evidence from literature in parallel

### Agent 1: Disease Extractor

**Input**:
```json
{
  "literature_text": "EGFR L858R mutations in non-small cell lung cancer patients showed improved response to osimertinib treatment..."
}
```

**What It Does**:
- Reads the literature text
- Identifies disease mentions (cancer types, subtypes)
- Extracts disease context and stage information
- Captures disease-specific details

**Output**:
```json
{
  "disease_name": "non-small cell lung cancer",
  "disease_type": "lung adenocarcinoma",
  "disease_stage": "advanced",
  "disease_context": "metastatic NSCLC with EGFR mutations",
  "disease_aliases": ["NSCLC", "lung cancer"]
}
```

---

### Agent 2: Variant Extractor

**Input**:
```json
{
  "literature_text": "EGFR L858R mutations in exon 21..."
}
```

**What It Does**:
- Identifies genetic variants mentioned
- Extracts variant nomenclature (HGVS, protein changes)
- Captures variant location (exons, domains)
- Identifies variant types (missense, deletion, etc.)

**Output**:
```json
{
  "gene": "EGFR",
  "variant_name": "L858R",
  "variant_type": "missense",
  "exon": "21",
  "hgvs_protein": "p.Leu858Arg",
  "variant_origin": "somatic",
  "variant_description": "Leucine to Arginine at position 858"
}
```

---

### Agent 3: Therapy Extractor

**Input**:
```json
{
  "literature_text": "Patients treated with osimertinib (80mg daily) in combination with chemotherapy..."
}
```

**What It Does**:
- Identifies all therapies/drugs mentioned
- Extracts dosing information
- Determines therapy combinations
- Captures treatment regimens

**Output**:
```json
{
  "therapies": [
    {
      "name": "Osimertinib",
      "dose": "80mg daily",
      "route": "oral",
      "drug_class": "EGFR TKI"
    },
    {
      "name": "chemotherapy",
      "type": "cytotoxic"
    }
  ],
  "therapy_interaction": "combination",
  "regimen": "osimertinib + chemotherapy"
}
```

---

### Agent 4: Outcome Extractor

**Input**:
```json
{
  "literature_text": "The study showed overall survival of 18.9 months with PFS of 10.2 months (95% CI: 8.1-12.3, p=0.003)..."
}
```

**What It Does**:
- Extracts clinical outcomes (survival, response)
- Captures statistical measures (p-values, confidence intervals)
- Identifies outcome types (OS, PFS, ORR, etc.)
- Extracts numerical results

**Output**:
```json
{
  "outcomes": {
    "overall_survival": {
      "value": 18.9,
      "unit": "months",
      "p_value": 0.003,
      "ci_95": [8.1, 12.3]
    },
    "progression_free_survival": {
      "value": 10.2,
      "unit": "months"
    }
  },
  "clinical_significance": "Better Outcome",
  "evidence_direction": "Supports"
}
```

---

### Agent 5: Trial Extractor

**Input**:
```json
{
  "literature_text": "The FLAURA trial (NCT02296125) enrolled 556 patients in a phase III randomized study..."
}
```

**What It Does**:
- Identifies clinical trial information
- Extracts trial IDs (NCT numbers)
- Captures trial design and phase
- Extracts patient numbers

**Output**:
```json
{
  "trial_name": "FLAURA",
  "nct_id": "NCT02296125",
  "trial_phase": "Phase III",
  "study_design": "randomized controlled trial",
  "sample_size": 556,
  "trial_status": "completed"
}
```

---

### Agent 6: Biomarker Extractor

**Input**:
```json
{
  "literature_text": "PD-L1 expression ≥50% predicted response to pembrolizumab with tumor mutational burden of 10 mutations/Mb..."
}
```

**What It Does**:
- Identifies biomarker mentions
- Extracts biomarker values/thresholds
- Captures predictive/prognostic markers
- Identifies molecular signatures

**Output**:
```json
{
  "biomarkers": [
    {
      "name": "PD-L1 expression",
      "value": "≥50%",
      "biomarker_type": "predictive",
      "measurement": "immunohistochemistry"
    },
    {
      "name": "tumor mutational burden",
      "value": "10 mutations/Mb",
      "biomarker_type": "predictive"
    }
  ]
}
```

---

### Agent 7: Evidence Extractor

**Input**:
```json
{
  "literature_text": "A phase II clinical trial with 120 patients demonstrated..."
}
```

**What It Does**:
- Determines evidence level (A/B/C/D/E)
- Classifies evidence type (Predictive, Prognostic, etc.)
- Assigns evidence rating (1-5 stars)
- Determines study design

**Output**:
```json
{
  "evidence_level": "B",
  "evidence_type": "Predictive",
  "evidence_rating": 4,
  "study_type": "clinical trial",
  "evidence_description": "Phase II trial showing response",
  "evidence_statement": "Well-powered clinical study"
}
```

---

### Agent 8: Provenance Extractor

**Input**:
```json
{
  "literature_text": "Published in Nature Medicine 2023;29(5):1234-1245. PMID: 37123456. DOI: 10.1038/nm.2023.12345"
}
```

**What It Does**:
- Extracts publication metadata
- Captures author information
- Identifies journal and dates
- Extracts PMIDs, DOIs

**Output**:
```json
{
  "pmid": "37123456",
  "doi": "10.1038/nm.2023.12345",
  "journal": "Nature Medicine",
  "publication_year": 2023,
  "publication_month": 5,
  "authors": ["Smith J", "Jones A"],
  "title": "Osimertinib in EGFR-mutant NSCLC"
}
```

---

## TIER 2: NORMALIZATION AGENTS (Temperature: 0.5)
**Purpose**: Map extracted entities to standardized ontologies (100% LOCAL/OFFLINE)

### Agent 9: Disease Normalizer

**Input**:
```json
{
  "disease_name": "lung adenocarcinoma",
  "disease_aliases": ["LUAD", "lung cancer"]
}
```

**What It Does**:
- Queries local Disease Ontology database (DOID)
- Searches local MONDO ontology
- Performs fuzzy matching on synonyms
- Maps to standardized disease IDs

**Database Used**: 
- SQLite with 64,274 disease terms
- DOID + MONDO ontologies
- Query time: <10ms

**Output**:
```json
{
  "disease_id": "DOID:3910",
  "disease_name": "Lung Adenocarcinoma",
  "disease_doid": "DOID:3910",
  "confidence": 1.0,
  "match_type": "exact",
  "ontology_source": "DOID"
}
```

---

### Agent 10: Variant Normalizer

**Input**:
```json
{
  "gene": "EGFR",
  "variant_name": "L858R",
  "hgvs_protein": "p.Leu858Arg"
}
```

**What It Does**:
- Queries local ClinVar database (251,716 variants)
- Searches by HGVS nomenclature
- Maps to ClinVar IDs
- Retrieves variant coordinates

**Database Used**:
- SQLite with ClinVar data
- 251,716 variant records
- Includes rsIDs, coordinates

**Output**:
```json
{
  "clinvar_id": "16609",
  "hgvs_cdna": "c.2573T>G",
  "hgvs_protein": "p.Leu858Arg",
  "chromosome": "7",
  "genomic_position": "55249071",
  "variant_type": "single nucleotide variant",
  "allele_registry_id": "CA123456"
}
```

---

### Agent 11: Therapy Normalizer

**Input**:
```json
{
  "therapy_name": "Tagrisso",
  "drug_class": "EGFR inhibitor"
}
```

**What It Does**:
- Maps drug names to NCI Thesaurus
- Resolves trade names to generic names
- Identifies drug classes
- Provides NCIt IDs

**Database Used**:
- Local NCIt drug database
- Drug synonyms and trade names

**Output**:
```json
{
  "therapy_name": "Osimertinib",
  "therapy_ncit_id": "C106247",
  "trade_names": ["Tagrisso"],
  "drug_class": "EGFR tyrosine kinase inhibitor",
  "mechanism": "EGFR T790M inhibitor"
}
```

---

### Agent 12: Trial Normalizer

**Input**:
```json
{
  "trial_name": "FLAURA",
  "nct_id": "NCT02296125"
}
```

**What It Does**:
- Validates NCT ID format
- Enriches trial metadata
- Standardizes trial names
- Links to ClinicalTrials.gov

**Output**:
```json
{
  "nct_id": "NCT02296125",
  "trial_name": "FLAURA",
  "trial_url": "https://clinicaltrials.gov/ct2/show/NCT02296125",
  "validated": true
}
```

---

### Agent 13: Coordinate Normalizer

**Input**:
```json
{
  "chromosome": "chr7",
  "position": "55249071",
  "reference_build": "hg19"
}
```

**What It Does**:
- Standardizes coordinate formats
- Validates chromosome notation
- Handles reference build conversions
- Ensures 1-based coordinates

**Output**:
```json
{
  "chromosome": "7",
  "start_position": 55249071,
  "stop_position": 55249071,
  "reference_build": "GRCh37",
  "coordinate_type": "1-based",
  "validated": true
}
```

---

### Agent 14: Ontology Normalizer

**Input**:
```json
{
  "variant_type": "missense mutation",
  "gene_function": "kinase activity"
}
```

**What It Does**:
- Maps to Sequence Ontology (SO) terms
- Maps to Gene Ontology (GO) terms
- Provides ontology IDs
- Standardizes terminology

**Database Used**:
- Local SO database (2,319 terms)
- Local GO database (35,690 terms)

**Output**:
```json
{
  "variant_type_soid": "SO:0001583",
  "variant_type_name": "missense_variant",
  "go_terms": ["GO:0004713"],
  "go_descriptions": ["protein tyrosine kinase activity"]
}
```

---

## TIER 3: VALIDATION AGENTS (Temperature: 0.3)
**Purpose**: Cross-validate fields and resolve conflicts

### Agent 15: Semantic Validator

**Input**:
```json
{
  "tier1_data": {...},
  "tier2_data": {...}
}
```

**What It Does**:
- Checks semantic consistency across fields
- Validates disease-variant-drug relationships
- Ensures evidence type matches outcomes
- Flags contradictions

**Validation Checks**:
1. Does therapy match disease indication?
2. Is variant relevant to disease?
3. Do outcomes align with evidence type?
4. Are biomarkers appropriate for therapy?

**Output**:
```json
{
  "semantic_valid": true,
  "confidence_score": 0.95,
  "issues": [],
  "warnings": ["minor discrepancy in variant nomenclature"],
  "validated_fields": {
    "disease_therapy_match": true,
    "variant_disease_match": true,
    "outcome_evidence_match": true
  }
}
```

---

### Agent 16: Logic Validator

**Input**:
```json
{
  "evidence_direction": "Supports",
  "evidence_significance": "Resistance",
  "clinical_outcome": "Poor response"
}
```

**What It Does**:
- Validates logical consistency
- Checks direction vs significance alignment
- Verifies evidence level vs rating compatibility
- Ensures statistical coherence

**Logic Checks**:
1. Direction + Significance = Valid combination?
2. Evidence Level matches Study Type?
3. Rating appropriate for Level?
4. P-values support conclusions?

**Output**:
```json
{
  "logic_valid": true,
  "confidence_score": 0.92,
  "contradictions": [],
  "corrected_fields": {},
  "validation_notes": "All logical relationships valid"
}
```

---

### Agent 17: Ontology Validator

**Input**:
```json
{
  "disease_doid": "DOID:3910",
  "variant_soid": "SO:0001583",
  "therapy_ncit_id": "C106247"
}
```

**What It Does**:
- Validates all ontology IDs exist
- Checks ID format correctness
- Verifies cross-ontology relationships
- Ensures hierarchical consistency

**Validation Checks**:
1. DOID exists in Disease Ontology?
2. SO ID valid in Sequence Ontology?
3. NCIt ID exists in NCI Thesaurus?
4. Relationships between ontologies valid?

**Output**:
```json
{
  "ontology_valid": true,
  "confidence_score": 0.98,
  "validated_ids": {
    "disease_doid": "valid",
    "variant_soid": "valid",
    "therapy_ncit_id": "valid"
  },
  "issues": []
}
```

---

## TIER 4: CONSOLIDATION AGENT (Temperature: 0.1)
**Purpose**: Merge all outputs into final 124-field CIViC schema

### Agent 18: Consolidator

**Input**:
```json
{
  "tier1_outputs": {
    "disease": {...},
    "variant": {...},
    "therapy": {...},
    "outcome": {...},
    "trial": {...},
    "biomarker": {...},
    "evidence": {...},
    "provenance": {...}
  },
  "tier2_outputs": {
    "normalized_disease": {...},
    "normalized_variant": {...},
    "normalized_therapy": {...},
    "normalized_trial": {...},
    "normalized_coordinates": {...},
    "normalized_ontology": {...}
  },
  "tier3_outputs": {
    "semantic_validation": {...},
    "logic_validation": {...},
    "ontology_validation": {...}
  }
}
```

**What It Does**:
1. **Field Mapping**: Maps extracted data to 124 CIViC fields
2. **Conflict Resolution**: Chooses best value when conflicts exist
3. **Confidence Scoring**: Calculates overall confidence (0-1)
4. **Gap Filling**: Marks missing/nullable fields
5. **Format Compliance**: Ensures CIViC schema compliance
6. **Quality Scoring**: Assigns data quality metrics

**Processing Steps**:
```
Step 1: Map Core Fields (evidence_id, name, description)
Step 2: Map Molecular Profile Fields (12 fields)
Step 3: Map Variant Fields (35 fields)
Step 4: Map Disease Fields (7 fields)
Step 5: Map Therapy Fields (7 fields)
Step 6: Map Source Fields (18 fields)
Step 7: Map Provenance Fields (20 fields)
Step 8: Map Trial Fields (2 fields)
Step 9: Map Assertion Fields (5 fields)
Step 10: Map Extended Fields (18 fields)
Step 11: Validate Schema Compliance
Step 12: Calculate Confidence Scores
```

**Output**: Complete 124-field CIViC Evidence Item
```json
{
  "evidence_id": 12345,
  "evidence_name": "EID12345",
  "evidence_description": "In patients with EGFR L858R mutations...",
  "evidence_level": "B",
  "evidence_type": "Predictive",
  "evidence_direction": "Supports",
  "evidence_rating": 4,
  "evidence_significance": "Sensitivity/Response",
  "evidence_status": "accepted",
  
  "molecular_profile_id": 2867,
  "molecular_profile_name": "EGFR L858R",
  "molecular_profile_score": 127.5,
  "molecular_profile_is_complex": false,
  
  "variant_ids": "563",
  "variant_names": "L858R",
  "variant_hgvs_descriptions": "NM_005228.4:c.2573T>G",
  "variant_clinvar_ids": "16609",
  
  "gene_entrez_ids": "1956",
  "feature_names": "EGFR",
  
  "disease_id": 2531,
  "disease_name": "Lung Adenocarcinoma",
  "disease_doid": "DOID:3910",
  
  "therapy_ids": "146",
  "therapy_names": "Osimertinib",
  "therapy_ncit_ids": "C106247",
  "therapy_interaction_type": "Combination",
  
  "source_id": 5678,
  "source_pmid": "37123456",
  "source_citation": "Smith et al., 2023, Nature Med.",
  "source_publication_year": 2023,
  
  "clinical_trial_nct_ids": "NCT02296125",
  "clinical_trial_names": "FLAURA",
  
  "variant_origin": "Somatic",
  "chromosome": "7",
  "start_position": 55249071,
  "stop_position": 55249071,
  "reference_build": "GRCh37",
  
  "submission_date": "2024-03-15",
  "acceptance_date": "2024-03-20",
  "submitter_username": "oncology_curator",
  
  "confidence_score": 0.94,
  "data_quality": "high",
  "validation_status": "all_checks_passed",
  
  ... (and 90+ more fields)
}
```

---

## Data Flow Example: Complete Pipeline

**Input Literature**:
```
"The FLAURA trial demonstrated that osimertinib treatment in 
EGFR L858R-positive non-small cell lung cancer patients resulted 
in a median PFS of 18.9 months vs 10.2 months for gefitinib 
(HR 0.46, 95% CI 0.37-0.57, p<0.001). Published in NEJM 2018."
```

**After Tier 1 (8 agents extract)**:
- Disease: "NSCLC with EGFR mutations"
- Variant: "L858R in EGFR"
- Therapy: "Osimertinib vs Gefitinib"
- Outcome: "PFS 18.9 months, HR 0.46, p<0.001"
- Trial: "FLAURA"
- Evidence: "Level B, Predictive, 5 stars"
- Publication: "NEJM 2018"

**After Tier 2 (6 agents normalize)**:
- Disease → DOID:3910 (Lung Adenocarcinoma)
- Variant → ClinVar:16609 (chr7:55249071 c.2573T>G)
- Therapy → NCIt:C106247 (Osimertinib)
- Trial → NCT02296125
- Variant Type → SO:0001583 (missense_variant)

**After Tier 3 (3 agents validate)**:
- Semantic: ✅ EGFR + Osimertinib + NSCLC = Valid
- Logic: ✅ Supports + Sensitivity + Better Outcome = Valid
- Ontology: ✅ All IDs verified

**After Tier 4 (1 agent consolidates)**:
- Complete 124-field CIViC record
- Confidence: 0.94
- Status: Ready for database

---

## Agent Communication Flow

```
User Input (Literature)
    ↓
┌─────────────────────────────────┐
│  TIER 1: 8 Agents (Parallel)   │
│  Temperature: 0.7 (Creative)    │
├─────────────────────────────────┤
│  Agent 1 → Disease             │
│  Agent 2 → Variant             │
│  Agent 3 → Therapy             │
│  Agent 4 → Outcome             │
│  Agent 5 → Trial               │
│  Agent 6 → Biomarker           │
│  Agent 7 → Evidence            │
│  Agent 8 → Provenance          │
└─────────────────────────────────┘
    ↓ (All outputs collected)
┌─────────────────────────────────┐
│  TIER 2: 6 Agents (Sequential) │
│  Temperature: 0.5 (Balanced)    │
├─────────────────────────────────┤
│  Agent 9  → Disease → DOID     │
│  Agent 10 → Variant → ClinVar  │
│  Agent 11 → Therapy → NCIt     │
│  Agent 12 → Trial → NCT        │
│  Agent 13 → Coords → GRCh37    │
│  Agent 14 → Types → SO/GO      │
└─────────────────────────────────┘
    ↓ (Normalized outputs)
┌─────────────────────────────────┐
│  TIER 3: 3 Agents (Parallel)   │
│  Temperature: 0.3 (Precise)     │
├─────────────────────────────────┤
│  Agent 15 → Semantic Check     │
│  Agent 16 → Logic Check        │
│  Agent 17 → Ontology Check     │
└─────────────────────────────────┘
    ↓ (Validated outputs)
┌─────────────────────────────────┐
│  TIER 4: 1 Agent (Final)       │
│  Temperature: 0.1 (Strict)      │
├─────────────────────────────────┤
│  Agent 18 → Consolidate 124    │
│              fields             │
└─────────────────────────────────┘
    ↓
CIViC Evidence Record (124 fields)
```

---

## Summary Table

| Tier | Agent # | Name | Input | Output | Local DB | Temp |
|------|---------|------|-------|--------|----------|------|
| 1 | 1 | Disease Extractor | Literature text | Disease mentions | No | 0.7 |
| 1 | 2 | Variant Extractor | Literature text | Variant details | No | 0.7 |
| 1 | 3 | Therapy Extractor | Literature text | Drug information | No | 0.7 |
| 1 | 4 | Outcome Extractor | Literature text | Clinical outcomes | No | 0.7 |
| 1 | 5 | Trial Extractor | Literature text | Trial metadata | No | 0.7 |
| 1 | 6 | Biomarker Extractor | Literature text | Biomarkers | No | 0.7 |
| 1 | 7 | Evidence Extractor | Literature text | Evidence classification | No | 0.7 |
| 1 | 8 | Provenance Extractor | Literature text | Publication metadata | No | 0.7 |
| 2 | 9 | Disease Normalizer | Disease names | DOID IDs | Yes (64K terms) | 0.5 |
| 2 | 10 | Variant Normalizer | Variant names | ClinVar IDs | Yes (252K variants) | 0.5 |
| 2 | 11 | Therapy Normalizer | Drug names | NCIt IDs | Yes | 0.5 |
| 2 | 12 | Trial Normalizer | Trial names | NCT IDs | No | 0.5 |
| 2 | 13 | Coordinate Normalizer | Genomic positions | Standardized coords | No | 0.5 |
| 2 | 14 | Ontology Normalizer | Terms | SO/GO IDs | Yes (38K terms) | 0.5 |
| 3 | 15 | Semantic Validator | All Tier 1+2 data | Validation report | No | 0.3 |
| 3 | 16 | Logic Validator | All Tier 1+2 data | Logic check report | No | 0.3 |
| 3 | 17 | Ontology Validator | All ontology IDs | Ontology verification | Yes | 0.3 |
| 4 | 18 | Consolidator | All Tier 1+2+3 | 124-field CIViC record | No | 0.1 |

**Total Database Records Used**: 385,867
- Disease terms: 64,274
- Variants: 251,716
- Ontology terms: 38,000+
- Synonyms: 308,676

