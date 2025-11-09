# Local Ontology Data Sources for Tier 2 Normalization Agents

This document contains all download URLs and setup information for local ontology databases.

---

## Agent 9: Disease Normalizer

### DOID (Disease Ontology)
- **Format**: OBO
- **Download URL**: https://github.com/DiseaseOntology/HumanDiseaseOntology/raw/main/src/ontology/doid.obo
- **Alternative**: http://purl.obolibrary.org/obo/doid.owl
- **Size**: ~15 MB
- **Update Frequency**: Monthly
- **License**: CC0 1.0
- **Website**: https://disease-ontology.org/

### NCIt (NCI Thesaurus)
- **Format**: OWL
- **Download URL**: https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Thesaurus.OWL.zip
- **Alternative OBO**: http://purl.obolibrary.org/obo/ncit.owl
- **Size**: ~500 MB (compressed)
- **Update Frequency**: Monthly
- **License**: CC BY 4.0
- **Website**: https://evs.nci.nih.gov/

### ICD-O-3 (International Classification of Diseases for Oncology)
- **Format**: Tables/CSV
- **Download**: WHO website (registration may be required)
- **Alternative**: Use SEER ICD-O-3 mappings
- **URL**: https://seer.cancer.gov/icd-o-3/
- **Size**: ~2 MB
- **License**: Public domain (WHO)

### SNOMED CT
- **Format**: RF2 (Release Format 2)
- **Download**: Requires UMLS license (free)
- **URL**: https://www.nlm.nih.gov/healthit/snomedct/international.html
- **Size**: ~3 GB
- **License**: UMLS license
- **Note**: Large, complex. May use subset for cancer terms

---

## Agent 10: Variant Normalizer

### SO (Sequence Ontology)
- **Format**: OBO
- **Download URL**: https://github.com/The-Sequence-Ontology/SO-Ontologies/raw/master/Ontology_Files/so.obo
- **Alternative OWL**: http://purl.obolibrary.org/obo/so.owl
- **Size**: ~5 MB
- **Update Frequency**: As needed
- **License**: CC BY 4.0
- **Website**: http://www.sequenceontology.org/

### dbSNP
- **Format**: VCF, JSON
- **Download**: NCBI FTP
- **URL**: https://ftp.ncbi.nih.gov/snp/latest_release/
- **Size**: ~100 GB (full), can use subset
- **Update Frequency**: Regular
- **License**: Public domain
- **Note**: Very large, recommend using API or subset

### ClinVar
- **Format**: VCF, XML, TSV
- **Download URL**: https://ftp.ncbi.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
- **Size**: ~1 GB (compressed)
- **Update Frequency**: Monthly
- **License**: Public domain
- **Website**: https://www.ncbi.nlm.nih.gov/clinvar/

### HGVS
- **Type**: Validation rules (not a database)
- **Implementation**: Use hgvs Python library
- **Install**: `pip install hgvs`
- **Documentation**: https://github.com/biocommons/hgvs

---

## Agent 11: Therapy Normalizer

### NCIt (Drug Terms)
- **Same as Agent 9** - NCIt contains drug classifications
- **Filter**: Use drug hierarchy subset

### RxNorm
- **Format**: RRF (Rich Release Format)
- **Download**: UMLS Metathesaurus (free license required)
- **URL**: https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html
- **Size**: ~500 MB
- **Update Frequency**: Monthly
- **License**: UMLS license

### DrugBank
- **Format**: XML, CSV
- **Download**: https://go.drugbank.com/releases/latest
- **Size**: ~100 MB
- **License**: Free for academic use (registration required)
- **Alternative**: Use open data subset

### ATC (Anatomical Therapeutic Chemical)
- **Format**: Excel/Text
- **Download**: WHO Collaborating Centre
- **URL**: https://www.whocc.no/atc_ddd_index/
- **Size**: ~5 MB
- **License**: Free use
- **Website**: https://www.whocc.no/

---

## Agent 12: Trial Normalizer

### ClinicalTrials.gov
- **Format**: JSON API
- **API URL**: https://clinicaltrials.gov/api/query/
- **Download**: Can cache entire database
- **Bulk Download**: https://clinicaltrials.gov/api/gui/ref/api_urls
- **Size**: ~5 GB (all trials)
- **Update**: Daily
- **License**: Public domain

### EudraCT
- **Format**: Web scraping or API
- **URL**: https://www.clinicaltrialsregister.eu/
- **Note**: No official bulk download
- **Alternative**: Focus on ClinicalTrials.gov which includes EU trials

---

## Agent 13: Coordinate Normalizer

### Reference Genomes (hg38, hg19)
- **Format**: FASTA
- **hg38 URL**: https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz
- **hg19 URL**: https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/hg19.fa.gz
- **Size**: ~3 GB each (compressed)
- **License**: Public domain

### RefSeq Transcripts
- **Format**: GFF, GTF
- **Download**: NCBI RefSeq
- **URL**: https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/
- **Size**: ~500 MB
- **Update**: Regular
- **License**: Public domain

### Ensembl Transcripts
- **Format**: GTF, GFF3
- **Download**: Ensembl FTP
- **URL**: https://ftp.ensembl.org/pub/current_gtf/homo_sapiens/
- **Size**: ~1 GB
- **Update**: Regular releases
- **License**: Public domain
- **Website**: https://www.ensembl.org/

