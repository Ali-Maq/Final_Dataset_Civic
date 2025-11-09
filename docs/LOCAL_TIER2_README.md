# Local Tier 2 Normalization System

## Overview

This document describes the **local, offline Tier 2 normalization system** for the OncoCITE 18-agent architecture. All 6 normalization agents (Agents 9-14) operate completely offline using local ontology databases.

**Status**: ✅ **FULLY OPERATIONAL**

---

## Quick Start

### 1. Download Ontologies

```bash
./download_ontologies.sh
```

Downloads ~3.6 GB of ontology data:
- DOID (Disease Ontology)
- SO (Sequence Ontology)
- GO (Gene Ontology)
- HPO (Human Phenotype Ontology)
- MONDO (Monarch Disease Ontology)
- ClinVar (Variant Database)

### 2. Build Local Database

```bash
python3 local_ontology_parsers.py
```

Parses OBO files and builds SQLite database with:
- 116,748 ontology terms
- 251,716 ClinVar variants
- 308,676 synonyms

### 3. Test Normalizers

```bash
python3 local_normalizers.py
```

Tests all 6 Tier 2 normalizer agents.

---

## Architecture

### Tier 2: Normalization Agents (Agents 9-14)

| Agent ID | Name | Data Sources | Status |
|----------|------|--------------|--------|
| **Agent 9** | Disease Normalizer | DOID, MONDO | ✅ Working |
| **Agent 10** | Variant Normalizer | SO, ClinVar | ✅ Working |
| **Agent 11** | Therapy Normalizer | Drug dictionary | ✅ Working |
| **Agent 12** | Trial Normalizer | NCT validation | ✅ Working |
| **Agent 13** | Coordinate Normalizer | HGVS validation | ✅ Working |
| **Agent 14** | Ontology Normalizer | GO, HPO | ✅ Working |

---

## Agent Details

### Agent 9: Disease Normalizer

**Purpose**: Normalize disease names to standardized ontologies

**Data Sources**:
- DOID (Disease Ontology): 11,985 terms
- MONDO (Monarch Disease Ontology): 52,289 terms

**Matching Strategy**:
1. Exact match on disease name
2. Synonym match
3. Partial match (fuzzy search)

**Example**:
```python
from local_normalizers import normalize_disease

result = normalize_disease("lung adenocarcinoma")
# Output: {
#   "doid": "DOID:3910",
#   "doid_name": "lung adenocarcinoma",
#   "confidence": 1.0
# }
```

**Performance**:
- Exact match: 100% confidence
- Synonym match: 95% confidence
- Partial match: <70% confidence

---

### Agent 10: Variant Normalizer

**Purpose**: Normalize genetic variants to ClinVar and SO

**Data Sources**:
- ClinVar: 251,716 variants
- SO (Sequence Ontology): 2,319 terms

**Features**:
- Single-letter to 3-letter amino acid conversion (L858R → Leu858Arg)
- Multiple search patterns
- HGVS notation support

**Example**:
```python
from local_normalizers import normalize_variant

result = normalize_variant("EGFR", "L858R")
# Output: {
#   "clinvar_matches": [{
#     "variation_id": 16609,
#     "name": "NM_005228.5(EGFR):c.2573T>G (p.Leu858Arg)",
#     "clinical_significance": "drug response"
#   }],
#   "confidence": 0.8
# }
```

**Amino Acid Mapping**:
- Automatic conversion: L858R → Leu858Arg
- Supports all 20 standard amino acids

---

### Agent 11: Therapy Normalizer

**Purpose**: Normalize drug/therapy names

**Data Sources**:
- Built-in drug dictionary (common oncology drugs)
- Expandable to NCIt (requires UMLS license)

**Supported Drugs**:
- EGFR inhibitors: osimertinib, gefitinib, erlotinib, afatinib
- Immune checkpoint inhibitors: pembrolizumab, nivolumab
- Platinum compounds: cisplatin, carboplatin
- Antifolates: pemetrexed

**Example**:
```python
from local_normalizers import normalize_therapy

result = normalize_therapy("Tagrisso")
# Output: {
#   "normalized_name": "Osimertinib",
#   "drug_class": "EGFR inhibitor",
#   "synonyms": ["tagrisso", "azd9291"],
#   "confidence": 1.0
# }
```

