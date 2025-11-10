#!/usr/bin/env python3
"""
REAL MCP Integration Test with OpenAI Agents SDK
Tests actual BioContext MCP server with real API calls
"""

import asyncio
import os
from pathlib import Path

# First, let's check if we have the required packages
try:
    from agents import Agent, Runner
    from agents.mcp import MCPServerStdio
    from agents.model_settings import ModelSettings
    print("✅ OpenAI Agents SDK imported successfully")
except ImportError as e:
    print(f"❌ Missing OpenAI Agents SDK: {e}")
    print("Installing openai-agents-sdk...")
    import subprocess
    subprocess.run(["pip", "install", "openai-agents-sdk"], check=True)
    from agents import Agent, Runner
    from agents.mcp import MCPServerStdio
    from agents.model_settings import ModelSettings

async def test_mcp_server_stdio():
    """Test BioContext MCP server via stdio transport"""
    
    print("="*80)
    print("REAL MCP SERVER INTEGRATION TEST")
    print("="*80)
    
    # Test 1: Start MCP server via stdio
    print("\n[Test 1] Starting BioContext MCP server via stdio...")
    
    try:
        async with MCPServerStdio(
            name="BioContext KB",
            params={
                "command": "uvx",
                "args": ["biocontext_kb@latest"],
                "env": {
                    "MCP_ENVIRONMENT": "DEVELOPMENT",
                    "PATH": os.environ.get("PATH", "")
                }
            },
            cache_tools_list=True,
        ) as server:
            
            print("✅ MCP server started successfully\n")
            
            # Test 2: List available tools
            print("[Test 2] Listing available tools from MCP server...")
            tools = await server.list_tools()
            print(f"✅ Found {len(tools)} tools from MCP server:")
            for i, tool in enumerate(tools[:5], 1):  # Show first 5
                print(f"  {i}. {tool.name} - {tool.description[:60]}...")
            
            print(f"\nTotal tools: {len(tools)}")
            
            # Test 3: Create agent with MCP tools
            print("\n[Test 3] Creating agent with MCP tools...")
            
            # Check if OpenAI API key is set
            if not os.environ.get("OPENAI_API_KEY"):
                print("⚠️  OPENAI_API_KEY not set - skipping agent tests")
                print("   Set it with: export OPENAI_API_KEY='your-key'")
                return
            
            agent = Agent(
                name="BioMedical Assistant",
                instructions="Use the BioContext MCP tools to answer biomedical questions.",
                mcp_servers=[server],
                model_settings=ModelSettings(
                    model="gpt-4",
                    tool_choice="auto"
                )
            )
            
            print("✅ Agent created with MCP tools\n")
            
            # Test 4: Run a simple query
            print("[Test 4] Testing real query: 'What is EGFR gene?'")
            result = await Runner.run(
                agent,
                "Look up information about the EGFR gene using the available tools."
            )
            
            print(f"✅ Query completed!")
            print(f"Response: {result.final_output[:200]}...\n")
            
            # Test 5: Test another tool
            print("[Test 5] Testing literature search: 'EGFR mutations'")
            result2 = await Runner.run(
                agent,
                "Search for recent papers about EGFR mutations in cancer."
            )
            
            print(f"✅ Literature search completed!")
            print(f"Response: {result2.final_output[:200]}...\n")
            
            print("="*80)
            print("✅ ALL REAL MCP TESTS PASSED")
            print("="*80)
            
    except Exception as e:
        print(f"❌ Error during MCP testing: {e}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    asyncio.run(test_mcp_server_stdio())