### MANE (Matched Annotation from NCBI and EMBL-EBI)
- **Format**: GFF3
- **Download**: https://ftp.ncbi.nlm.nih.gov/refseq/MANE/MANE_human/current/
- **Size**: ~50 MB
- **Purpose**: Gold standard transcript set
- **License**: Public domain

---

## Agent 14: Ontology Normalizer

### GO (Gene Ontology)
- **Format**: OBO
- **Download URL**: http://purl.obolibrary.org/obo/go.obo
- **Alternative**: http://current.geneontology.org/ontology/go.obo
- **Size**: ~100 MB
- **Update**: Regular
- **License**: CC BY 4.0
- **Website**: https://geneontology.org/

### HPO (Human Phenotype Ontology)
- **Format**: OBO
- **Download URL**: http://purl.obolibrary.org/obo/hp.obo
- **Alternative OWL**: http://purl.obolibrary.org/obo/hp.owl
- **Size**: ~20 MB
- **Update**: Regular
- **License**: Custom (free for research)
- **Website**: https://hpo.jax.org/

### MONDO (Monarch Disease Ontology)
- **Format**: OBO, OWL, JSON
- **Download URL**: http://purl.obolibrary.org/obo/mondo.obo
- **Alternative**: https://github.com/monarch-initiative/mondo/releases
- **Size**: ~50 MB
- **Update**: Monthly
- **License**: CC BY 4.0
- **Website**: https://mondo.monarchinitiative.org/

### KEGG Pathways
- **Format**: KGML, Text
- **API**: https://rest.kegg.jp/
- **Download**: Via API (no bulk download)
- **License**: Academic use free
- **Website**: https://www.genome.jp/kegg/

### Reactome Pathways
- **Format**: BioPAX, SBML, Various
- **Download**: https://reactome.org/download-data
- **Size**: ~500 MB
- **License**: CC BY 4.0
- **Website**: https://reactome.org/

---

## Storage Requirements

### Minimum Setup (Essential ontologies only):
- DOID: 15 MB
- SO: 5 MB
- GO: 100 MB
- HPO: 20 MB
- ClinVar: 1 GB
- **Total**: ~1.2 GB

### Full Setup (All databases):
- Ontologies: ~200 MB
- ClinVar: 1 GB
- RxNorm: 500 MB
- NCIt: 500 MB
- RefSeq/Ensembl: 1.5 GB
- ClinicalTrials cache: 5 GB
- **Total**: ~8-10 GB

### Large Optional (if needed):
- dbSNP full: 100 GB
- SNOMED CT: 3 GB
- Reference genomes: 6 GB

---

## Update Strategy

### Daily Updates:
- ClinicalTrials.gov (via API)

### Monthly Updates:
- DOID, NCIt, ClinVar, RxNorm

### Quarterly Updates:
- GO, HPO, MONDO, RefSeq, Ensembl

### As Needed:
- Sequence Ontology, KEGG, Reactome

---

## Implementation Priority

### Phase 1 (Core - Implement First):
1. ✅ DOID (Disease Ontology)
2. ✅ SO (Sequence Ontology)
3. ✅ GO (Gene Ontology)
4. ✅ HPO (Human Phenotype Ontology)

### Phase 2 (Important):
5. ✅ ClinVar
6. ✅ NCIt subset (cancer terms + drugs)

### Phase 3 (Enhanced):
7. ⏸️ RxNorm (requires UMLS license)
8. ⏸️ RefSeq/Ensembl transcripts
9. ⏸️ ClinicalTrials.gov cache

### Phase 4 (Optional):
10. ⏸️ SNOMED CT (requires UMLS license)
11. ⏸️ dbSNP (very large)
12. ⏸️ Reference genomes

---

## Download Script Strategy

```bash
#!/bin/bash
# Quick download script for essential ontologies

mkdir -p data/ontologies

# DOID
wget -O data/ontologies/doid.obo \
  https://github.com/DiseaseOntology/HumanDiseaseOntology/raw/main/src/ontology/doid.obo

# SO
wget -O data/ontologies/so.obo \
  https://github.com/The-Sequence-Ontology/SO-Ontologies/raw/master/Ontology_Files/so.obo

# GO
wget -O data/ontologies/go.obo \
  http://purl.obolibrary.org/obo/go.obo

# HPO
wget -O data/ontologies/hp.obo \
  http://purl.obolibrary.org/obo/hp.obo

# MONDO
wget -O data/ontologies/mondo.obo \
  http://purl.obolibrary.org/obo/mondo.obo

# ClinVar
wget -O data/ontologies/clinvar_summary.txt.gz \
  https://ftp.ncbi.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
gunzip data/ontologies/clinvar_summary.txt.gz

echo "Essential ontologies downloaded successfully!"
```

---

## Python Libraries for Parsing

```python
# OBO format
pip install pronto  # Best for OBO/OWL parsing

# Alternative parsers
pip install owlready2  # OWL parsing
pip install fastobo    # Fast OBO parser

# Variant nomenclature
pip install hgvs       # HGVS validation

# Bio utilities
pip install biopython  # General bio parsing
```

---

## Next Steps

1. Create download scripts for each agent
2. Build OBO/OWL parsers
3. Create SQLite databases for fast lookup
4. Implement fuzzy matching for term normalization
5. Build API wrappers for each normalizer agent
