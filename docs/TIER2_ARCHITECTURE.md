# Tier 2 Local Normalization Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      ONCOCITE TIER 2 NORMALIZATION                      │
│                       (COMPLETELY OFFLINE/LOCAL)                        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                             INPUT (From Tier 1)                         │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐           │
│  │  Disease  │  │  Variant  │  │  Therapy  │  │   Trial   │           │
│  │   Names   │  │   Names   │  │   Names   │  │    IDs    │           │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘           │
└─────────────────────────────────────────────────────────────────────────┘
         │                │                │                │
         ▼                ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           NORMALIZATION AGENTS                          │
│                                                                         │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐    │
│  │    AGENT 9       │  │    AGENT 10      │  │    AGENT 11      │    │
│  │  Disease Norm    │  │  Variant Norm    │  │  Therapy Norm    │    │
│  │                  │  │                  │  │                  │    │
│  │  • Exact match   │  │  • L858R→Leu858R │  │  • Brand→Generic │    │
│  │  • Synonym match │  │  • ClinVar lookup│  │  • Drug class    │    │
│  │  • Fuzzy search  │  │  • HGVS format   │  │  • Synonyms      │    │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘    │
│           │                     │                     │               │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐    │
│  │    AGENT 12      │  │    AGENT 13      │  │    AGENT 14      │    │
│  │  Trial Norm      │  │  Coordinate Norm │  │  Ontology Norm   │    │
│  │                  │  │                  │  │                  │    │
│  │  • NCT validate  │  │  • HGVS validate │  │  • Phenotype     │    │
│  │  • EudraCT       │  │  • Genomic coord │  │  • GO terms      │    │
│  │  • Registry ID   │  │  • Build (hg38)  │  │  • HPO           │    │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘    │
│           │                     │                     │               │
└───────────┼─────────────────────┼─────────────────────┼───────────────┘
            │                     │                     │
            ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        LOCAL SQLITE DATABASE                            │
│                     data/databases/ontologies.db                        │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │
│  │    terms     │  │   synonyms   │  │    xrefs     │  │ variants │  │
│  │  116,748 rows│  │  308,676 rows│  │              │  │ 251,716  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────┘  │
│                                                                         │
│  Indices: ontology, name, term_id, gene_symbol                         │
└─────────────────────────────────────────────────────────────────────────┘
            ▲                     ▲                     ▲
            │                     │                     │
┌───────────┼─────────────────────┼─────────────────────┼───────────────┐
│           │                     │                     │               │
│  ┌────────────────────────────────────────────────────────────┐       │
│  │                   DATABASE BUILDER                         │       │
│  │            local_ontology_parsers.py                       │       │
│  │                                                            │       │
│  │  • OBOParser (parses OBO format)                          │       │
│  │  • ClinVarParser (parses TSV)                             │       │
│  │  • OntologyDatabaseBuilder (SQLite)                       │       │
│  └────────────────────────────────────────────────────────────┘       │
│                              ▲                                         │
│                              │                                         │
│  ┌────────────────────────────────────────────────────────────┐       │
│  │                  DOWNLOAD SCRIPT                           │       │
│  │            download_ontologies.sh                          │       │
│  │                                                            │       │
│  │  Downloads from:                                           │       │
│  │  • GitHub (DOID, SO, MONDO)                               │       │
│  │  • OBO Library (GO, HPO)                                  │       │
│  │  • NCBI FTP (ClinVar)                                     │       │
│  └────────────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘
            │                     │                     │
            ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        ONTOLOGY FILES (3.6 GB)                          │
│                       data/ontologies/                                  │
│                                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│  │ doid.obo │  │ so.obo   │  │ go.obo   │  │ hp.obo   │  │mondo.obo ││
│  │  6.7 MB  │  │  1.1 MB  │  │  34 MB   │  │ 9.8 MB   │  │  49 MB   ││
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  └──────────┘│
│                                                                         │
│  ┌─────────────────────┐                                               │
│  │ clinvar_summary.txt │                                               │
│  │       3.5 GB        │                                               │
│  └─────────────────────┘                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### 1. Setup Phase (One-Time)

```
┌──────────────────┐
│  User runs:      │
│  ./download_     │
│  ontologies.sh   │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Download 6 ontology files:          │
│  • DOID    (15 MB)                   │
│  • SO      (5 MB)                    │
│  • GO      (100 MB)                  │
│  • HPO     (20 MB)                   │
│  • MONDO   (50 MB)                   │
│  • ClinVar (1 GB compressed)         │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────┐
│  User runs:      │
│  python3 local_  │
│  ontology_       │
│  parsers.py      │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Parse OBO files:                    │
│  • Extract terms, definitions        │
│  • Extract synonyms                  │
│  • Extract relationships (is_a)      │
│  • Parse ClinVar TSV                 │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Build SQLite database:              │
│  • Create schema (4 tables)          │
│  • Insert 116,748 terms              │
│  • Insert 308,676 synonyms           │
│  • Insert 251,716 variants           │
│  • Create indices                    │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────┐
│  Database ready  │
│  (~200 MB)       │
└──────────────────┘
```

