import React, { useState } from 'react';
import { 
  ChevronDown, ChevronRight, Database, FileText, Search, 
  CheckCircle, AlertCircle, Brain, Layers, GitBranch,
  Activity, BarChart3, Shield, Workflow, Zap
} from 'lucide-react';

const OncociteArchitectureDetailed = () => {
  const [activeTab, setActiveTab] = useState('overview');
  const [expandedSections, setExpandedSections] = useState({});

  const toggleSection = (section) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  // Agent definitions with full details
  const agents = {
    phase1: [
      {
        id: 'agent1',
        name: 'Source Metadata Extractor',
        model: 'gpt-4o-mini',
        type: 'Extraction',
        description: 'Extracts publication metadata from PubMed/ASCO/ASH',
        inputs: ['Paper markdown', 'PubMed ID/ASCO ID/DOI'],
        outputs: ['source_id', 'source_type', 'source_title', 'source_authors', 'source_publication_year', 'clinical_trial_nct_ids'],
        tools: ['PubMed E-utilities API', 'ASCO API', 'ASH API'],
        evaluation: 'Exact match against database (98%+ target)',
        dependencies: [],
        instructions: `Extract all source metadata fields:
1. Parse identifier type (PMID/ASCO/DOI)
2. Query appropriate API (PubMed E-utilities/ASCO/ASH)
3. Extract: title, authors, journal, year, month, day, abstract
4. If PubMed: Check for clinical_trial_nct_ids in metadata
5. Format authors as comma-separated list
6. Generate source_citation: "First Author et al., Year, Journal"
7. Return structured metadata object`,
        sequence: `User->>Agent1: paper_id="12345678", type="PMID"
Agent1->>PubMed API: GET /esearch.fcgi?id=12345678
PubMed API-->>Agent1: XML metadata
Agent1->>Agent1: Parse title, authors, journal, year
Agent1->>PubMed API: Check for clinical trial links
PubMed API-->>Agent1: NCT ID if linked
Agent1-->>Orchestrator: Return source metadata object`
      },
      {
        id: 'agent2',
        name: 'Biomedical Entity Recognizer (NER)',
        model: 'BioBERT + gpt-4o-mini',
        type: 'NER',
        description: 'Tags all biomedical entities in full paper text',
        inputs: ['Full paper text (all sections)'],
        outputs: ['Tagged entities: genes, variants, drugs, diseases, phenotypes', 'Entity positions in text', 'Confidence scores'],
        tools: ['BioBERT', 'PubTator', 'Custom NER models'],
        evaluation: 'F1 score vs gold standard (85%+ genes, 75%+ variants)',
        dependencies: [],
        instructions: `Identify and tag all biomedical entities:
1. Genes: Use Entrez Gene database, identify by symbol or full name
   - Normalize to HGNC symbols (e.g., "HER2" → "ERBB2")
   - Track positions in text for later reference
2. Variants: Detect HGVS notation, common names, protein changes
   - Pattern match: V600E, L858R, Exon 19 deletion, etc.
   - Record variant type hints (missense, frameshift, fusion)
3. Drugs/Therapies: NCIt vocabulary
   - Map to generic names (not trade names)
   - Identify regimen names (FOLFOX, R-CHOP)
4. Diseases: Disease Ontology terms
   - Capture specificity (adenocarcinoma vs lung cancer)
5. Phenotypes: HPO terms when mentioned
6. Statistics: n=178, p<0.001, HR=2.3, etc.
7. Return entity spans with confidence scores`,
        sequence: `Orchestrator->>Agent2: full_paper_text
Agent2->>BioBERT: Run NER model on text
BioBERT-->>Agent2: Raw entity predictions
Agent2->>Agent2: Post-process entities:
  - Normalize gene symbols
  - Standardize variant notation
  - Map to ontologies
Agent2->>PubTator: Validate gene mentions
PubTator-->>Agent2: Confirmed gene IDs
Agent2-->>Orchestrator: Tagged entities with positions`
      },
      {
        id: 'agent3',
        name: 'Study Design Classifier',
        model: 'gpt-4o',
        type: 'Classification',
        description: 'Classifies study characteristics and determines evidence level foundation',
        inputs: ['Full paper', 'Methods section', 'Abstract'],
        outputs: ['Clinical trial phase', 'Study design type', 'Sample size', 'Statistical methodology', 'Evidence level recommendation'],
        tools: ['Section-aware LM', 'Rule-based validators'],
        evaluation: 'Classification accuracy vs manual (90%+)',
        dependencies: [],
        instructions: `Classify study design to enable evidence_level determination:

PHASE CLASSIFICATION (if clinical trial):
- Phase I: Safety, dose-finding, small n (<30)
- Phase II: Efficacy signal, moderate n (30-100)
- Phase III: Definitive efficacy, large n (>100), often RCT
- Phase IV: Post-marketing

STUDY DESIGN:
- RCT: Randomized, controlled, parallel arms
- Cohort: Prospective/retrospective observational
- Case-Control: Compare cases to controls
- Case Study: 1-5 patients, no controls
- Preclinical: Cell lines, animal models, in vitro

SAMPLE SIZE:
- Extract n= from Methods/Results
- Distinguish total n vs variant-specific n
- Note: "178 NSCLC patients, 23 with EGFR L858R"

STATISTICAL METHODS:
- Tests used (Fisher's, log-rank, Cox regression)
- Multiple comparison corrections
- Confidence intervals reported

EVIDENCE LEVEL MAPPING:
- Phase III RCT + proven → Level A
- Phase II or large cohort → Level B  
- Case studies (1-5 patients) → Level C
- Preclinical (cells/mice) → Level D
- Inferential/indirect → Level E`,
        sequence: `Orchestrator->>Agent3: paper_sections
Agent3->>Agent3: Parse Methods for study design keywords
Agent3->>Agent3: Extract sample size from Methods/Abstract
Agent3->>Agent3: Identify statistical tests
Agent3->>Agent3: Classification decision tree:
  Is RCT? → Check phase
  Is Phase III? → Likely Level A/B
  Is preclinical? → Level D
  Is case study? → Level C
Agent3-->>Orchestrator: Study characteristics + evidence_level hint`
      }
    ],
    phase2: [
      {
        id: 'agent4',
        name: 'Evidence Type Classifier',
        model: 'o4-mini (reasoning)',
        type: 'Classification',
        description: 'CRITICAL: Determines evidence_type which constrains all downstream fields',
        inputs: ['Full paper', 'Entity tags (Agent 2)', 'Study design (Agent 3)'],
        outputs: ['evidence_type: Predictive/Prognostic/Diagnostic/Predisposing/Oncogenic/Functional'],
        tools: ['file_search (CIViC dictionary)', 'Fine-tuned classifier'],
        evaluation: 'Multi-class accuracy 85%+, per-class F1',
        dependencies: ['Agent 2', 'Agent 3'],
        instructions: `CRITICAL DECISION POINT - This determines all downstream field requirements

Query CIViC dictionary via file_search for evidence_type definitions:
- file_search: "What is Predictive evidence type?"
- file_search: "Difference between Prognostic and Predictive"

DECISION TREE:
1. Is therapy/drug mentioned AND outcome measured?
   YES → Likely PREDICTIVE
   - Check: Does variant predict response to specific therapy?
   - Look for: response rates, PFS with drug, resistance to treatment

2. Is survival/outcome measured WITHOUT specific therapy context?
   YES → Likely PROGNOSTIC
   - Check: Does variant correlate with overall survival, DFS?
   - Look for: "independent of treatment", "across all therapies"

3. Is variant used to classify disease/subtype?
   YES → Likely DIAGNOSTIC
   - Check: Does variant define disease entity?
   - Example: BCR-ABL for CML, IDH for glioma subtype

4. Is germline variant AND cancer susceptibility discussed?
   YES → Likely PREDISPOSING
   - Check: Segregation analysis, familial cases
   - Look for: penetrance, carrier frequency

5. Is somatic variant AND tumor pathogenesis focus?
   YES → Likely ONCOGENIC
   - Check: Hallmarks of cancer evidence
   - Look for: transformation assays, focus formation

6. Is functional assay WITHOUT disease context?
   YES → Likely FUNCTIONAL
   - Check: In vitro activity, protein function
   - Look for: kinase activity, binding affinity

REASONING TRACE:
Log detailed justification for classification:
"Found dabrafenib mentioned in Methods (drug entity)
Found response rate outcome in Results (efficacy measure)
Found BRAF V600E variant (molecular entity)
Relationship: V600E → dabrafenib response
Conclusion: PREDICTIVE evidence type
Confidence: 0.95"`,
        sequence: `Orchestrator->>Agent4: {paper, entity_tags, study_design}
Agent4->>file_search: Query "evidence_type Predictive definition"
file_search-->>Agent4: Retrieved definition
Agent4->>Agent4: Reasoning steps:
  1. Check for therapy mentions → Found "dabrafenib"
  2. Check for outcome measures → Found "response rate 68%"
  3. Check relationship → V600E predicts dabrafenib response
  4. Classification: PREDICTIVE
Agent4->>Traces: Log reasoning chain
Agent4-->>Orchestrator: evidence_type="Predictive" (confidence=0.95)`
      },
      {
        id: 'agent5',
        name: 'Evidence Level Determiner',
        model: 'gpt-4o-mini (rule-based)',
        type: 'Classification',
        description: 'Assigns evidence_level (A/B/C/D/E) based on study characteristics',
        inputs: ['Study design (Agent 3)', 'Evidence type (Agent 4)'],
        outputs: ['evidence_level: A/B/C/D/E'],
        tools: ['file_search (CIViC dictionary)', 'Rule engine'],
        evaluation: 'Classification accuracy 90%+',
        dependencies: ['Agent 3', 'Agent 4'],
        instructions: `Apply CIViC evidence_level rules:

Query file_search: "What are criteria for evidence_level A?"

LEVEL A - Validated Association (10 points):
Rules:
- Phase III clinical trial OR
- FDA-approved companion diagnostic OR
- In professional guidelines (NCCN, WHO) OR
- Multiple independent confirmations
Examples:
- CLEOPATRA trial (HER2+ breast cancer)
- FDA approval for BRAF V600E + vemurafenib

LEVEL B - Clinical Evidence (5 points):
Rules:
- Phase I/II clinical trial with patient data OR
- Large observational study (n>50) with statistics OR
- Clear clinical outcomes measured
Examples:
- Phase II trial, 37 HER2+ CRC patients responding

LEVEL C - Case Study (3 points):
Rules:
- Individual case reports (1-5 patients) OR
- Small case series without controls OR
- Published clinical observation
Examples:
- Single patient with FLT3 overexpression responding to sunitinib

LEVEL D - Preclinical Evidence (1 point):
Rules:
- In vivo or in vitro models OR
- Cell line studies, mouse xenografts OR
- Molecular assays, binding studies
Examples:
- 49 BRAF-mutant melanoma cell lines responding to drug combo

LEVEL E - Inferential Association (0.5 points):
Rules:
- Indirect evidence, ≥1 step removed OR
- Suggests mechanism without direct proof OR
- Correlative observations
Examples:
- "CD33 expression increased in NPM1-mutant AML, suggesting anti-CD33 may work"

DECISION LOGIC:
IF study_design == "Phase III RCT" AND proven_therapy:
    RETURN Level_A
ELIF study_design == "Phase II" OR (study_design == "Cohort" AND n > 50):
    RETURN Level_B
ELIF study_design == "Case Study" AND n <= 5:
    RETURN Level_C
ELIF study_design == "Preclinical":
    RETURN Level_D
ELSE:
    RETURN Level_E`,
        sequence: `Orchestrator->>Agent5: {study_design, evidence_type}
Agent5->>file_search: Query "evidence_level criteria"
file_search-->>Agent5: Retrieved criteria definitions
Agent5->>Agent5: Apply rule engine:
  study_design="Phase III RCT"
  sample_size=178
  therapy_approval="FDA-approved"
  → Level A
Agent5-->>Orchestrator: evidence_level="A"`
      }
    ],
    phase3: [
      {
        id: 'agent6',
        name: 'Disease Mapper',
        model: 'gpt-4o',
        type: 'Ontology Mapping',
        description: 'Maps disease mentions to Disease Ontology with specificity',
        inputs: ['Disease mentions (Agent 2)', 'Paper context'],
        outputs: ['disease_name', 'disease_doid', 'disease_display_name'],
        tools: ['Disease Ontology API', 'BioPortal', 'Fuzzy matching'],
        evaluation: 'Mapping accuracy 85%+, specificity score',
        dependencies: ['Agent 2'],
        instructions: `Map disease to Disease Ontology (DO):

EXTRACTION:
1. Get disease mentions from Agent 2 entity tags
2. Extract additional context:
   - Disease stage if mentioned
   - Histological subtype
   - Molecular subtype (e.g., "ER+ breast cancer")

DISAMBIGUATION:
- "AML" → "acute myeloid leukemia" (not "amyotrophic lateral sclerosis")
- Context clues: mentions of chemotherapy, blast cells → cancer interpretation
- Cross-reference with other entities (genes/variants typical of that cancer)

SPECIFICITY SELECTION:
Prefer most specific applicable DO term:
- "Lung adenocarcinoma" (DOID:3910) preferred over
- "Lung carcinoma" (DOID:3905) preferred over  
- "Lung cancer" (DOID:1324)

MAPPING PROCESS:
1. Extract candidate disease strings from text
2. Normalize: lowercase, remove punctuation
3. Query Disease Ontology API:
   - Exact match first
   - Fuzzy match if no exact (Levenshtein distance)
   - Synonym matching
4. Verify specificity: Is this the most specific term that applies?
5. Check hierarchy: Is this term too broad?

VALIDATION:
- Ensure DOID exists and is not deprecated
- Check that DO term aligns with paper's cancer focus
- If paper discusses multiple diseases, select PRIMARY disease

RETURN:
{
  "disease_name": "Acute myeloid leukemia",
  "disease_doid": "DOID:9119",
  "disease_display_name": "Acute myeloid leukemia",
  "confidence": 0.95
}`,
        sequence: `Orchestrator->>Agent6: disease_mentions=["melanoma"]
Agent6->>DO API: Search "melanoma"
DO API-->>Agent6: Multiple results:
  - "Melanoma" (DOID:1909)
  - "Cutaneous melanoma" (DOID:8923)
  - "Uveal melanoma" (DOID:1752)
Agent6->>Agent6: Check paper context for specificity
Agent6->>Agent6: Decision: Generic "melanoma" most appropriate
Agent6-->>Orchestrator: {
  disease_name: "Melanoma",
  disease_doid: "DOID:1909"
}`
      },
      {
        id: 'agent7',
        name: 'Variant Origin Classifier',
        model: 'gpt-4o-mini',
        type: 'Classification',
        description: 'Determines variant_origin (Somatic/Germline/etc)',
        inputs: ['Variant mentions (Agent 2)', 'Methods section', 'Patient population'],
        outputs: ['variant_origin: Somatic/Rare Germline/Common Germline/Unknown/N/A'],
        tools: ['Context classifier', 'gnomAD API (for germline frequency)'],
        evaluation: 'Classification accuracy 80%+',
        dependencies: ['Agent 2'],
        instructions: `Classify variant origin:

CONTEXTUAL CLUES:

SOMATIC INDICATORS:
- "Tumor sequencing"
- "Somatic mutation"
- "Acquired mutation"
- "Driver mutation"
- Hotspot mutations (BRAF V600E, KRAS G12)
- Methods: tumor-only sequencing
- Frequency: variant NOT in gnomAD (or <0.01%)

GERMLINE INDICATORS:
- "Inherited mutation"
- "Germline variant"
- "Constitutional"
- "Familial"
- Methods: blood/normal tissue sequencing
- Segregation analysis mentioned
- ACMG/AMP classification mentioned

FREQUENCY CHECK (if germline):
Query gnomAD via API for population frequency:
- If variant NOT in gnomAD → Somatic OR Rare Germline
- If freq < 0.01 (1%) → Rare Germline
- If freq ≥ 0.01 → Common Germline

SPECIAL CASES:
- Expression variants (ERBB2 Overexpression) → N/A
- Fusions (usually somatic unless hereditary syndrome)

DECISION TREE:
1. Check Methods for sequencing approach:
   - Tumor-only → Likely Somatic
   - Matched tumor-normal → Check if found in normal
   - Blood/saliva → Germline

2. Check variant type:
   - Hotspot mutation (V600E, L858R) → Somatic
   - Nonsense in tumor suppressor → Could be either

3. Query gnomAD:
   - If found with freq ≥ 0.01 → Common Germline
   - If found with freq < 0.01 → Rare Germline
   - If not found → Likely Somatic (or very rare germline)

4. Check evidence_type:
   - Predisposing type → Definitely Germline
   - Oncogenic type → Likely Somatic

DEFAULT LOGIC:
IF evidence_type == "Predisposing":
    RETURN Rare_Germline OR Common_Germline (based on frequency)
ELIF hotspot_mutation AND cancer_context:
    RETURN Somatic
ELIF expression_variant:
    RETURN N_A
ELSE:
    RETURN Unknown (flag for human review)`,
        sequence: `Orchestrator->>Agent7: {variant="BRAF V600E", methods_section}
Agent7->>Agent7: Parse methods for sequencing:
  Found: "Tumor tissue sequencing"
  No matched normal mentioned
Agent7->>Agent7: Check variant type:
  V600E is known hotspot mutation
Agent7->>gnomAD API: Query "BRAF V600E" frequency
gnomAD API-->>Agent7: Not found in population
Agent7->>Agent7: Decision logic:
  Tumor sequencing + Hotspot + Not in gnomAD
  → Classification: Somatic
Agent7-->>Orchestrator: variant_origin="Somatic"`
      },
      {
        id: 'agent8',
        name: 'Direction & Significance Interpreter',
        model: 'o4-mini (reasoning)',
        type: 'Interpretation',
        description: 'HARDEST: Interprets evidence_direction and evidence_significance',
        inputs: ['Evidence type (Agent 4)', 'Variant (Agent 2)', 'Results section', 'Statistics'],
        outputs: ['evidence_direction: Supports/Does Not Support', 'evidence_significance (type-dependent)'],
        tools: ['file_search (CIViC dictionary)', 'Multi-step reasoning'],
        evaluation: 'Agreement with experts (kappa 0.75+)',
        dependencies: ['Agent 2', 'Agent 4'],
        instructions: `MOST COMPLEX INTERPRETATION TASK

Query file_search for evidence_significance options:
"What are significance values for Predictive evidence type?"

STEP 1: Get allowed significance values based on evidence_type

IF evidence_type == "Predictive":
  significance_options = [
    "Sensitivity/Response",
    "Resistance", 
    "Adverse Response",
    "Reduced Sensitivity",
    "N/A"
  ]

ELIF evidence_type == "Prognostic":
  significance_options = [
    "Better Outcome",
    "Poor Outcome",
    "N/A"
  ]

ELIF evidence_type == "Diagnostic":
  significance_options = [
    "Positive",
    "Negative"
  ]

... (continue for Predisposing, Oncogenic, Functional)

STEP 2: Parse Results section for outcome information

FOR PREDICTIVE:
Look for:
- Response rates: "ORR 68%", "CR in 23/37 patients"
- PFS/OS: "median PFS 11.3 vs 4.2 months"
- Resistance phrases: "acquired resistance", "no response"
- Adverse events: "grade 3-4 toxicity in 45%"

FOR PROGNOSTIC:
Look for:
- Survival outcomes: "OS HR=2.3 (p<0.001)"
- "Independent prognostic factor"
- "Associated with poor survival"

STEP 3: Determine DIRECTION (hardest part)

SUPPORTS + Sensitivity:
- Study SHOWS variant predicts response
- Example: "BRAF V600E patients responded to dabrafenib (ORR 68%)"

DOES NOT SUPPORT + Sensitivity:
- Study REFUTES previous sensitivity claims OR shows no response
- Example: "Despite BRAF V600E, no response to vemurafenib observed"
- NOTE: This is NOT the same as resistance (no active mechanism)

SUPPORTS + Resistance:
- Study SHOWS variant predicts lack of response with active mechanism
- Example: "EGFR T790M conferred resistance to gefitinib"

DOES NOT SUPPORT + Resistance:
- Study REFUTES previous resistance claims
- Example: "EGFR T790M patients still responded when treated with osimertinib"

KEY DISTINCTIONS:
- "Does Not Support Sensitivity" ≠ "Supports Resistance"
- Former = absence of effect (no evidence for sensitivity)
- Latter = active resistance mechanism demonstrated

STEP 4: REASONING CHAIN

Example reasoning:
"Analyzing Results section:
- Found: '178 NSCLC patients with BRAF V600E'
- Found: 'ORR to dabrafenib: 68% (p<0.001)'
- Found: 'Median PFS: 11.3 months vs 4.2 in control'
- Statistical significance: p<0.001

Interpretation:
- Variant: BRAF V600E
- Therapy: Dabrafenib
- Outcome: Positive response (68% ORR, prolonged PFS)
- Study shows V600E PREDICTS response to dabrafenib

Classification:
- evidence_direction = Supports
- evidence_significance = Sensitivity/Response

Confidence: 0.95 (clear response rate data)"

STEP 5: Handle ambiguous cases

IF outcome unclear:
  - Flag for human review
  - Return confidence < 0.7

IF multiple outcomes:
  - Focus on primary endpoint
  - Note secondary findings in comments

IF contradictory to literature:
  - Still code what THIS study shows
  - Mention controversy in evidence_description`,
        sequence: `Orchestrator->>Agent8: {evidence_type, variant, results, stats}
Agent8->>file_search: "Predictive evidence significance options"
file_search-->>Agent8: Retrieved: Sensitivity/Response, Resistance...

Agent8->>Agent8: Multi-step reasoning:
Step 1: Parse results section
  - Extract outcome: "ORR 68%"
  - Extract comparison: "vs 12% in wild-type"
  - Extract statistics: "p<0.001"

Step 2: Interpret outcome
  - 68% ORR indicates strong response
  - Statistically significant difference
  - Comparison shows variant-specific effect

Step 3: Classify significance
  - Response observed → Sensitivity/Response

Step 4: Determine direction  
  - Study SUPPORTS sensitivity claim
  - Not refuting anything
  
Agent8->>Traces: Log complete reasoning chain

Agent8-->>Orchestrator: {
  evidence_direction: "Supports",
  evidence_significance: "Sensitivity/Response",
  reasoning: "...",
  confidence: 0.95
}`
      },
      {
        id: 'agent9',
        name: 'Evidence Statement Generator',
        model: 'gpt-4o (abstractive)',
        type: 'Generation',
        description: 'Generates evidence_description (clinical summary)',
        inputs: ['All previous agent outputs', 'Results section', 'Methods'],
        outputs: ['evidence_description (paraphrased clinical statement)'],
        tools: ['Abstractive summarization', 'Plagiarism detection'],
        evaluation: 'Expert scoring 70%+, ROUGE-L, coverage checklist',
        dependencies: ['All previous agents'],
        instructions: `Generate high-quality evidence_description:

REQUIREMENTS:
1. Must include: molecular profile, disease, sample size, statistics, outcome
2. Must NOT include: PHI, direct quotes (plagiarism), speculation
3. Must paraphrase source material in your own words
4. Must be concise but complete (2-4 sentences typical)

STRUCTURE TEMPLATE:
"In [study description] of [n] [disease] patients/samples, [molecular profile] was [associated with/predicted] [outcome] [with therapy if Predictive]. [Key statistics: p-value, HR, ORR, etc.]"

EXAMPLES BY EVIDENCE TYPE:

PREDICTIVE:
"In this Phase III trial of 178 non-small cell lung cancer patients with BRAF V600E mutations, treatment with dabrafenib resulted in an overall response rate of 68% (p<0.001) and median progression-free survival of 11.3 months compared to 4.2 months in historical controls."

PROGNOSTIC:
"In a retrospective cohort of 245 chronic lymphocytic leukemia patients, TP53 mutations were associated with significantly worse overall survival (HR=2.3, 95% CI 1.5-3.4, p<0.001) independent of treatment received."

DIAGNOSTIC:
"In this study of 89 acute myeloid leukemia samples, NPM1 mutations were present in 35% of cytogenetically normal AML cases and were highly specific for this AML subtype (sensitivity 87%, specificity 96%)."

PREDISPOSING:
"In a family with Von Hippel-Lindau disease, the VHL R167Q variant segregated with disease phenotype across three generations (LOD score 3.2), supporting pathogenic classification per ACMG criteria PP1."

ONCOGENIC:
"In focus formation assays using CDKN2A-deficient cells, the CDKN2A D108Y variant failed to suppress cell proliferation or restore cell cycle arrest, demonstrating loss of tumor suppressor function (p<0.01 vs wild-type)."

FUNCTIONAL:
"In vitro kinase assays demonstrated that BRAF V600E exhibits constitutive kinase activity independent of RAS activation, with 500-fold increased MEK phosphorylation compared to wild-type BRAF."

WRITING GUIDELINES:
1. Front-load most important info (molecular profile, disease)
2. Specify study population characteristics when relevant
   - "178 NSCLC patients" not just "patients"
   - "49 BRAF-mutant melanoma cell lines" not just "cell lines"
3. Include statistical support
   - p-values, confidence intervals, hazard ratios
   - Sample sizes for categorical outcomes (23/37 patients)
4. Specify therapies by name if Predictive
   - "gefitinib" not "EGFR inhibitor" (unless multiple similar drugs)
5. Indicate disease stage when relevant
   - "metastatic melanoma" vs "early-stage melanoma"
6. Distinguish somatic vs germline context when important
7. For categorical variants, state if individual variant details available
   - "In 23 of 178 patients with various EGFR exon 19 deletions..."

AVOID:
- PHI: Names, dates, medical record numbers
- Plagiarism: Direct quotes or close paraphrasing from abstract
- Speculation: "May suggest", "could indicate" (stick to what's shown)
- Jargon: Write for general scientific audience
- Vagueness: "Study showed response" (specify: 68% ORR)

PLAGIARISM CHECK:
After generating statement:
1. Compare to source abstract sentence-by-sentence
2. Flag any >5 word exact matches
3. If detected, regenerate with different phrasing
4. Never copy phrases verbatim, even with citations`,
        sequence: `Orchestrator->>Agent9: {all_extracted_fields, results_section}
Agent9->>Agent9: Generate draft statement:
  "In this Phase III trial of 178 NSCLC patients..."
  
Agent9->>PlagiarismCheck: Compare to source abstract
PlagiarismCheck-->>Agent9: No matches >5 words

Agent9->>Agent9: Quality checks:
  ✓ Includes sample size
  ✓ Includes statistics  
  ✓ Includes outcome
  ✓ Paraphrased (not copied)
  ✓ No PHI
  
Agent9->>file_search: "Best practices for evidence_description"
file_search-->>Agent9: Retrieved guidelines

Agent9->>Agent9: Finalize statement

Agent9-->>Orchestrator: evidence_description="In this Phase III..."`
      }
    ],
    phase4: [
      {
        id: 'agent10',
        name: 'Variant Standardizer',
        model: 'gpt-4o-mini',
        type: 'Normalization',
        description: 'Standardizes variant names to CIViC format',
        inputs: ['Variant mentions (Agent 2)', 'Gene context'],
        outputs: ['variant_names (canonical CIViC format)', 'variant_aliases'],
        tools: ['Regex patterns', 'HGVS validator', 'CIViC variant search'],
        evaluation: 'Naming consistency 90%+, alias coverage',
        dependencies: ['Agent 2'],
        instructions: `Standardize variant nomenclature:

NORMALIZATION RULES:

1. AMINO ACID CHANGES:
Standard format: Single-letter code + position + new amino acid
- "V600E" ✓
- "Val600Glu" → "V600E"
- "V600→E" → "V600E"
- "p.Val600Glu" → "V600E" (remove p. prefix for variant name)

2. FRAMESHIFTS:
Short form preferred:
- "W288fs" ✓
- "W288Afs*46" → Add to aliases, use "W288fs" as primary
- "p.Trp288Argfs*46" → "W288fs"

3. DELETIONS:
- "Del I843" ✓
- "E746_T751del" ✓
- "Exon 19 Deletion" ✓ (when specific bases unknown)

4. INSERTIONS:
- "P780ins" ✓
- "M774insAYVM" ✓

5. FUSIONS:
Format: GENE1-GENE2 (5' to 3', hyphen separator)
- "BCR-ABL1" ✓
- "EML4-ALK" ✓
- "BCR/ABL" → "BCR-ABL1"

6. EXPRESSION:
- "Overexpression" ✓
- "Expression" ✓
- "Amplification" ✓

7. CATEGORICAL:
- "Mutation" ✓ (when specific change unknown)
- "Exon 12 Mutation" ✓
- "V600" ✓ (position without specifying amino acid)

TITLE CASE:
Use Title Case for category terms:
- "Exon 19 Deletion" not "exon 19 deletion"
- "Kinase Domain Mutation"

GENERATE ALIASES:
Common alternative names to include:
- 3-letter amino acid codes: "Val600Glu"
- Full HGVS: "p.Val600Glu"
- dbSNP ID: "rs121913227" (if known/common)
- COSMIC ID: "COSM476" (if known/common)
- Legacy names: "NPM1-A" for NPM1 W288fs
- Alternate numbering: "D769Y" (different transcript)

CHECK EXISTING CIViC VARIANTS:
Query CIViC API: Is this variant already in CIViC?
If yes: Use existing variant_id and canonical name
If no: Flag as new variant to be created

VALIDATION:
- Verify amino acid codes are valid (20 standard + stop)
- Check position is reasonable for gene length
- Ensure fusion genes are in correct 5'→3' order`,
        sequence: `Orchestrator->>Agent10: variant_mention="Val600Glu in BRAF"
Agent10->>Agent10: Normalize notation:
  "Val600Glu" → "V600E"
  
Agent10->>Agent10: Generate aliases:
  - "Val600Glu"
  - "V600E"
  - "p.Val600Glu"
  - "BRAF V600E"
  
Agent10->>CIViC API: Search existing variants: "BRAF V600E"
CIViC API-->>Agent10: Found: variant_id=12, name="BRAF V600E"

Agent10-->>Orchestrator: {
  variant_names: "BRAF V600E",
  variant_ids: "12",
  variant_aliases: ["Val600Glu", "p.Val600Glu"],
  existing_variant: true
}`
      },
      {
        id: 'agent11',
        name: 'Molecular Profile Classifier',
        model: 'gpt-4o',
        type: 'Classification',
        description: 'Determines if simple or complex molecular profile',
        inputs: ['Standardized variants (Agent 10)', 'Paper context'],
        outputs: ['molecular_profile_name', 'molecular_profile_is_complex', 'Boolean logic'],
        tools: ['Dependency parser', 'Logical structure analyzer'],
        evaluation: 'MP structure accuracy 85%+',
        dependencies: ['Agent 10'],
        instructions: `Classify Molecular Profile complexity:

DECISION LOGIC:

SIMPLE MP (is_complex=false):
ONE variant mentioned in isolation:
- "BRAF V600E" → Simple MP
- "EGFR L858R" → Simple MP
- "NPM1 Mutation" (categorical) → Simple MP

COMPLEX MP (is_complex=true):
MULTIPLE variants with explicit relationship:

AND relationship:
- "EGFR L858R AND EGFR T790M" (double mutant)
- "MYC Rearrangement AND BCL2 Rearrangement" (double-hit lymphoma)
- Must be studied TOGETHER as combination

OR relationship:
- "KRAS G12C OR KRAS G12V" (either variant)
- "Erlotinib OR Gefitinib" (substitute therapies)
- Evidence applies to ANY of the variants

NOT relationship:
- "BRAF V600E AND NOT NRAS Mutation" (exclusion criteria)
- "PDL1 Expression AND NOT (EGFR Mutation OR ALK Fusion)"

DETECTION STRATEGY:
1. Check if multiple variants mentioned
2. Look for explicit conjunction words: "and", "or", "in combination with"
3. Check Methods: "Patients with both L858R and T790M"
4. Check Results: Are outcomes reported for combination specifically?

AMBIGUOUS CASES:

Multiple variants studied separately → Multiple simple MPs:
"We analyzed L858R and L747_P753delinsS separately..."
→ Create 2 simple MPs, not 1 complex MP

Multiple variants where relationship unclear:
"Paper mentions V600E and also mentions T790M but not together"
→ Default to simple MPs unless evidence they were studied together

NAMING COMPLEX MPs:
Follow Boolean logic order:
1. NOT (highest precedence)
2. AND 
3. OR (lowest precedence)

Use parentheses for grouping:
"MYC Rearrangement AND (BCL2 Rearrangement OR BCL6 Rearrangement)"

VALIDATION:
- All component variants must exist in CIViC first
- Boolean logic must be valid
- Check that complexity is justified by paper content`,
        sequence: `Orchestrator->>Agent11: {variants: ["EGFR L858R", "EGFR T790M"]}
Agent11->>Agent11: Check paper for relationship:
  Methods: "Patients with acquired T790M resistance..."
  Results: "Double mutants (L858R + T790M) showed resistance"
  
Agent11->>Agent11: Decision: Complex MP (studied together)
  
Agent11->>Agent11: Construct MP name:
  "EGFR L858R AND EGFR T790M"
  
Agent11-->>Orchestrator: {
  molecular_profile_name: "EGFR L858R AND EGFR T790M",
  molecular_profile_is_complex: true,
  is_multi_variant: true,
  variants: ["EGFR L858R", "EGFR T790M"]
}`
      },
      {
        id: 'agent12',
        name: 'Variant Type Annotator',
        model: 'gpt-4o-mini',
        type: 'Ontology Mapping',
        description: 'Maps to Sequence Ontology terms',
        inputs: ['Variant names (Agent 10)', 'Molecular profile (Agent 11)'],
        outputs: ['variant_type_names', 'variant_type_soids', 'variant_type_descriptions'],
        tools: ['Sequence Ontology API', 'Pattern matching'],
        evaluation: 'SO term accuracy 90%+',
        dependencies: ['Agent 10', 'Agent 11'],
        instructions: `Map to Sequence Ontology (SO) terms:

CLASSIFICATION LOGIC:

1. SINGLE NUCLEOTIDE CHANGES:

MISSENSE (SO:0001583):
- Amino acid change, length preserved
- Examples: V600E, L858R
- "A sequence variant that changes one or more bases, resulting in a different amino acid sequence but where the length is preserved"

NONSENSE / Stop Gained (SO:0001587):
- Premature stop codon
- Examples: Q61*, R213*
- "A sequence variant whereby at least one base of a codon is changed, resulting in a premature stop codon"

SYNONYMOUS (SO:0001819):
- No amino acid change
- Silent mutation
- Less common in CIViC (usually non-functional)

2. INDELS:

FRAMESHIFT (SO:0001589):
- Insertion/deletion not multiple of 3
- Disrupts reading frame
- Examples: W288fs, P86fs
- "A sequence variant which causes a disruption of the translational reading frame"

IN-FRAME INSERTION (SO:0001821):
- Insertion multiple of 3
- Examples: M774insAYVM
- No frameshift

IN-FRAME DELETION (SO:0001822):
- Deletion multiple of 3
- Examples: E746_T751del (Exon 19 del)
- No frameshift

3. STRUCTURAL:

TRANSCRIPT FUSION (SO:0001886):
- Gene fusion events
- Examples: BCR-ABL1, EML4-ALK
- "A feature fusion where the deletion brings together transcript regions"

TRANSCRIPT AMPLIFICATION (SO:0001889):
- Copy number increase
- Examples: ERBB2 Amplification, MYC Amplification

TRANSCRIPT ABLATION (SO:0001893):
- Deletion of transcript
- Examples: Homozygous deletion

4. FUNCTIONAL:

EXON VARIANT (SO:0001791):
- Variant within exon (may be general term)
- Examples: Exon 19 Deletion (specific exon)

SPLICE DONOR/ACCEPTOR (SO:0001575, SO:0001574):
- Affects splicing sites
- Examples: IVS14+1G>A

5. REGIONAL:

For categorical variants like "Exon 12 Mutation":
Use broader term: "Exon Variant" (SO:0001791)

MOST SPECIFIC TERM:
Always choose most specific applicable term:
- "Missense Variant" preferred over "Sequence Variant"
- "Conservative Missense" preferred over "Missense" (if conservative)

MULTIPLE TYPES:
Can assign >1 type if variant has multiple effects:
- "Loss of Function Variant" AND "Nonsense"

AVOID REDUNDANCY:
Don't select both parent and child:
- DON'T: "Sequence Variant" AND "Missense Variant"
- DO: Just "Missense Variant"

SPECIAL CASES:

Expression variants:
- Often no specific SO term applicable
- May use "N/A" or very general term

Categorical variants:
- Use broadest applicable: "Protein Altering Variant"

QUERY SO API:
For each variant:
1. Classify variant type by inspection
2. Query SO API for corresponding term
3. Verify definition matches
4. Get SO ID and description
5. Return structured annotation`,
        sequence: `Orchestrator->>Agent12: {variant="BRAF V600E"}
Agent12->>Agent12: Classify variant:
  V600E = single amino acid change
  Length preserved
  → Missense Variant
  
Agent12->>SO API: Query "Missense Variant"
SO API-->>Agent12: {
  term: "Missense Variant",
  id: "SO:0001583",
  definition: "A sequence variant that changes..."
}

Agent12-->>Orchestrator: {
  variant_type_names: ["Missense Variant"],
  variant_type_soids: ["SO:0001583"],
  variant_type_descriptions: ["A sequence variant that changes one or more bases, resulting in a different amino acid sequence but where the length is preserved"]
}`
      },
      {
        id: 'agent13',
        name: 'Coordinate Extractor',
        model: 'o4-mini (reasoning) + External APIs',
        type: 'Extraction + Lookup',
        description: 'COMPLEX: Extracts/infers genomic coordinates',
        inputs: ['Variant names (Agent 10)', 'Methods section', 'Supplementary tables'],
        outputs: ['chromosome', 'start_position', 'stop_position', 'reference_bases', 'variant_bases', 'reference_build', 'representative_transcript'],
        tools: ['Text extraction', 'ClinGen Allele Registry', 'ClinVar API', 'COSMIC', 'Ensembl API', 'LiftOver'],
        evaluation: 'Coordinate accuracy 60%+ (often not in paper)',
        dependencies: ['Agent 10'],
        instructions: `Extract or lookup genomic coordinates:

CHALLENGE: Coordinates often NOT explicitly stated in paper

STRATEGY 1: Direct extraction from paper
Check for coordinate mentions in:
- Methods: "chr7:140453136A>T (GRCh37)"
- Supplementary tables
- Figure legends

STRATEGY 2: External database lookup (most common)

FOR WELL-KNOWN VARIANTS:
1. Query ClinVar API:
   - Search by gene + variant name
   - Example: "BRAF V600E"
   - Returns: chromosome, position, ref, alt, build

2. Query ClinGen Allele Registry:
   - Search by gene + HGVS expression
   - Returns: CA ID + coordinates in multiple builds
   - Preferred source (canonical allele representation)

3. Query COSMIC:
   - Search by gene + variant
   - Returns: coordinates, allele frequencies

FOR NOVEL/RARE VARIANTS:
May need to:
- Infer from protein change using Ensembl API
- Look up transcript coordinates
- Calculate genomic position from transcript position
- Flag as "coordinates not confirmed"

COORDINATE SYSTEM:
- 1-based (not 0-based)
- Left-shifted for indels
- Inclusive start and stop

REFERENCE BUILD:
- Prefer GRCh37 (CIViC standard)
- If only GRCh38 available: use LiftOver to convert
- Always specify build explicitly

REPRESENTATIVE TRANSCRIPT:
Selection criteria (in priority order):
1. MANE Select transcript (if available)
   - Query: "What is MANE Select for BRAF?"
   - Source: NCBI Gene page, Ensembl
2. Ensembl canonical transcript (marked ***)
3. Longest ORF
4. Most exons
5. Widely used in literature

Transcript format: "ENST00000646891.2" (include version)

FOR SNVs:
- start_position = stop_position (single base)
- reference_bases = "C"
- variant_bases = "T"

FOR DELETIONS:
- start_position = first deleted base
- stop_position = last deleted base
- reference_bases = "ACGT" (deleted sequence)
- variant_bases = "" or "-"

FOR INSERTIONS:
- start_position = base before insertion
- stop_position = base after insertion
- reference_bases = "" or "-"
- variant_bases = "GG" (inserted sequence)

FOR FUSIONS:
Need TWO coordinate sets:
- Primary: 5' partner breakpoint
- Secondary: 3' partner breakpoint
Each with: chr, start, stop, transcript

VALIDATION:
- Verify coordinates match reference genome
- Check HGVS expression is consistent
- Ensure build is specified
- Verify transcript contains variant

FALLBACK:
If coordinates cannot be determined:
- Flag field as "Not available in source"
- Set confidence = low
- Suggest manual curation`,
        sequence: `Orchestrator->>Agent13: {variant="BRAF V600E"}
Agent13->>Agent13: Check paper for explicit coordinates:
  Methods section: No coordinates mentioned
  Supplementary: No tables
  
Agent13->>Agent13: Strategy: External lookup

Agent13->>ClinVar API: Search "BRAF V600E"
ClinVar API-->>Agent13: {
  variant_id: 13961,
  chr: "7",
  position: 140453136,
  ref: "A",
  alt: "T",
  build: "GRCh37"
}

Agent13->>ClinGen Allele Registry: Search "BRAF V600E"
ClinGen-->>Agent13: {
  ca_id: "CA123596",
  GRCh37: "7:140453136",
  GRCh38: "7:140753336",
  hgvs: ["NC_000007.13:g.140453136A>T"]
}

Agent13->>NCBI Gene: Query MANE Select for BRAF
NCBI-->>Agent13: MANE Select: ENST00000646891.2

Agent13->>Agent13: Assemble coordinates:
  chromosome: "7"
  start: 140453136
  stop: 140453136 (SNV)
  ref: "A"
  alt: "T"
  build: "GRCh37"
  transcript: "ENST00000646891.2"
  
Agent13-->>Orchestrator: Coordinate object with confidence=0.95`
      }
    ],
    phase5: [
      {
        id: 'agent14',
        name: 'Therapy Extractor',
        model: 'gpt-4o-mini',
        type: 'Extraction + Mapping',
        description: 'Extracts and maps therapies (IF Predictive evidence)',
        inputs: ['Drug mentions (Agent 2)', 'Methods/Results sections'],
        outputs: ['therapy_names', 'therapy_ncit_ids', 'therapy_interaction_type'],
        tools: ['NCIt API', 'RxNorm', 'Drug name normalization'],
        evaluation: 'Drug ID accuracy 85%+, NCIt mapping',
        dependencies: ['Agent 2', 'Agent 4'],
        conditional: 'Only if evidence_type=="Predictive"',
        instructions: `Extract and map therapies to NCIt:

CONDITIONAL EXECUTION:
IF evidence_type != "Predictive":
  SKIP this agent (return null)
  
EXTRACTION:
1. Get drug mentions from Agent 2 NER tags
2. Extract additional from Methods/Results:
   - Treatment regimens
   - Drug combinations
   - Dosing schedules (for context, not storage)

NORMALIZATION:
Prefer GENERIC names, not trade names:
- "imatinib" ✓ (not "Gleevec")
- "trastuzumab" ✓ (not "Herceptin")
- "erlotinib" ✓ (not "Tarceva")

HANDLE REGIMENS:
Named regimens acceptable:
- "FOLFOX" ✓ (5-FU + Leucovorin + Oxaliplatin)
- "R-CHOP" ✓
- Expand components in evidence_description if needed

MAPPING TO NCIt:
1. Query NCIt API with drug name
2. Verify it's a therapy (not disease or anatomy)
3. Get NCIt concept ID (C-code)
4. Examples:
   - imatinib → C1484
   - trastuzumab → C1647
   - tamoxifen → C62078

INTERACTION TYPE (if multiple drugs):
REQUIRED when ≥2 therapies

COMBINATION:
- Drugs given together/concurrently
- May be same day or alternating within cycle
- Examples:
  * "dabrafenib + trametinib"
  * "FOLFOX" (concurrent multi-drug)
  * "docetaxel + pertuzumab + trastuzumab"

SEQUENTIAL:
- Drugs given one after another
- Order matters
- Examples:
  * "erlotinib → osimertinib" (after resistance)
  * "induction → maintenance"

SUBSTITUTES:
- Interchangeable alternatives
- Patient receives ONE of these
- Examples:
  * "erlotinib OR gefitinib" (both EGFR TKIs)
  * "pembrolizumab OR nivolumab" (both anti-PD1)

DETERMINATION LOGIC:
Check paper for explicit language:
- "in combination with" → Combination
- "followed by" → Sequential
- "or alternatively" → Substitutes
- "versus" (comparing arms) → Typically SEPARATE evidence items

VALIDATION:
- All drugs must be in NCIt
- If not found: Flag for curator to add
- Interaction type must be justified by paper
- Cannot infer interaction from curator knowledge alone`,
        sequence: `Agent4-->>Agent14: evidence_type="Predictive" (proceed)

Orchestrator->>Agent14: {drug_mentions: ["dabrafenib", "trametinib"]}

Agent14->>Agent14: Normalize names:
  "Tafinlar" → "dabrafenib"
  "Mekinist" → "trametinib"
  
Agent14->>NCIt API: Search "dabrafenib"
NCIt API-->>Agent14: {
  concept_id: "C68398",
  preferred_name: "Dabrafenib",
  semantic_type: "Pharmacologic Substance"
}

Agent14->>NCIt API: Search "trametinib"
NCIt API-->>Agent14: {
  concept_id: "C77908",
  preferred_name: "Trametinib"
}

Agent14->>Agent14: Check paper for interaction:
  Methods: "Patients received dabrafenib 150mg twice daily 
           and trametinib 2mg once daily"
  → Concurrent administration → Combination
  
Agent14-->>Orchestrator: {
  therapy_names: ["Dabrafenib", "Trametinib"],
  therapy_ncit_ids: ["C68398", "C77908"],
  therapy_interaction_type: "Combination"
}`
      },
      {
        id: 'agent15',
        name: 'Phenotype Extractor',
        model: 'gpt-4o-mini',
        type: 'Extraction + Mapping',
        description: 'Extracts phenotypes (primarily for Predisposing evidence)',
        inputs: ['Phenotype mentions (Agent 2)', 'Patient descriptions'],
        outputs: ['phenotype_names', 'phenotype_hpo_ids'],
        tools: ['HPO API', 'Clinical text parser'],
        evaluation: 'HPO mapping accuracy 80%+',
        dependencies: ['Agent 2'],
        conditional: 'Primarily for Predisposing, but any type if phenotypes mentioned',
        instructions: `Extract and map phenotypes to HPO:

PRIMARY USE CASE:
Predisposing evidence describing cancer predisposition syndromes

EXTRACTION:
1. Get phenotype mentions from Agent 2 tags
2. Look for clinical descriptions in:
   - Patient characteristics
   - Family history
   - Associated conditions

EXAMPLES:
For Von Hippel-Lindau disease:
- "Pheochromocytoma" (HPO:0002666)
- "Renal cell carcinoma" (HPO:0005584)
- "Pancreatic cysts" (HPO:0001737)
- "Hemangioblastoma" (HPO:0009588)

For Lynch syndrome:
- "Colorectal carcinoma" (HPO:0003003)
- "Endometrial carcinoma" (HPO:0012114)

MAPPING TO HPO:
1. Query HPO API with phenotype text
2. Disambiguate (use disease context):
   - "AML" in cancer paper → "Acute myeloid leukemia"
3. Get HPO ID and preferred name
4. Verify specificity (most specific applicable term)

VALIDATION:
- Phenotype must be EXPLICITLY observed in study
- Must be associated with specific variant
- Not inferred from general knowledge
- Document in what context phenotype appears

CURATION RULE:
Only include phenotypes that are:
1. Directly observed in patients/families in paper
2. Associated with the specific variant being studied
3. Relevant to cancer/predisposition context

SKIP if:
- General disease description (that's disease field)
- Not variant-specific
- Inferred but not observed`,
        sequence: `Orchestrator->>Agent15: {phenotype_mentions: ["pheochromocytoma", "renal cysts"]}

Agent15->>Agent15: Check paper context:
  "Family with VHL R167Q showed pheochromocytoma 
   in 3 of 5 affected individuals and renal cysts 
   in all 5"
   
Agent15->>HPO API: Search "pheochromocytoma"
HPO API-->>Agent15: {
  hpo_id: "HP:0002666",
  name: "Pheochromocytoma"
}

Agent15->>HPO API: Search "renal cysts"  
HPO API-->>Agent15: {
  hpo_id: "HP:0000107",
  name: "Renal cyst"
}

Agent15-->>Orchestrator: {
  phenotype_names: ["Pheochromocytoma", "Renal cyst"],
  phenotype_hpo_ids: ["HP:0002666", "HP:0000107"]
}`
      }
    ],
    phase6: [
      {
        id: 'agent16',
        name: 'Evidence Rating Assessor',
        model: 'gpt-4o',
        type: 'Assessment',
        description: 'Assigns evidence_rating (1-5 stars) based on study quality',
        inputs: ['All evidence fields', 'Study design (Agent 3)', 'Sample size', 'Statistics'],
        outputs: ['evidence_rating: 1-5 stars'],
        tools: ['Multi-factor scoring', 'LLM judge'],
        evaluation: 'Rating agreement with experts (ICC 0.6+)',
        dependencies: ['All previous agents'],
        instructions: `Assess evidence quality and assign star rating:

RATING CRITERIA (1-5 stars):

★★★★★ (5 STARS) - Exceptionally Strong:
Requirements:
- Well-powered study (appropriate n for analysis)
- Statistically robust (p<0.05, CI reported)
- Respected journal/lab (high impact factor)
- Well-controlled experiments
- Clean, reproducible results
- Independent validation methods
- Minimal confounding factors

Examples:
- Phase III RCT in NEJM, n=343, double-blind
- Multi-institutional validation study
- Mechanistic validation in multiple models

★★★★ (4 STARS) - Strong:
Requirements:
- Well-supported evidence
- Appropriate sample size
- Good statistical support
- Minor limitations that don't undermine conclusions
- Credible methodology

Examples:
- Phase 2A trial, n=37, registered, clear endpoints
- JCO publication with standard methodology

★★★ (3 STARS) - Moderate:
Requirements:
- Convincing but not exhaustive
- Smaller scale or early-phase
- Novel results without extensive validation
- Some experimental limitations
- Appropriate for hypothesis-generating

Examples:
- Subset analysis, n=9 patients responding
- Pilot study with clear but limited data

★★ (2 STARS) - Weak:
Requirements:
- Limited experimental support
- Small sample without power
- Lack of proper controls
- Potential confounding
- Lower-impact publication
- Not independently validated

Examples:
- n=6 patients, heterogeneous methodology
- Underpowered comparison

★ (1 STAR) - Minimal:
Requirements:
- Claims poorly supported by data
- Very small n (1-2) or single unreplicated experiment
- Not reproducible or highly variable
- No validation
- Significant methodological concerns

Examples:
- Anecdotal observation
- Single experiment, no replicates

ASSESSMENT PROCESS:
1. Review study design (Agent 3 output)
2. Assess sample size adequacy:
   - For clinical: Is n sufficient for statistical power?
   - For preclinical: Are replicates adequate?
   - For categorical outcomes: Check numerator/denominator
3. Evaluate statistical rigor:
   - p-values reported and significant?
   - Confidence intervals provided?
   - Multiple comparison corrections if needed?
4. Consider publication venue:
   - High-impact journal (Nature, Science, NEJM, JCO)?
   - Respected specialty journal?
   - Conference abstract only?
5. Check experimental controls:
   - Appropriate comparators?
   - Blinding where applicable?
   - Confounding factors addressed?
6. Assess reproducibility:
   - Independent validation?
   - Multiple methods confirming finding?
   - Replication in different contexts?

IMPORTANT NOTES:
- Rate the SPECIFIC EVIDENCE extracted, not the whole paper
- High-quality paper may yield low-rated evidence if specific claim weakly supported
- Example: n=500 study but only 2 patients have variant → low rating
- Preclinical (Level D) CAN be 5-star if exceptionally rigorous
- Clinical (Level B) CAN be 1-star if poorly controlled

EDGE CASES:
- Large study, small variant subset → Rate based on subset
- Multiple findings in paper → Rate the specific claim being extracted
- Contradictory results → Lower rating, note in comments

CONFIDENCE:
Output rating with confidence score:
- 0.9+ if clear criteria met
- 0.7-0.9 if some ambiguity
- <0.7 flag for human review`,
        sequence: `Orchestrator->>Agent16: {all_fields, study_design, sample_size, stats}

Agent16->>Agent16: Assess quality factors:
  1. Study design: Phase III RCT
  2. Sample size: n=178 (adequate for analysis)
  3. Statistics: p<0.001, HR with CI reported
  4. Journal: NEJM (high impact)
  5. Controls: Randomized, controlled
  6. Reproducibility: Multiple sites

Agent16->>file_search: "Examples of 5-star evidence rating"
file_search-->>Agent16: Retrieved criteria

Agent16->>Agent16: Scoring matrix:
  Design: 5/5 (Phase III RCT)
  Sample: 5/5 (well-powered)
  Statistics: 5/5 (robust, CI reported)
  Journal: 5/5 (NEJM)
  Controls: 5/5 (double-blind RCT)
  Validation: 4/5 (multi-site but no independent study)
  
  Average: 4.8/5 → Round to 5 stars
  
Agent16->>Traces: Log rating justification

Agent16-->>Orchestrator: {
  evidence_rating: 5,
  confidence: 0.95,
  justification: "Phase III RCT with 178 patients..."
}`
      },
      {
        id: 'agent17',
        name: 'Cross-Field Validator',
        model: 'gpt-4o-mini (rule-based)',
        type: 'Validation',
        description: 'Validates consistency and completeness of all extracted fields',
        inputs: ['All extracted fields'],
        outputs: ['Validation passed/failed', 'List of errors', 'Confidence scores per field'],
        tools: ['Rule-based validator', 'External API checks'],
        evaluation: 'Error detection rate 95%+',
        dependencies: ['All previous agents'],
        instructions: `Validate extracted data for consistency and completeness:

VALIDATION CATEGORIES:

1. REQUIRED FIELDS CHECK:
Verify all required fields present based on evidence_type:

For ALL types:
- evidence_description ✓
- evidence_type ✓
- evidence_direction ✓
- evidence_significance ✓
- evidence_level ✓
- evidence_rating ✓
- disease (name, doid) ✓
- variant_origin ✓
- molecular_profile ✓
- source metadata ✓

For Predictive (additional):
- therapy_names ✓
- therapy_ncit_ids ✓
- therapy_interaction_type (if multiple therapies) ✓

2. EVIDENCE TYPE ↔ SIGNIFICANCE COMPATIBILITY:
Verify significance matches allowed values for type:

IF evidence_type == "Predictive":
  ALLOWED: [Sensitivity/Response, Resistance, Adverse Response, Reduced Sensitivity, N/A]
  REJECT: [Better Outcome, Poor Outcome, Positive, Negative, ...]

IF evidence_type == "Prognostic":
  ALLOWED: [Better Outcome, Poor Outcome, N/A]
  REJECT: [Sensitivity/Response, ...]

(Continue for all types)

3. COORDINATE VALIDITY:
IF coordinates present:
- start_position ≤ stop_position ✓
- chromosome in [1-22, X, Y, MT] ✓
- reference_build specified ✓
- reference_bases and variant_bases match coordinate type:
  * SNV: both single characters
  * Deletion: ref has sequence, alt is empty
  * Insertion: ref is empty, alt has sequence

4. HGVS FORMAT CHECK:
IF hgvs_descriptions present:
- Format: "NM_004333.4:c.1799T>A" or "NP_004324.2:p.Val600Glu"
- Includes transcript + version
- Follows HGVS nomenclature rules

5. ONTOLOGY ID VALIDATION:
External API checks:

Disease Ontology:
- Query DO API: Does disease_doid exist?
- Is it deprecated?

HPO (if phenotypes):
- Query HPO API: Do phenotype_hpo_ids exist?

NCIt (if therapies):
- Query NCIt API: Do therapy_ncit_ids exist?

Sequence Ontology:
- Verify variant_type_soids exist

6. LOGICAL CONSISTENCY:
Check for contradictions:

- IF evidence_direction == "Supports" AND evidence_significance == "Sensitivity":
  THEN evidence_description should mention response/efficacy
  
- IF variant_origin == "Somatic" AND evidence_type == "Predisposing":
  FLAG: Likely error (Predisposing usually germline)

- IF evidence_level == "A" BUT study_design == "Preclinical":
  FLAG: Inconsistency (Level A requires clinical validation)

7. MOLECULAR PROFILE CONSISTENCY:
- IF molecular_profile_is_complex == true:
  THEN should have ≥2 component variants
  
- IF therapy_interaction_type present:
  THEN should have ≥2 therapies

8. COMPLETENESS SCORE:
Calculate % of optional fields populated:
- phenotypes
- clinical_trial_nct_ids
- hgvs_descriptions
- allele_registry_ids
- coordinates (if determinable)

Target: 70%+ for high-quality curation

9. CONFIDENCE SCORING:
Aggregate confidence from all agents:
- Weight by importance (critical fields weighted higher)
- Flag if any field <0.7 confidence
- Overall extraction confidence = min(critical_field_confidences)

ERROR CATEGORIZATION:
- CRITICAL: Required field missing, logical contradiction
- MAJOR: Ontology ID invalid, format error
- MINOR: Optional field missing, low confidence

RETURN:
{
  "validation_passed": true/false,
  "errors": [
    {"field": "disease_doid", "type": "MAJOR", "message": "DOID not found in DO"},
    ...
  ],
  "warnings": [...],
  "completeness_score": 0.85,
  "overall_confidence": 0.92
}`,
        sequence: `Orchestrator->>Agent17: {all_extracted_fields}

Agent17->>Agent17: Check required fields:
  ✓ evidence_description
  ✓ evidence_type
  ✓ evidence_direction
  ... (all present)

Agent17->>Agent17: Validate type-significance compatibility:
  evidence_type="Predictive"
  evidence_significance="Sensitivity/Response"
  ✓ Compatible

Agent17->>Agent17: Check coordinate validity:
  start=140453136 ≤ stop=140453136 ✓
  chromosome="7" ✓ (valid)
  
Agent17->>DO API: Verify disease_doid="DOID:1909"
DO API-->>Agent17: ✓ Valid, not deprecated

Agent17->>NCIt API: Verify therapy_ncit_ids=["C68398"]
NCIt API-->>Agent17: ✓ Valid

Agent17->>Agent17: Check logical consistency:
  variant_origin="Somatic" + evidence_type="Predictive" ✓
  evidence_level="A" + study_design="Phase III" ✓
  
Agent17->>Agent17: Calculate completeness:
  Required: 100% (20/20)
  Optional: 75% (9/12)
  Overall: 87%
  
Agent17->>Agent17: Aggregate confidence:
  Min critical field: 0.92
  Average all fields: 0.94
  
Agent17-->>Orchestrator: {
  validation_passed: true,
  errors: [],
  warnings: ["coordinates_confidence=0.85"],
  completeness_score: 0.87,
  overall_confidence: 0.92
}`
      },
      {
        id: 'agent18',
        name: 'Completeness & Conflict Resolver',
        model: 'gpt-4o',
        type: 'Resolution',
        description: 'Final assembly, conflict resolution, human review queue',
        inputs: ['All fields', 'Validation results', 'Confidence scores'],
        outputs: ['Final structured output', 'Flagged fields for review', 'Confidence report'],
        tools: ['Conflict resolver', 'Output formatter'],
        evaluation: 'Coverage 95%+ required fields',
        dependencies: ['Agent 17'],
        instructions: `Finalize extraction and prepare output:

STEP 1: Identify Missing Required Fields
For each evidence_type:
- List which required fields are missing
- Attempt to infer from context if possible
- If cannot infer: Flag for human curation

STEP 2: Resolve Validation Errors
For each error from Agent 17:

CRITICAL errors:
- Attempt automatic fix if possible
  Example: Swap start/stop if reversed
- If cannot fix: Flag for human review
- Block publication until resolved

MAJOR errors:
- Try alternative ontology mappings
- Suggest corrections
- Flag for curator verification

MINOR errors:
- Note in comments
- Allow to proceed with warning

STEP 3: Handle Low Confidence Fields
For fields with confidence < 0.7:
- Mark field as "Low confidence"
- Provide alternative interpretations if available
- Add to human review queue

STEP 4: Conflict Resolution
If agents produced contradictory outputs:

Example: Agent 4 says Predictive, but no therapy found by Agent 14
Resolution strategies:
- Re-run Agent 4 with explicit therapy check
- Escalate to human review
- Choose most confident agent output

STEP 5: Assemble Final Output
Structure as CIViC Evidence Item JSON:

{
  "evidence_id": null, // Assigned by CIViC on submission
  "evidence_description": "...",
  "evidence_type": "Predictive",
  "evidence_direction": "Supports",
  "evidence_significance": "Sensitivity/Response",
  "evidence_level": "A",
  "evidence_rating": 5,
  
  "disease": {
    "disease_name": "Melanoma",
    "disease_doid": "DOID:1909"
  },
  
  "molecular_profile": {
    "name": "BRAF V600E",
    "is_complex": false,
    "variants": [...]
  },
  
  "therapies": [...],
  
  "source": {
    "source_id": "24185512",
    "source_type": "PubMed",
    ...
  },
  
  "metadata": {
    "extraction_date": "2025-11-03",
    "extractor": "OncoCITE Agent 1",
    "confidence_scores": {...},
    "validation_status": "Passed"
  }
}

STEP 6: Generate Human Review Queue
Prioritize for review:
1. CRITICAL validation errors
2. Overall confidence < 0.75
3. Evidence type = uncertain
4. Missing required fields
5. Novel variants (not in CIViC)

For each flagged item:
{
  "field": "evidence_significance",
  "issue": "Low confidence (0.68)",
  "suggested_values": ["Sensitivity/Response", "Resistance"],
  "context": "Paper shows response but also mentions acquired resistance",
  "recommendation": "Human review required to disambiguate"
}

STEP 7: Confidence Report
Summary statistics:
- Overall extraction confidence: 0.92
- Fields with confidence >0.9: 85%
- Fields requiring review: 2
- Completeness: 87% (required 100%, optional 75%)

Per-agent confidence:
- Source Metadata: 0.98
- NER: 0.85
- Evidence Type: 0.95
- ...

STEP 8: Trace Finalization
Ensure complete reasoning trace stored:
- All agent steps logged
- Tool calls recorded
- Confidence scores tracked
- Final decisions documented

RETURN PACKAGE:
1. Final CIViC Evidence Item (JSON)
2. Reasoning Trace (JSONB for PostgreSQL)
3. Confidence Report
4. Human Review Queue (if items flagged)
5. Trace URL (platform.openai.com/traces/{id})`,
        sequence: `Orchestrator->>Agent18: {all_fields, validation_results}

Agent18->>Agent18: Check for missing fields:
  Required: All present ✓
  Optional: 2 missing (phenotypes, hgvs) - acceptable
  
Agent18->>Agent18: Review validation errors:
  0 critical
  0 major
  1 warning (coordinate confidence 0.85) - acceptable
  
Agent18->>Agent18: Check confidence thresholds:
  Overall: 0.92 ✓ (>0.75)
  Min critical field: 0.92 ✓
  Fields <0.7: 0 ✓
  
Agent18->>Agent18: Assemble final JSON:
  {evidence_description, evidence_type, ...}
  
Agent18->>Agent18: Generate confidence report:
  - Extraction confidence: 0.92
  - Completeness: 87%
  - Review required: No
  
Agent18->>PostgreSQL: Store reasoning trace JSONB
PostgreSQL-->>Agent18: Stored with trace_id

Agent18->>Traces: Finalize OpenAI trace
Traces-->>Agent18: Trace URL generated

Agent18-->>Orchestrator: {
  civic_evidence_item: {...},
  reasoning_trace: {...},
  confidence_report: {...},
  review_queue: [],
  trace_url: "platform.openai.com/traces/abc123"
}`
      }
    ]
  };

  const toolDetails = {
    file_search: {
      name: 'file_search (Responses API)',
      description: 'Vector-based semantic search over CIViC data dictionary',
      setup: `1. Create vector store:
   vector_store = client.beta.vector_stores.create(
     name="CIViC Data Dictionary"
   )
   
2. Upload dictionary PDF:
   file = client.files.create(
     file=open("civic_dictionary.pdf", "rb"),
     purpose="assistants"
   )
   
3. Add to vector store:
   client.beta.vector_stores.files.create(
     vector_store_id=vector_store.id,
     file_id=file.id
   )`,
      usage: `# In agent definition:
agent = Agent(
  model="gpt-4o",
  tools=[
    {
      "type": "file_search",
      "file_search": {
        "vector_store_ids": [vector_store_id],
        "max_num_results": 5
      }
    }
  ]
)

# Agent calls automatically via tool use:
"Use file_search to find evidence_level criteria"

# Returns:
{
  "results": [
    {
      "content": "Level A - Validated Association: Phase III clinical trial OR FDA-approved companion diagnostic...",
      "file_name": "civic_dictionary.pdf",
      "score": 0.92
    }
  ]
}`,
      examples: [
        {
          query: "What are the criteria for evidence_level A?",
          response: "Retrieved: Level A criteria including Phase III trials, FDA approval, professional guidelines..."
        },
        {
          query: "What significance values are allowed for Predictive evidence type?",
          response: "Retrieved: Sensitivity/Response, Resistance, Adverse Response, Reduced Sensitivity, N/A"
        },
        {
          query: "How do I determine variant_origin for a somatic mutation?",
          response: "Retrieved: Somatic indicators include tumor-only sequencing, hotspot mutations, not in gnomAD..."
        }
      ]
    },
    web_search: {
      name: 'web_search (Responses API)',
      description: 'Real-time web search for clinical validation and current information',
      setup: `# In agent definition:
agent = Agent(
  model="gpt-4o",
  tools=[
    {"type": "web_search"}
  ]
)

# Enabled by default in Responses API
# No additional configuration needed`,
      usage: `# Agent calls automatically:
"Use web_search to validate BRAF V600E clinical information"

# Returns:
{
  "results": [
    {
      "title": "BRAF V600E Mutations in Melanoma - NCCN Guidelines",
      "url": "https://nccn.org/...",
      "snippet": "BRAF V600E mutations occur in approximately 50% of melanomas and predict sensitivity to BRAF inhibitors...",
      "date": "2024-08"
    },
    ...
  ]
}`,
      examples: [
        {
          query: "Latest clinical guidelines for BRAF V600E melanoma treatment",
          response: "Found: NCCN guidelines recommend dabrafenib + trametinib as first-line for BRAF V600E+ metastatic melanoma"
        },
        {
          query: "Current FDA approvals for EGFR L858R NSCLC",
          response: "Found: FDA approved osimertinib for EGFR L858R+ NSCLC including T790M resistance mutations"
        },
        {
          query: "Verify if NPM1 mutations are diagnostic for AML",
          response: "Found: WHO classification includes NPM1-mutated AML as distinct entity, diagnostic significance confirmed"
        }
      ]
    }
  };

  const renderAgentSequence = (agent) => (
    <div className="bg-gray-50 p-4 rounded-lg overflow-x-auto">
      <h4 className="font-semibold mb-2">Execution Sequence</h4>
      <pre className="text-xs font-mono bg-white p-3 rounded">
        {agent.sequence}
      </pre>
    </div>
  );

  const renderAgentCard = (agent, index) => (
    <div key={agent.id} className="bg-white rounded-lg shadow-lg p-6 mb-6">
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-3 mb-2">
            <div className="w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold">
              {index + 1}
            </div>
            <div>
              <h3 className="text-xl font-bold text-gray-800">{agent.name}</h3>
              <div className="text-sm text-gray-600">Model: {agent.model}</div>
            </div>
          </div>
          <p className="text-gray-700 mb-3">{agent.description}</p>
        </div>
        <div className={`px-3 py-1 rounded-full text-xs font-semibold ${
          agent.type === 'Extraction' ? 'bg-green-100 text-green-800' :
          agent.type === 'Classification' ? 'bg-blue-100 text-blue-800' :
          agent.type === 'NER' ? 'bg-purple-100 text-purple-800' :
          agent.type === 'Ontology Mapping' ? 'bg-yellow-100 text-yellow-800' :
          agent.type === 'Interpretation' ? 'bg-red-100 text-red-800' :
          agent.type === 'Generation' ? 'bg-indigo-100 text-indigo-800' :
          agent.type === 'Normalization' ? 'bg-pink-100 text-pink-800' :
          agent.type === 'Extraction + Lookup' ? 'bg-orange-100 text-orange-800' :
          agent.type === 'Assessment' ? 'bg-teal-100 text-teal-800' :
          agent.type === 'Validation' ? 'bg-cyan-100 text-cyan-800' :
          'bg-gray-100 text-gray-800'
        }`}>
          {agent.type}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
          <h4 className="font-semibold text-sm text-gray-700 mb-2">Inputs</h4>
          <ul className="text-sm space-y-1">
            {agent.inputs.map((input, i) => (
              <li key={i} className="flex items-start">
                <span className="text-green-600 mr-2">→</span>
                <span>{input}</span>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h4 className="font-semibold text-sm text-gray-700 mb-2">Outputs</h4>
          <ul className="text-sm space-y-1">
            {agent.outputs.map((output, i) => (
              <li key={i} className="flex items-start">
                <span className="text-blue-600 mr-2">←</span>
                <span>{output}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {agent.tools && agent.tools.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-sm text-gray-700 mb-2">Tools</h4>
          <div className="flex flex-wrap gap-2">
            {agent.tools.map((tool, i) => (
              <span key={i} className="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-xs">
                {tool}
              </span>
            ))}
          </div>
        </div>
      )}

      {agent.dependencies && agent.dependencies.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-sm text-gray-700 mb-2">Dependencies</h4>
          <div className="flex flex-wrap gap-2">
            {agent.dependencies.map((dep, i) => (
              <span key={i} className="px-3 py-1 bg-orange-100 text-orange-800 rounded-full text-xs">
                {dep}
              </span>
            ))}
          </div>
        </div>
      )}

      {agent.conditional && (
        <div className="mb-4 bg-yellow-50 border-l-4 border-yellow-500 p-3">
          <div className="font-semibold text-sm text-yellow-900">Conditional Execution</div>
          <div className="text-sm text-yellow-800">{agent.conditional}</div>
        </div>
      )}

      <div className="mb-4">
        <h4 className="font-semibold text-sm text-gray-700 mb-2">Evaluation Metric</h4>
        <div className="text-sm bg-blue-50 p-2 rounded">{agent.evaluation}</div>
      </div>

      <div className="mb-4">
        <h4 className="font-semibold text-sm text-gray-700 mb-2">Detailed Instructions</h4>
        <pre className="text-xs bg-gray-800 text-green-400 p-4 rounded overflow-x-auto whitespace-pre-wrap">
          {agent.instructions}
        </pre>
      </div>

      {renderAgentSequence(agent)}
    </div>
  );

  return (
    <div className="w-full min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto p-6">
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-8 rounded-lg shadow-lg mb-6">
          <h1 className="text-4xl font-bold mb-3">OncoCITE Agent 1: Complete Architecture</h1>
          <p className="text-blue-100 text-lg">18 Specialized Agents • OpenAI Native Stack • Full Reasoning Traces</p>
        </div>

        {/* Main Tabs */}
        <div className="flex flex-wrap gap-2 mb-6 border-b border-gray-300">
          <button
            onClick={() => setActiveTab('overview')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'overview'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Architecture Overview
          </button>
          <button
            onClick={() => setActiveTab('phase1')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'phase1'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Phase 1: Foundation
          </button>
          <button
            onClick={() => setActiveTab('phase2')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'phase2'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Phase 2: Evidence Structure
          </button>
          <button
            onClick={() => setActiveTab('phase3')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'phase3'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Phase 3: Clinical Interpretation
          </button>
          <button
            onClick={() => setActiveTab('phase4')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'phase4'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Phase 4: Molecular Profile
          </button>
          <button
            onClick={() => setActiveTab('phase5')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'phase5'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Phase 5: Conditional
          </button>
          <button
            onClick={() => setActiveTab('phase6')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'phase6'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Phase 6: Quality & Validation
          </button>
          <button
            onClick={() => setActiveTab('tools')}
            className={`px-6 py-3 font-semibold transition-colors ${
              activeTab === 'tools'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-600 hover:text-blue-600'
            }`}
          >
            Tool Details
          </button>
        </div>

        {/* Content */}
        <div className="space-y-6">
          {activeTab === 'overview' && (
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Complete Pipeline Architecture</h2>
              
              <div className="bg-gradient-to-r from-blue-50 to-purple-50 p-6 rounded-lg mb-6">
                <h3 className="text-xl font-bold mb-3">18 Specialized Agents</h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div className="bg-white p-4 rounded shadow">
                    <div className="font-bold text-blue-900 mb-2">Phase 1: Foundation (3)</div>
                    <div className="text-sm space-y-1">
                      <div>1. Source Metadata</div>
                      <div>2. Biomedical NER</div>
                      <div>3. Study Design</div>
                    </div>
                  </div>
                  <div className="bg-white p-4 rounded shadow">
                    <div className="font-bold text-green-900 mb-2">Phase 2: Evidence Structure (2)</div>
                    <div className="text-sm space-y-1">
                      <div>4. Evidence Type (CRITICAL)</div>
                      <div>5. Evidence Level</div>
                    </div>
                  </div>
                  <div className="bg-white p-4 rounded shadow">
                    <div className="font-bold text-purple-900 mb-2">Phase 3: Clinical (4)</div>
                    <div className="text-sm space-y-1">
                      <div>6. Disease Mapper</div>
                      <div>7. Variant Origin</div>
                      <div>8. Direction & Significance (HARD)</div>
                      <div>9. Statement Generator</div>
                    </div>
                  </div>
                  <div className="bg-white p-4 rounded shadow">
                    <div className="font-bold text-orange-900 mb-2">Phase 4: Molecular (4)</div>
                    <div className="text-sm space-y-1">
                      <div>10. Variant Standardizer</div>
                      <div>11. MP Classifier</div>
                      <div>12. Variant Type</div>
                      <div>13. Coordinates (COMPLEX)</div>
                    </div>
                  </div>
                  <div className="bg-white p-4 rounded shadow">
                    <div className="font-bold text-red-900 mb-2">Phase 5: Conditional (2)</div>
                    <div className="text-sm space-y-1">
                      <div>14. Therapy (if Predictive)</div>
                      <div>15. Phenotype (if Predisposing)</div>
                    </div>
                  </div>
                  <div className="bg-white p-4 rounded shadow">
                    <div className="font-bold text-teal-900 mb-2">Phase 6: Quality (3)</div>
                    <div className="text-sm space-y-1">
                      <div>16. Evidence Rating</div>
                      <div>17. Cross-Field Validator</div>
                      <div>18. Completeness & Resolver</div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Execution Flow */}
              <div className="mb-6">
                <h3 className="text-xl font-bold mb-3">Execution Flow</h3>
                <div className="bg-gray-50 p-4 rounded">
                  <pre className="text-sm font-mono overflow-x-auto">
{`Phase 1 (Parallel)
├─ Agent 1: Source Metadata ────┐
├─ Agent 2: NER ───────────────┤
└─ Agent 3: Study Design ──────┴─→ Context Established

Phase 2 (Sequential)
└─ Agent 4: Evidence Type (CRITICAL BRANCH POINT)
   └─ Agent 5: Evidence Level

Phase 3 (Mostly Parallel)
├─ Agent 6: Disease Mapper
├─ Agent 7: Variant Origin
├─ Agent 8: Direction & Significance (uses all above)
└─ Agent 9: Statement Generator (uses all above)

Phase 4 (Sequential with External Lookups)
├─ Agent 10: Variant Standardizer
├─ Agent 11: MP Classifier
├─ Agent 12: Variant Type
└─ Agent 13: Coordinates (Complex, may need external APIs)

Phase 5 (Conditional, Parallel if both apply)
├─ Agent 14: Therapy (IF Predictive)
└─ Agent 15: Phenotype (IF Predisposing or phenotypes mentioned)

Phase 6 (Sequential)
├─ Agent 16: Evidence Rating
├─ Agent 17: Cross-Field Validator
└─ Agent 18: Completeness & Conflict Resolver
   └─ Final Output + Human Review Queue`}
                  </pre>
                </div>
              </div>

              {/* Key Features */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-green-50 p-4 rounded border-l-4 border-green-500">
                  <h4 className="font-bold text-green-900 mb-2">OpenAI Native Tools</h4>
                  <ul className="text-sm space-y-1">
                    <li>• file_search: CIViC dictionary vector store</li>
                    <li>• web_search: Real-time validation</li>
                    <li>• Built into Responses API</li>
                    <li>• No external dependencies</li>
                  </ul>
                </div>
                <div className="bg-purple-50 p-4 rounded border-l-4 border-purple-500">
                  <h4 className="font-bold text-purple-900 mb-2">Tracing System</h4>
                  <ul className="text-sm space-y-1">
                    <li>• OpenAI Traces Dashboard (automatic)</li>
                    <li>• Custom reasoning spans</li>
                    <li>• PostgreSQL JSONB storage</li>
                    <li>• Complete audit trail</li>
                  </ul>
                </div>
                <div className="bg-blue-50 p-4 rounded border-l-4 border-blue-500">
                  <h4 className="font-bold text-blue-900 mb-2">Evaluation</h4>
                  <ul className="text-sm space-y-1">
                    <li>• OpenAI Evals API integration</li>
                    <li>• LLM-as-judge (o3 model)</li>
                    <li>• Python validators</li>
                    <li>• Automated benchmarking</li>
                  </ul>
                </div>
                <div className="bg-orange-50 p-4 rounded border-l-4 border-orange-500">
                  <h4 className="font-bold text-orange-900 mb-2">Model Strategy</h4>
                  <ul className="text-sm space-y-1">
                    <li>• o4-mini: Complex reasoning tasks</li>
                    <li>• gpt-4o: Orchestration & quality</li>
                    <li>• gpt-4o-mini: Straightforward tasks</li>
                    <li>• Cost-optimized selection</li>
                  </ul>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'phase1' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Phase 1: Foundation Layer (Agents 1-3)</h2>
              <p className="text-gray-700 mb-6">
                Extract basic entities and paper context. These agents run in parallel and establish the foundation for all downstream analysis.
              </p>
              {agents.phase1.map((agent, index) => renderAgentCard(agent, index))}
            </div>
          )}

          {activeTab === 'phase2' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Phase 2: Evidence Structure (Agents 4-5)</h2>
              <p className="text-gray-700 mb-6">
                <strong className="text-red-600">CRITICAL BRANCHING POINT:</strong> Agent 4 (Evidence Type Classifier) determines which fields are required downstream. This is the most important classification decision in the entire pipeline.
              </p>
              {agents.phase2.map((agent, index) => renderAgentCard(agent, index + 3))}
            </div>
          )}

          {activeTab === 'phase3' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Phase 3: Clinical Interpretation (Agents 6-9)</h2>
              <p className="text-gray-700 mb-6">
                Extract and interpret clinical entities. Agent 8 (Direction & Significance) is the hardest interpretation task, requiring careful reasoning about what the study demonstrates.
              </p>
              {agents.phase3.map((agent, index) => renderAgentCard(agent, index + 5))}
            </div>
          )}

          {activeTab === 'phase4' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Phase 4: Molecular Profile Construction (Agents 10-13)</h2>
              <p className="text-gray-700 mb-6">
                Build the variant representation with proper nomenclature, ontology terms, and genomic coordinates. Agent 13 (Coordinates) is particularly challenging as coordinates are often not stated in papers.
              </p>
              {agents.phase4.map((agent, index) => renderAgentCard(agent, index + 9))}
            </div>
          )}

          {activeTab === 'phase5' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Phase 5: Conditional Specialized Agents (Agents 14-15)</h2>
              <p className="text-gray-700 mb-6">
                <strong className="text-orange-600">CONDITIONAL EXECUTION:</strong> These agents only run if specific evidence types are detected. Agent 14 runs only for Predictive evidence, Agent 15 primarily for Predisposing evidence.
              </p>
              {agents.phase5.map((agent, index) => renderAgentCard(agent, index + 13))}
            </div>
          )}

          {activeTab === 'phase6' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Phase 6: Quality & Validation (Agents 16-18)</h2>
              <p className="text-gray-700 mb-6">
                Final quality assessment, validation, and output assembly. These agents ensure completeness, correctness, and flag any issues for human review.
              </p>
              {agents.phase6.map((agent, index) => renderAgentCard(agent, index + 15))}
            </div>
          )}

          {activeTab === 'tools' && (
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">OpenAI Native Tool Details</h2>
              
              {/* file_search */}
              <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
                <div className="flex items-center space-x-3 mb-4">
                  <Database className="w-8 h-8 text-purple-600" />
                  <div>
                    <h3 className="text-xl font-bold text-gray-800">{toolDetails.file_search.name}</h3>
                    <p className="text-gray-600">{toolDetails.file_search.description}</p>
                  </div>
                </div>

                <div className="mb-4">
                  <h4 className="font-semibold mb-2">Setup</h4>
                  <pre className="text-sm bg-gray-800 text-green-400 p-4 rounded overflow-x-auto">
                    {toolDetails.file_search.setup}
                  </pre>
                </div>

                <div className="mb-4">
                  <h4 className="font-semibold mb-2">Usage in Agents</h4>
                  <pre className="text-sm bg-gray-800 text-green-400 p-4 rounded overflow-x-auto">
                    {toolDetails.file_search.usage}
                  </pre>
                </div>

                <div>
                  <h4 className="font-semibold mb-2">Example Queries</h4>
                  <div className="space-y-3">
                    {toolDetails.file_search.examples.map((ex, i) => (
                      <div key={i} className="bg-purple-50 p-3 rounded border-l-4 border-purple-500">
                        <div className="font-semibold text-sm text-purple-900">{ex.query}</div>
                        <div className="text-sm text-purple-800 mt-1">{ex.response}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* web_search */}
              <div className="bg-white rounded-lg shadow-lg p-6">
                <div className="flex items-center space-x-3 mb-4">
                  <Search className="w-8 h-8 text-blue-600" />
                  <div>
                    <h3 className="text-xl font-bold text-gray-800">{toolDetails.web_search.name}</h3>
                    <p className="text-gray-600">{toolDetails.web_search.description}</p>
                  </div>
                </div>

                <div className="mb-4">
                  <h4 className="font-semibold mb-2">Setup</h4>
                  <pre className="text-sm bg-gray-800 text-green-400 p-4 rounded overflow-x-auto">
                    {toolDetails.web_search.setup}
                  </pre>
                </div>

                <div className="mb-4">
                  <h4 className="font-semibold mb-2">Usage in Agents</h4>
                  <pre className="text-sm bg-gray-800 text-green-400 p-4 rounded overflow-x-auto">
                    {toolDetails.web_search.usage}
                  </pre>
                </div>

                <div>
                  <h4 className="font-semibold mb-2">Example Queries</h4>
                  <div className="space-y-3">
                    {toolDetails.web_search.examples.map((ex, i) => (
                      <div key={i} className="bg-blue-50 p-3 rounded border-l-4 border-blue-500">
                        <div className="font-semibold text-sm text-blue-900">{ex.query}</div>
                        <div className="text-sm text-blue-800 mt-1">{ex.response}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="bg-gradient-to-r from-green-600 to-teal-600 text-white p-6 rounded-lg shadow-lg mt-6">
          <h3 className="text-xl font-bold mb-3">Implementation Summary</h3>
          <div className="grid md:grid-cols-4 gap-4 text-sm">
            <div>
              <div className="font-semibold mb-2">Total Agents</div>
              <div className="text-2xl font-bold">18</div>
              <div className="text-green-100">Specialized agents</div>
            </div>
            <div>
              <div className="font-semibold mb-2">Phases</div>
              <div className="text-2xl font-bold">6</div>
              <div className="text-green-100">Sequential phases</div>
            </div>
            <div>
              <div className="font-semibold mb-2">Fields Extracted</div>
              <div className="text-2xl font-bold">100+</div>
              <div className="text-green-100">CIViC fields</div>
            </div>
            <div>
              <div className="font-semibold mb-2">Dependencies</div>
              <div className="text-2xl font-bold">0</div>
              <div className="text-green-100">External (OpenAI only)</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default OncociteArchitectureDetailed;