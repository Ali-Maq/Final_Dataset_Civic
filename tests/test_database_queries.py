"""
Test database queries to verify local ontology data
"""

import sqlite3

db_path = "data/databases/ontologies.db"

print("="*80)
print("DATABASE CONTENT VERIFICATION")
print("="*80)
print()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Count terms by ontology
print("📊 Terms by Ontology:")
print("-" * 80)
cursor.execute("SELECT ontology, COUNT(*) FROM terms GROUP BY ontology")
for row in cursor.fetchall():
    print(f"  {row[0]:10s}: {row[1]:>8,} terms")
print()

# Count variants
print("📊 Variants:")
print("-" * 80)
cursor.execute("SELECT COUNT(*) FROM variants")
count = cursor.fetchone()[0]
print(f"  ClinVar: {count:>8,} variants")
print()

# Search for seizure in HPO
print("🔍 Searching for 'seizure' in HPO:")
print("-" * 80)
cursor.execute("""
    SELECT term_id, name
    FROM terms
    WHERE ontology='HPO' AND name LIKE '%seizure%'
    LIMIT 10
""")
results = cursor.fetchall()
if results:
    for term_id, name in results:
        print(f"  {term_id}: {name}")
else:
    print("  No results found")
print()

# Search for EGFR in ClinVar
print("🔍 Searching for EGFR variants in ClinVar:")
print("-" * 80)
cursor.execute("""
    SELECT variation_id, name, gene_symbol
    FROM variants
    WHERE gene_symbol='EGFR'
    LIMIT 10
""")
results = cursor.fetchall()
if results:
    for var_id, name, gene in results:
        print(f"  {var_id}: {gene} {name}")
else:
    print("  No EGFR variants found")
print()

# Search for L858R in ClinVar
print("🔍 Searching for L858R variant in ClinVar:")
print("-" * 80)
cursor.execute("""
    SELECT variation_id, name, gene_symbol, clinical_significance
    FROM variants
    WHERE name LIKE '%L858R%' OR name LIKE '%Leu858Arg%'
    LIMIT 10
""")
results = cursor.fetchall()
if results:
    for var_id, name, gene, sig in results:
        print(f"  {var_id}: {gene} {name} ({sig})")
else:
    print("  No L858R variants found")
print()

# Check if we have any synonyms
print("📊 Synonyms:")
print("-" * 80)
cursor.execute("SELECT COUNT(*) FROM synonyms")
count = cursor.fetchone()[0]
print(f"  Total synonyms: {count:>8,}")
print()

# Sample HPO synonyms for seizure
print("🔍 HPO synonyms containing 'seizure':")
print("-" * 80)
cursor.execute("""
    SELECT t.term_id, t.name, s.synonym
    FROM terms t
    JOIN synonyms s ON t.term_id = s.term_id
    WHERE t.ontology = 'HPO' AND s.synonym LIKE '%seizure%'
    LIMIT 5
""")
results = cursor.fetchall()
if results:
    for term_id, name, synonym in results:
        print(f"  {term_id}: {name}")
        print(f"    Synonym: {synonym}")
else:
    print("  No synonyms found")
print()

conn.close()

print("="*80)
print("✅ Database verification complete")
print("="*80)
