#!/usr/bin/env python3
"""
REAL API Testing - Direct calls to biomedical APIs
"""

import requests
import json

def test_europepmc():
    """Test EuropePMC API directly"""
    print("\n[1] Testing EuropePMC - Literature Search")
    print("="*70)
    
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    params = {
        "query": "EGFR L858R mutation lung cancer",
        "format": "json",
        "pageSize": 3
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if "resultList" in data and "result" in data["resultList"]:
            results = data["resultList"]["result"]
            print(f"✅ REAL API RESPONSE - Found {len(results)} papers:")
            
            for i, paper in enumerate(results, 1):
                print(f"\n  Paper {i}:")
                print(f"    Title: {paper.get('title', 'N/A')[:80]}...")
                print(f"    PMID: {paper.get('pmid', 'N/A')}")
                print(f"    Journal: {paper.get('journalTitle', 'N/A')}")
                print(f"    Year: {paper.get('pubYear', 'N/A')}")
            
            return True
        else:
            print(f"❌ Unexpected response format")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_ensembl():
    """Test Ensembl API directly"""
    print("\n[2] Testing Ensembl - Gene Lookup")
    print("="*70)
    
    gene_id = "ENSG00000146648"  # EGFR
    url = f"https://rest.ensembl.org/lookup/id/{gene_id}"
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        
        print(f"✅ REAL API RESPONSE - Gene Data:")
        print(f"    Gene ID: {data.get('id', 'N/A')}")
        print(f"    Symbol: {data.get('display_name', 'N/A')}")
        print(f"    Description: {data.get('description', 'N/A')[:80]}...")
        print(f"    Chromosome: {data.get('seq_region_name', 'N/A')}")
        print(f"    Start: {data.get('start', 'N/A'):,}")
        print(f"    End: {data.get('end', 'N/A'):,}")
        print(f"    Strand: {data.get('strand', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_string():
    """Test STRING API directly"""
    print("\n[3] Testing STRING - Protein Interactions")
    print("="*70)
    
    url = "https://string-db.org/api/json/network"
    params = {
        "identifiers": "EGFR",
        "species": 9606,  # Human
        "limit": 5
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        print(f"✅ REAL API RESPONSE - Found {len(data)} interactions:")
        
        for i, interaction in enumerate(data[:5], 1):
            print(f"\n  Interaction {i}:")
            print(f"    {interaction.get('preferredName_A', 'N/A')} <-> {interaction.get('preferredName_B', 'N/A')}")
            print(f"    Score: {interaction.get('score', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_opentargets():
    """Test OpenTargets API"""
    print("\n[4] Testing OpenTargets - Target-Disease Associations")
    print("="*70)
    
    # GraphQL query
    query = """
    query targetInfo {
      target(ensemblId: "ENSG00000146648") {
        id
        approvedSymbol
        approvedName
      }
    }
    """
    
    url = "https://api.platform.opentargets.org/api/v4/graphql"
    
    try:
        response = requests.post(
            url,
            json={"query": query},
            timeout=10
        )
        data = response.json()
        
        if "data" in data and "target" in data["data"]:
            target = data["data"]["target"]
            print(f"✅ REAL API RESPONSE - Target Info:")
            print(f"    ID: {target.get('id', 'N/A')}")
            print(f"    Symbol: {target.get('approvedSymbol', 'N/A')}")
            print(f"    Name: {target.get('approvedName', 'N/A')}")
            return True
        else:
            print(f"❌ Unexpected response")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_protein_atlas():
    """Test Human Protein Atlas API"""
    print("\n[5] Testing Protein Atlas - Expression Data")
    print("="*70)
    
    url = "https://www.proteinatlas.org/api/search_download.php"
    params = {
        "search": "EGFR",
        "format": "json",
        "columns": "g,eg,up",
        "compress": "no"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        # Parse TSV response
        lines = response.text.strip().split('\n')
        if len(lines) > 1:
            headers = lines[0].split('\t')
            data = lines[1].split('\t')
            
            print(f"✅ REAL API RESPONSE - Protein Info:")
            for i, header in enumerate(headers):
                if i < len(data):
                    print(f"    {header}: {data[i]}")
            
            return True
        else:
            print(f"❌ No data returned")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("="*70)
    print("REAL BIOMEDICAL API TESTING")
    print("="*70)
    
    results = {
        "EuropePMC": test_europepmc(),
        "Ensembl": test_ensembl(),
        "STRING": test_string(),
        "OpenTargets": test_opentargets(),
        "Protein Atlas": test_protein_atlas()
    }
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    for api, success in results.items():
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{api:20s}: {status}")
    
    total = len(results)
    passed = sum(results.values())
    print(f"\nTotal: {passed}/{total} APIs working with REAL data")
