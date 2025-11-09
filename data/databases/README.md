# Database Files

This directory contains the SQLite database built from downloaded ontology files.

## Contents

After running the database builder, this directory will contain:

- **ontologies.db** (~200 MB) - SQLite database with indexed ontology data

## Database Schema

The database contains 5 tables:

### 1. terms
Stores ontology terms from DOID, SO, GO, HPO, MONDO
- **116,748 records**
- Fields: term_id, ontology, name, definition, is_obsolete

### 2. synonyms
Stores alternative names for terms
- **308,676 records**
- Fields: term_id, synonym

### 3. xrefs
Stores cross-references to other databases
- Fields: term_id, xref

### 4. relationships
Stores parent-child relationships (is_a)
- Fields: child_term_id, parent_term_id

### 5. variants
Stores ClinVar variant data
- **251,716 records**
- Fields: variation_id, name, gene_symbol, clinical_significance, rs_id, chromosome, position, ref_allele, alt_allele, type

**Total Records**: 385,867

## How to Build

This database is NOT included in the Git repository due to its size (200 MB).

To build it:

### Step 1: Download Ontologies

```bash
./scripts/download_ontologies.sh
```

### Step 2: Build Database

```bash
python3 src/normalizers/local_ontology_parsers.py
```

Build time: ~2 minutes

## Verification

To verify the database was built correctly:

```bash
python3 tests/test_database_queries.py
```

Expected output:
```
✅ 116,748 ontology terms loaded
✅ 251,716 ClinVar variants loaded
✅ 308,676 synonyms loaded
```

## Performance

With proper indices, queries are very fast:
- Exact match: <5 ms
- Synonym lookup: <10 ms
- Fuzzy search: <20 ms

## Rebuilding

To rebuild the database (e.g., after updating ontologies):

```bash
rm data/databases/ontologies.db
python3 src/normalizers/local_ontology_parsers.py
```

## Notes

- This file is regeneratable and should NOT be committed to Git
- It is excluded via `.gitignore`
- The database uses SQLite FTS5 for fast text search
- All tables are indexed for optimal query performance
- The database is read-only for normalizer agents (no writes during normalization)

## Usage

The database is used by all 6 Tier 2 normalizer agents:

```python
from src.normalizers.local_normalizers import normalize_disease

result = normalize_disease("lung adenocarcinoma")
# Queries: data/databases/ontologies.db
```

See `docs/LOCAL_TIER2_README.md` for detailed usage examples.
