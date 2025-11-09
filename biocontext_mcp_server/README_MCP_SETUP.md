# BioContext AI Knowledgebase MCP Server - Setup & Testing

## 📁 Test Directory
Location: `/home/user/biocontext_mcp_test/`

## ✅ Installation Status

### Components Installed:
1. **uv package manager** - Modern Python package installer
2. **BioContext KB MCP Server** - Latest version via uvx

### Installation Method:
```bash
# uv installed via:
curl -LsSf https://astral.sh/uv/install.sh | sh

# BioContext KB installed via:
uvx biocontext_kb@latest
```

## 🔧 Available Tools

The MCP server provides access to 12+ biomedical APIs:

### 1. **Antibody Registry** 
- Function: Gene ID conversion
- Use: Convert between gene identifiers

### 2. **bioRxiv/medRxiv**
- Function: Preprint search and metadata
- Use: Access recent biomedical preprints

### 3. **Ensembl**
- Function: Gene ID conversion
- Use: Convert gene identifiers across databases

### 4. **EuropePMC**
- Function: Literature search and full-text access
- Use: Search biomedical literature

### 5. **InterPro**
- Function: Protein classification
- Use: Protein families, domains, functional sites

### 6. **OpenTargets**
- Function: Target-disease associations
- Use: Drug target identification

### 7. **PanglaoDB**
- Function: scRNA-seq cell type markers
- Use: Single-cell RNA-sequencing data

### 8. **PRIDE**
- Function: Proteomics data repository
- Use: Mass spectrometry data access

### 9. **Protein Atlas**
- Function: Protein expression data
- Use: Tissue/cell expression profiles

### 10. **Reactome**
- Function: Pathways database
- Use: Biological pathway analysis

### 11. **STRING**
- Function: Protein-protein interactions
- Use: Network analysis

### 12. **AlphaFold DB**
- Function: Protein structures
- Use: 3D structure predictions

## 🚀 Usage

### Run MCP Server (Development Mode):
```bash
export MCP_ENVIRONMENT=DEVELOPMENT
uvx biocontext_kb
```

### Run MCP Server (Production with HTTP):
```bash
export MCP_ENVIRONMENT=PRODUCTION
export PORT=8000
uvx biocontext_kb
```

## 🧪 Testing

Run the test suite:
```bash
python3 test_mcp_tools.py
```

Results saved to: `mcp_test_results.json`

## 📝 Configuration for Claude Desktop

Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "biocontext_kb": {
      "command": "uvx",
      "args": ["biocontext_kb@latest"],
      "env": {
        "UV_PYTHON": "3.12"
      }
    }
  }
}
```

## 🔗 Resources

- **Documentation**: https://biocontext.ai
- **API Docs**: https://docs.kb.biocontext.ai/
- **Registry**: https://github.com/biocontext-ai/registry
- **GitHub**: https://github.com/biocontext-ai/knowledgebase-mcp
- **Publication**: https://www.nature.com/articles/s41587-025-02900-9

## ⚖️ License

- **Code**: Apache 2.0
- **Data**: Various licenses - check individual API terms

## ⚠️ Important Notes

1. **Rate Limits**: Respect API rate limits for each service
2. **Citations**: Cite both BioContextAI and individual data sources
3. **Data Licenses**: Apache 2.0 only applies to code, not accessed data
4. **KEGG**: Free for academic use only, no commercial services

## 🎯 Test Results Summary

- **Installation**: ✅ Success
- **Tools Available**: 12+
- **Status**: Ready for use