### 2. Normalization Phase (Runtime)

```
┌──────────────────────────────────────┐
│  Input from Tier 1:                  │
│  "lung adenocarcinoma"               │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Agent 9: DiseaseNormalizer          │
│  normalizer.normalize("lung adeno..") │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Query SQLite:                       │
│  SELECT term_id, name                │
│  FROM terms                          │
│  WHERE ontology = 'DOID'             │
│    AND LOWER(name) = 'lung adeno...' │
│    AND is_obsolete = 0               │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Result:                             │
│  {                                   │
│    "doid": "DOID:3910",              │
│    "doid_name": "lung adenocarcinoma"│
│    "confidence": 1.0                 │
│  }                                   │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Output to Tier 3 (Validation)       │
└──────────────────────────────────────┘
```

---

## Agent-Specific Workflows

### Agent 9: Disease Normalizer

```
Input: "Non-small cell lung cancer"
    │
    ▼
┌─────────────────────────┐
│  Step 1: Exact Match    │
│  LOWER(name) = input    │
└───────┬─────────────────┘
        │ No match
        ▼
┌─────────────────────────┐
│  Step 2: Synonym Match  │
│  JOIN synonyms table    │
└───────┬─────────────────┘
        │ No match
        ▼
┌─────────────────────────┐
│  Step 3: Fuzzy Match    │
│  name LIKE %input%      │
└───────┬─────────────────┘
        │ Found 5 matches
        ▼
┌─────────────────────────┐
│  Return best match      │
│  + all partial matches  │
└─────────────────────────┘
```

### Agent 10: Variant Normalizer

```
Input: gene="EGFR", variant="L858R"
    │
    ▼
┌────────────────────────────────┐
│  Step 1: Convert AA notation   │
│  L858R → Leu858Arg             │
└───────┬────────────────────────┘
        │
        ▼
┌────────────────────────────────┐
│  Step 2: Build search patterns │
│  • %L858R%                     │
│  • %EGFR%L858R%                │
│  • %Leu858Arg%                 │
└───────┬────────────────────────┘
        │
        ▼
┌────────────────────────────────┐
│  Step 3: Query ClinVar         │
│  WHERE gene_symbol = 'EGFR'    │
│    AND name LIKE pattern       │
└───────┬────────────────────────┘
        │ Found match!
        ▼
┌────────────────────────────────┐
│  Return ClinVar entry:         │
│  • variation_id                │
│  • HGVS notation               │
│  • clinical_significance       │
└────────────────────────────────┘
```

### Agent 11: Therapy Normalizer

```
Input: "Tagrisso"
    │
    ▼
┌────────────────────────────────┐
│  Step 1: Normalize input       │
│  LOWER(input) = "tagrisso"     │
└───────┬────────────────────────┘
        │
        ▼
┌────────────────────────────────┐
│  Step 2: Lookup in dictionary  │
│  drug_synonyms dict            │
│  "osimertinib": ["tagrisso"]   │
└───────┬────────────────────────┘
        │ Found!
        ▼
┌────────────────────────────────┐
│  Step 3: Return normalized:    │
│  • normalized_name: Osimertinib│
│  • drug_class: EGFR inhibitor  │
│  • synonyms: [tagrisso, azd..] │
└────────────────────────────────┘
```

---

## Database Schema Details

### Terms Table Structure

```
┌─────────────────────────────────────────────────────────────┐
│                         TERMS TABLE                         │
├──────────┬──────────┬──────────┬────────────┬───────────────┤
│ term_id  │ ontology │   name   │ definition │  is_obsolete  │
├──────────┼──────────┼──────────┼────────────┼───────────────┤
│DOID:3910 │   DOID   │lung ade..│A lung non..│       0       │
│HP:0001..│   HPO    │Seizure   │An episode..│       0       │
│GO:00001..│   GO     │mitochon..│A membrane..│       0       │
└──────────┴──────────┴──────────┴────────────┴───────────────┘
                  ▲
                  │
        ┌─────────┴──────────────┐
        │                        │
┌───────▼─────────┐    ┌─────────▼────────┐
│  SYNONYMS       │    │    XREFS         │
│                 │    │                  │
│ term_id | syn   │    │ term_id | xref   │
│ DOID... | NSCLC │    │ DOID... | UMLS:..│
└─────────────────┘    └──────────────────┘
```

### Variants Table Structure

```
┌────────────────────────────────────────────────────────────────────┐
│                        VARIANTS TABLE                              │
├────────┬───────┬──────┬─────────┬──────┬─────┬─────┬──────┬──────┤
│var_id  │ name  │ gene │ clin_sig│ rs_id│ chr │ pos │ ref  │ alt  │
├────────┼───────┼──────┼─────────┼──────┼─────┼─────┼──────┼──────┤
│ 16609  │NM_...│ EGFR │drug resp│rs1..│  7  │5524.│  T   │  G   │
└────────┴───────┴──────┴─────────┴──────┴─────┴─────┴──────┴──────┘
```

