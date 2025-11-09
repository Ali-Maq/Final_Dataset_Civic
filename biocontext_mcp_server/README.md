# BioContext AI Knowledgebase MCP Server

This folder contains the complete setup, testing, and documentation for the BioContext AI Knowledgebase MCP server.

## 📁 Contents

```
biocontext_mcp_server/
├── README.md                              # This file
├── README_MCP_SETUP.md                    # Complete setup guide
├── FINAL_MCP_STATUS.md                    # Status summary
├── COMPREHENSIVE_TEST_REPORT.md           # Full test report
├── test_mcp_tools.py                      # Initial test script
├── comprehensive_tool_tests.py            # Full test suite (35 tests)
├── mcp_test_results.json                  # Initial results
└── comprehensive_test_results.json        # Detailed results
```

## 🚀 Quick Start

### Installation
```bash
# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install BioContext KB MCP Server
uvx biocontext_kb@latest
```

### Run Server

**Development Mode (stdio):**
```bash
export MCP_ENVIRONMENT=DEVELOPMENT
uvx biocontext_kb
```

**Production Mode (HTTP on port 8000):**
```bash
export MCP_ENVIRONMENT=PRODUCTION
export PORT=8000
uvx biocontext_kb
```

### Run Tests
```bash
python3 comprehensive_tool_tests.py
```

## ✅ Status

- **Tools Available**: 12/12 (100%)
- **Test Cases**: 35 comprehensive tests
- **Status**: FULLY OPERATIONAL

## 🔧 Available Tools

1. **Antibody Registry** - Gene ID conversion
2. **bioRxiv/medRxiv** - Preprint search
3. **Ensembl** - Gene data lookup
4. **EuropePMC** - Literature search
5. **InterPro** - Protein domains
6. **OpenTargets** - Target-disease associations
7. **PanglaoDB** - scRNA-seq cell markers
8. **PRIDE** - Proteomics datasets
9. **Protein Atlas** - Protein expression
10. **Reactome** - Biological pathways
11. **STRING** - Protein interactions
12. **AlphaFold DB** - Protein structures

## 📖 Documentation

- **Setup Guide**: [README_MCP_SETUP.md](README_MCP_SETUP.md)
- **Test Report**: [COMPREHENSIVE_TEST_REPORT.md](COMPREHENSIVE_TEST_REPORT.md)
- **Status Summary**: [FINAL_MCP_STATUS.md](FINAL_MCP_STATUS.md)

## 🔗 Resources

- **Documentation**: https://biocontext.ai
- **API Docs**: https://docs.kb.biocontext.ai/
- **GitHub**: https://github.com/biocontext-ai/knowledgebase-mcp
- **Publication**: Nature Biotechnology (2025)

## 🎯 Integration

### Claude Desktop
Edit `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "biocontext_kb": {
      "command": "uvx",
      "args": ["biocontext_kb@latest"],
      "env": {"UV_PYTHON": "3.12"}
    }
  }
}
```

### VS Code / Cursor / WindSurf
Edit `.vscode/mcp.json`:
```json
{
  "mcpServers": {
    "biocontext_kb": {
      "command": "uvx",
      "args": ["biocontext_kb@latest"]
    }
  }
}
```

## ⚖️ License

- **Code**: Apache 2.0
- **Data**: Various licenses (check individual API terms)

See [README_MCP_SETUP.md](README_MCP_SETUP.md) for detailed licensing information.

---

*Last Updated: 2025-11-09*
