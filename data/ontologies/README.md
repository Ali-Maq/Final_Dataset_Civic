# Ontology Data Files

This directory contains downloaded ontology files used by the Tier 2 normalization agents.

## Contents

After running the download script, this directory will contain:

### OBO Format Files
- **doid.obo** (6.7 MB) - Disease Ontology
- **so.obo** (1.1 MB) - Sequence Ontology
- **go.obo** (34 MB) - Gene Ontology
- **hp.obo** (9.8 MB) - Human Phenotype Ontology
- **mondo.obo** (49 MB) - Monarch Disease Ontology

### ClinVar Data
- **clinvar_summary.txt** (3.5 GB) - ClinVar variant database

**Total Size**: ~3.6 GB

## How to Download

These files are NOT included in the Git repository due to their large size.

To download them, run:

```bash
cd /path/to/Final_Dataset_Civic
./scripts/download_ontologies.sh
```

The script will automatically download all 6 ontology files from their official sources.

## Data Sources

See `docs/LOCAL_ONTOLOGIES_SOURCES.md` for detailed information about:
- Download URLs
- Licenses
- Update frequencies
- File formats

## Next Steps

After downloading, build the SQLite database:

```bash
python3 src/normalizers/local_ontology_parsers.py
```

This will parse all OBO files and create a searchable database in `data/databases/ontologies.db`.

## Update Schedule

To keep ontologies current:
- **Monthly**: DOID, ClinVar, MONDO
- **Quarterly**: GO, HPO, SO

Re-run the download and build scripts to update.

## Notes

- These files are regeneratable and should NOT be committed to Git
- They are excluded via `.gitignore`
- Download takes ~5 minutes depending on internet speed
- Requires ~4 GB free disk space