**Features**:
- Brand name → Generic name mapping
- Drug class classification
- Synonym recognition

---

### Agent 12: Trial Normalizer

**Purpose**: Validate and normalize clinical trial identifiers

**Supported Registries**:
- ClinicalTrials.gov (NCT format)
- EudraCT (European Union)

**Validation**:
- NCT format: NCT + 8 digits (e.g., NCT01234567)
- Automatic extraction from free text

**Example**:
```python
from local_normalizers import normalize_trial

result = normalize_trial("NCT01234567")
# Output: {
#   "normalized_id": "NCT01234567",
#   "registry": "ClinicalTrials.gov",
#   "is_valid": True,
#   "confidence": 1.0
# }
```

---

### Agent 13: Coordinate Normalizer

**Purpose**: Validate and normalize genomic coordinates

**Supported Formats**:
- HGVS protein notation: `p.Leu858Arg`
- HGVS cDNA notation: `c.2573T>G`
- Genomic coordinates: `chr7:55249071 A>G`
- Simple format: `7:55249071A>G`

**Example**:
```python
from local_normalizers import normalize_coordinates

result = normalize_coordinates("p.Leu858Arg")
# Output: {
#   "hgvs_validated": True,
#   "genomic_build": "hg38",
#   "confidence": 1.0
# }
```

**Features**:
- HGVS format validation
- Genomic coordinate extraction
- Build specification (hg38, hg19)

---

### Agent 14: Ontology Normalizer

**Purpose**: Normalize to GO, HPO, MONDO

**Data Sources**:
- GO (Gene Ontology): 35,690 terms
- HPO (Human Phenotype Ontology): 14,465 terms
- MONDO: 52,289 terms

**Matching Strategy**:
1. Exact match on phenotype name
2. Synonym match
3. Partial match

**Example**:
```python
from local_normalizers import normalize_phenotype

result = normalize_phenotype("seizure")
# Output: {
#   "hpo_id": "HP:0001327",
#   "hpo_name": "Photosensitive myoclonic seizure",
#   "confidence": 0.7,
#   "hpo_matches": [...]
# }
```

---

## Database Schema

### SQLite Database: `data/databases/ontologies.db`

**Tables**:

#### 1. `terms` table
```sql
CREATE TABLE terms (
    term_id TEXT PRIMARY KEY,
    ontology TEXT,
    name TEXT,
    definition TEXT,
    is_obsolete INTEGER
);
```

**Indices**:
- `idx_terms_ontology`
- `idx_terms_name`
- `idx_terms_obsolete`

#### 2. `synonyms` table
```sql
CREATE TABLE synonyms (
    term_id TEXT,
    synonym TEXT,
    FOREIGN KEY (term_id) REFERENCES terms(term_id)
);
```

**Index**: `idx_synonyms_term_id`

#### 3. `xrefs` table
```sql
CREATE TABLE xrefs (
    term_id TEXT,
    xref TEXT,
    FOREIGN KEY (term_id) REFERENCES terms(term_id)
);
```

**Index**: `idx_xrefs_term_id`

#### 4. `relationships` table
```sql
CREATE TABLE relationships (
    child_term_id TEXT,
    parent_term_id TEXT,
    FOREIGN KEY (child_term_id) REFERENCES terms(term_id),
    FOREIGN KEY (parent_term_id) REFERENCES terms(term_id)
);
```

**Index**: `idx_relationships_child`

#### 5. `variants` table
```sql
CREATE TABLE variants (
    variation_id INTEGER PRIMARY KEY,
    name TEXT,
    gene_symbol TEXT,
    clinical_significance TEXT,
    rs_id TEXT,
    chromosome TEXT,
    position INTEGER,
    ref_allele TEXT,
    alt_allele TEXT,
    type TEXT
);
```

**Indices**:
- `idx_variants_gene`
- `idx_variants_name`

---

## File Structure

