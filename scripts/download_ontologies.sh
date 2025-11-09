#!/bin/bash
# OncoCITE Local Ontology Download Script
# Downloads essential ontologies for local normalization agents

set -e  # Exit on error

echo "========================================================================"
echo "OncoCITE - Downloading Local Ontologies for Tier 2 Normalization"
echo "========================================================================"
echo ""

# Create directories
mkdir -p data/ontologies
mkdir -p data/databases
mkdir -p data/indices

cd data/ontologies

#=========================================================================
# PHASE 1: Essential Ontologies (~200 MB total)
#=========================================================================

echo "📥 Phase 1: Downloading Essential Ontologies..."
echo ""

# 1. DOID (Disease Ontology) - ~15 MB
echo "[1/6] Downloading DOID (Disease Ontology)..."
if [ ! -f "doid.obo" ]; then
    wget -q --show-progress -O doid.obo \
        https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/main/src/ontology/doid.obo
    echo "✅ DOID downloaded successfully"
else
    echo "⏭️  DOID already exists, skipping"
fi
echo ""

# 2. SO (Sequence Ontology) - ~5 MB
echo "[2/6] Downloading SO (Sequence Ontology)..."
if [ ! -f "so.obo" ]; then
    wget -q --show-progress -O so.obo \
        https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/Ontology_Files/so.obo
    echo "✅ SO downloaded successfully"
else
    echo "⏭️  SO already exists, skipping"
fi
echo ""

# 3. GO (Gene Ontology) - ~100 MB
echo "[3/6] Downloading GO (Gene Ontology)..."
if [ ! -f "go.obo" ]; then
    wget -q --show-progress -O go.obo \
        http://purl.obolibrary.org/obo/go.obo
    echo "✅ GO downloaded successfully"
else
    echo "⏭️  GO already exists, skipping"
fi
echo ""

# 4. HPO (Human Phenotype Ontology) - ~20 MB
echo "[4/6] Downloading HPO (Human Phenotype Ontology)..."
if [ ! -f "hp.obo" ]; then
    wget -q --show-progress -O hp.obo \
        http://purl.obolibrary.org/obo/hp.obo
    echo "✅ HPO downloaded successfully"
else
    echo "⏭️  HPO already exists, skipping"
fi
echo ""

# 5. MONDO (Monarch Disease Ontology) - ~50 MB
echo "[5/6] Downloading MONDO (Monarch Disease Ontology)..."
if [ ! -f "mondo.obo" ]; then
    wget -q --show-progress -O mondo.obo \
        http://purl.obolibrary.org/obo/mondo.obo
    echo "✅ MONDO downloaded successfully"
else
    echo "⏭️  MONDO already exists, skipping"
fi
echo ""

# 6. ClinVar (Variant Summary) - ~1 GB compressed
echo "[6/6] Downloading ClinVar Variant Summary..."
if [ ! -f "clinvar_summary.txt" ]; then
    echo "⏳ This may take a few minutes (downloading ~1 GB)..."
    wget -q --show-progress -O clinvar_summary.txt.gz \
        https://ftp.ncbi.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
    echo "📦 Decompressing ClinVar..."
    gunzip clinvar_summary.txt.gz
    echo "✅ ClinVar downloaded and decompressed successfully"
else
    echo "⏭️  ClinVar already exists, skipping"
fi
echo ""

#=========================================================================
# Summary
#=========================================================================

echo "========================================================================"
echo "✅ DOWNLOAD COMPLETE"
echo "========================================================================"
echo ""
echo "Downloaded Ontologies:"
echo "  • DOID    (Disease Ontology)"
echo "  • SO      (Sequence Ontology)"
echo "  • GO      (Gene Ontology)"
echo "  • HPO     (Human Phenotype Ontology)"
echo "  • MONDO   (Monarch Disease Ontology)"
echo "  • ClinVar (Variant Database)"
echo ""

# Check sizes
echo "File Sizes:"
du -h doid.obo 2>/dev/null    || echo "  doid.obo: not found"
du -h so.obo 2>/dev/null      || echo "  so.obo: not found"
du -h go.obo 2>/dev/null      || echo "  go.obo: not found"
du -h hp.obo 2>/dev/null      || echo "  hp.obo: not found"
du -h mondo.obo 2>/dev/null   || echo "  mondo.obo: not found"
du -h clinvar_summary.txt 2>/dev/null || echo "  clinvar_summary.txt: not found"
echo ""

echo "Total Size:"
du -sh . 2>/dev/null || echo "  Unable to calculate"
echo ""

echo "========================================================================"
echo "Next Steps:"
echo "  1. Run: python build_local_databases.py"
echo "  2. This will parse ontologies and build searchable indices"
echo "========================================================================"