---

## Performance Optimization

### Index Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                    QUERY OPTIMIZATION                       │
│                                                             │
│  Without Indices:          With Indices:                   │
│  ┌────────────────┐       ┌────────────────┐              │
│  │ Full table scan│       │ Index lookup   │              │
│  │ 116K rows      │       │ B-tree search  │              │
│  │ ~200ms         │       │ ~5ms           │              │
│  └────────────────┘       └────────────────┘              │
│                                                             │
│  Key Indices:                                              │
│  • idx_terms_ontology (ontology)                           │
│  • idx_terms_name (name)                                   │
│  • idx_variants_gene (gene_symbol)                         │
│  • idx_variants_name (name)                                │
└─────────────────────────────────────────────────────────────┘
```

### Caching Strategy (Future)

```
┌────────────────────────────────────────────────────────────┐
│                  FUTURE CACHING LAYER                      │
│                                                            │
│  Input → Check Redis → Cache Hit? → Return                │
│              │                                             │
│              └─ Cache Miss → SQLite → Cache → Return      │
│                                                            │
│  Expected Performance:                                     │
│  • Cache Hit: <1ms                                        │
│  • Cache Miss: ~10ms (SQLite) + cache write               │
│  • Cache TTL: 1 hour                                      │
└────────────────────────────────────────────────────────────┘
```

---

## Error Handling

### Normalization Confidence Levels

```
┌─────────────────────────────────────────────────────────────┐
│                   CONFIDENCE SCORING                        │
│                                                             │
│  1.0 (100%) ──► Exact match                                │
│                 └─ "lung adenocarcinoma" → DOID:3910       │
│                                                             │
│  0.95 (95%)  ──► Synonym match                             │
│                 └─ "NSCLC" → "non-small cell lung cancer"  │
│                                                             │
│  0.8 (80%)   ──► Format conversion                         │
│                 └─ "L858R" → "p.Leu858Arg"                 │
│                                                             │
│  0.7 (70%)   ──► Partial match                             │
│                 └─ "seizure" → "Photosensitive...seizure"  │
│                                                             │
│  0.3 (30%)   ──► No match (return original)                │
│                 └─ Unknown drug → original name            │
└─────────────────────────────────────────────────────────────┘
```

---

## Deployment Scenarios

### Scenario 1: Single Machine

```
┌───────────────────────────────────────┐
│          Local Machine                │
│                                       │
│  ┌─────────────────────────────────┐ │
│  │   OncoCITE Python Process       │ │
│  │                                 │ │
│  │   ┌──────────────┐              │ │
│  │   │ Tier 1       │              │ │
│  │   │ Extraction   │              │ │
│  │   └──────┬───────┘              │ │
│  │          │                      │ │
│  │   ┌──────▼───────┐              │ │
│  │   │ Tier 2       │──┐           │ │
│  │   │ Normalization│  │           │ │
│  │   └──────────────┘  │           │ │
│  │                     │           │ │
│  │   ┌─────────────────▼────────┐  │ │
│  │   │   SQLite Database        │  │ │
│  │   │   ontologies.db (200MB)  │  │ │
│  │   └──────────────────────────┘  │ │
│  └─────────────────────────────────┘ │
└───────────────────────────────────────┘
```

### Scenario 2: Client-Server (Future)

```
┌──────────────┐      ┌──────────────────────────┐
│   Client 1   │─────►│   Normalization Server   │
└──────────────┘      │                          │
                      │  ┌────────────────────┐  │
┌──────────────┐      │  │   FastAPI/Flask    │  │
│   Client 2   │─────►│  │   REST endpoints   │  │
└──────────────┘      │  └─────────┬──────────┘  │
                      │            │             │
┌──────────────┐      │  ┌─────────▼──────────┐  │
│   Client 3   │─────►│  │  6 Normalizers     │  │
└──────────────┘      │  └─────────┬──────────┘  │
                      │            │             │
                      │  ┌─────────▼──────────┐  │
                      │  │   SQLite + Redis   │  │
                      │  │   Cache Layer      │  │
                      │  └────────────────────┘  │
                      └──────────────────────────┘
```

---

## Summary Statistics

```
┌────────────────────────────────────────────────────────────┐
│               TIER 2 SYSTEM STATISTICS                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Total Agents:              6                             │
│  Total Terms:               116,748                        │
│  Total Variants:            251,716                        │
│  Total Synonyms:            308,676                        │
│  Database Size:             ~200 MB                        │
│  Raw Ontology Files:        ~3.6 GB                        │
│                                                            │
│  Avg Query Time:            <10 ms                         │
│  Setup Time:                ~5 minutes                     │
│  Internet Required:         No (after setup)               │
│  External API Calls:        0                              │
│                                                            │
│  Status:                    ✅ OPERATIONAL                 │
└────────────────────────────────────────────────────────────┘
```

---

**Architecture Version**: 1.0.0
**Last Updated**: 2025-11-08
**Status**: ✅ Production Ready