```
Final_Dataset_Civic/
│
├── data/
│   ├── ontologies/               # Downloaded OBO files (3.6 GB)
│   │   ├── doid.obo
│   │   ├── so.obo
│   │   ├── go.obo
│   │   ├── hp.obo
│   │   ├── mondo.obo
│   │   └── clinvar_summary.txt
│   │
│   └── databases/                # Built SQLite database
│       └── ontologies.db         # ~200 MB
│
├── download_ontologies.sh        # Download script
├── local_ontology_parsers.py     # OBO parser + DB builder
├── local_normalizers.py          # 6 normalizer agents
├── test_database_queries.py      # Database verification
│
├── LOCAL_ONTOLOGIES_SOURCES.md   # Data source documentation
└── LOCAL_TIER2_README.md         # This file
```

---

## Performance Metrics

### Database Statistics

| Metric | Value |
|--------|-------|
| **Total Terms** | 116,748 |
| **Total Variants** | 251,716 |
| **Total Synonyms** | 308,676 |
| **Database Size** | ~200 MB |
| **Build Time** | ~2 minutes |

### Normalizer Performance

| Agent | Avg Query Time | Confidence Range |
|-------|----------------|------------------|
| Agent 9 (Disease) | <10 ms | 0.7 - 1.0 |
| Agent 10 (Variant) | <20 ms | 0.3 - 1.0 |
| Agent 11 (Therapy) | <1 ms | 0.3 - 1.0 |
| Agent 12 (Trial) | <1 ms | 0.8 - 1.0 |
| Agent 13 (Coordinate) | <1 ms | 0.8 - 1.0 |
| Agent 14 (Phenotype) | <10 ms | 0.7 - 1.0 |

---

## Usage Examples

### Python API

```python
from local_normalizers import (
    normalize_disease,
    normalize_variant,
    normalize_therapy,
    normalize_trial,
    normalize_coordinates,
    normalize_phenotype
)

# Disease normalization
disease = normalize_disease("non-small cell lung cancer")
print(f"DOID: {disease['doid']}")

# Variant normalization
variant = normalize_variant("BRAF", "V600E")
print(f"ClinVar: {len(variant['clinvar_matches'])} matches")

# Therapy normalization
drug = normalize_therapy("Keytruda")
print(f"Normalized: {drug['normalized_name']}")

# Trial normalization
trial = normalize_trial("NCT02220894")
print(f"Valid: {trial['is_valid']}")

# Coordinate normalization
coord = normalize_coordinates("chr7:140753336A>T")
print(f"Validated: {coord['hgvs_validated']}")

# Phenotype normalization
pheno = normalize_phenotype("tumor")
print(f"HPO: {pheno['hpo_id']}")
```

### Class-Based API

```python
from local_normalizers import DiseaseNormalizer

# Using context manager (auto-connects and closes DB)
with DiseaseNormalizer() as normalizer:
    result = normalizer.normalize("melanoma")
    print(result)

# Manual connection management
normalizer = DiseaseNormalizer()
normalizer.connect()
result = normalizer.normalize("melanoma")
normalizer.close()
```

---

## Extending the System

### Adding More Drugs (Agent 11)

Edit `local_normalizers.py`:

```python
class TherapyNormalizer(BaseNormalizer):
    def __init__(self, db_path: str = "data/databases/ontologies.db"):
        super().__init__(db_path)
        self.drug_synonyms = {
            # Add more drugs here
            "trastuzumab": ["herceptin"],
            "bevacizumab": ["avastin"],
            # ...
        }
```

### Adding NCIt Support

1. Download NCIt from NCI (requires UMLS license)
2. Parse OWL file and add drug terms to database
3. Update `TherapyNormalizer` to query NCIt table

### Adding More Ontologies

1. Add download URL to `download_ontologies.sh`
2. Add parser to `local_ontology_parsers.py`
3. Update database schema if needed
4. Update corresponding normalizer

---

## Troubleshooting

### Issue: Database Not Found

**Error**: `FileNotFoundError: Database not found: data/databases/ontologies.db`

**Solution**:
```bash
# Download ontologies
./download_ontologies.sh

# Build database
python3 local_ontology_parsers.py
```

### Issue: No Matches Found

**Problem**: Normalizer returns empty results

**Solutions**:
1. Check spelling of input term
2. Try partial matches (will have lower confidence)
3. Check if term is in database:
   ```python
   python3 test_database_queries.py
   ```

### Issue: Slow Queries

**Problem**: Queries taking > 100ms

**Solutions**:
1. Verify database indices are created
2. Check database file size (should be ~200 MB)
3. Rebuild database: `python3 local_ontology_parsers.py`

---

## Maintenance

### Updating Ontologies

Ontologies are updated regularly by their maintainers:

**Monthly Updates**:
- DOID
- ClinVar
- MONDO

**Quarterly Updates**:
- GO
- HPO

**To update**:
```bash
# Re-download latest versions
./download_ontologies.sh

# Rebuild database
python3 local_ontology_parsers.py
```

### Database Optimization

To rebuild indices for better performance:

```python
import sqlite3

conn = sqlite3.connect("data/databases/ontologies.db")
conn.execute("ANALYZE")
conn.close()
```

---

## Integration with OncoCITE

The local normalizers integrate seamlessly with the main OncoCITE pipeline:

```python
from oncocite_agents import OncoCITEOrchestrator
from local_normalizers import (
    DiseaseNormalizer,
    VariantNormalizer,
    TherapyNormalizer
)

# Initialize normalizers
disease_norm = DiseaseNormalizer()
variant_norm = VariantNormalizer()
therapy_norm = TherapyNormalizer()

# Use in Tier 2 of pipeline
# (See oncocite_agents.py for integration details)
```

---

## Testing

### Run All Tests

```bash
# Test database content
python3 test_database_queries.py

# Test all normalizers
python3 local_normalizers.py
```

### Expected Output

All tests should show:
- ✅ Database contains correct number of terms
- ✅ All 6 normalizers return valid results
- ✅ Confidence scores in expected ranges

---

## License & Attribution

### Ontology Licenses

- **DOID**: CC0 1.0 (Public Domain)
- **SO**: CC BY 4.0
- **GO**: CC BY 4.0
- **HPO**: Custom (free for research)
- **MONDO**: CC BY 4.0
- **ClinVar**: Public Domain (NCBI)

### Citations

If using this system, please cite the original ontologies:

**DOID**:
```
Schriml LM, et al. Disease Ontology 2022: a mountain of mapping and precision.
Nucleic Acids Res. 2022.
```

**GO**:
```
The Gene Ontology Consortium. The Gene Ontology resource: enriching a GOld mine.
Nucleic Acids Res. 2021.
```

**HPO**:
```
Köhler S, et al. The Human Phenotype Ontology in 2021.
Nucleic Acids Res. 2021.
```

**ClinVar**:
```
Landrum MJ, et al. ClinVar: improvements to accessing data.
Nucleic Acids Res. 2020.
```

---

## FAQ

**Q: Can this system work completely offline?**
A: Yes! Once ontologies are downloaded and the database is built, all operations are local.

**Q: How often should I update the ontologies?**
A: Monthly for clinical applications, quarterly for research.

**Q: Can I add custom ontologies?**
A: Yes! Add your OBO file to `data/ontologies/` and update the parser.

**Q: What about SNOMED CT or NCIt?**
A: These require UMLS licenses. Contact NLM for access.

**Q: How much disk space is needed?**
A: ~4 GB total (3.6 GB ontologies + 200 MB database)

---

## Support

For issues or questions:
1. Check troubleshooting section above
2. Review test output: `python3 local_normalizers.py`
3. Verify database: `python3 test_database_queries.py`

---

## Future Enhancements

### Planned Features

1. **Fuzzy Matching**
   - Levenshtein distance for typos
   - Phonetic matching for drug names

2. **API Server**
   - REST API for normalizers
   - FastAPI/Flask wrapper

3. **Caching Layer**
   - Redis cache for frequent queries
   - Reduce database hits

4. **Batch Processing**
   - Process multiple terms at once
   - Parallel normalization

5. **Web UI**
   - Interactive normalization interface
   - Confidence visualization

---

**Status**: ✅ **ALL 6 TIER 2 NORMALIZERS OPERATIONAL**

**Version**: 1.0.0
**Last Updated**: 2025-11-08
**Database Build**: 385,867 total records
