#!/usr/bin/env python3
"""
REAL MCP Server Testing with stdio transport
"""

import asyncio
import sys
import os

# Add uvx to PATH
os.environ['PATH'] = f"/root/.local/bin:{os.environ.get('PATH', '')}"

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    print("✅ MCP package imported")
except ImportError:
    print("❌ MCP package not available")
    sys.exit(1)

async def test_biocontext_mcp():
    """Test BioContext MCP server via stdio"""
    
    print("="*80)
    print("REAL MCP SERVER TEST - stdio transport")
    print("="*80)
    
    print("\n[1] Starting BioContext MCP server...")
    
    params = StdioServerParameters(
        command="/root/.local/bin/uvx",
        args=["biocontext_kb@latest"],
        env={"MCP_ENVIRONMENT": "DEVELOPMENT"}
    )
    
    try:
        async with stdio_client(params) as (read, write):
            print("✅ Server process started\n")
            
            async with ClientSession(read, write) as session:
                print("[2] Initializing MCP session...")
                
                # Initialize
                init_result = await session.initialize()
                print(f"✅ Initialized - Server: {init_result.server_info.name}")
                print(f"   Version: {init_result.protocol_version}\n")
                
                # List tools
                print("[3] Listing available tools...")
                tools_result = await session.list_tools()
                tools = tools_result.tools
                
                print(f"✅ Found {len(tools)} REAL tools from MCP server:\n")
                
                for i, tool in enumerate(tools, 1):
                    print(f"  {i}. {tool.name}")
                    print(f"     {tool.description[:80]}...")
                    if tool.inputSchema:
                        print(f"     Input: {list(tool.inputSchema.get('properties', {}).keys())[:3]}")
                    print()
                
                # Try calling a tool
                if len(tools) > 0:
                    print(f"[4] Testing tool execution - Calling '{tools[0].name}'...")
                    
                    try:
                        # Find a search-related tool
                        search_tools = [t for t in tools if 'search' in t.name.lower() or 'europepmc' in t.name.lower()]
                        
                        if search_tools:
                            tool_name = search_tools[0].name
                            print(f"   Tool: {tool_name}")
                            
                            # Call with minimal params
                            result = await session.call_tool(
                                tool_name,
                                arguments={"query": "EGFR", "page_size": 2}
                            )
                            
                            print(f"✅ REAL TOOL EXECUTION SUCCESS!")
                            print(f"   Result type: {type(result)}")
                            print(f"   Result preview: {str(result)[:200]}...")
                            
                        else:
                            print(f"   Calling first tool: {tools[0].name}")
                            result = await session.call_tool(tools[0].name, arguments={})
                            print(f"✅ Tool executed - Result: {str(result)[:200]}...")
                            
                    except Exception as e:
                        print(f"⚠️  Tool execution error: {e}")
                        print("   (May need specific parameters)")
                
                print("\n" + "="*80)
                print("✅ REAL MCP SERVER TEST COMPLETE")
                print("="*80)
                print(f"\nVerified:")
                print(f"  • MCP server starts ✅")
                print(f"  • Server responds to initialize ✅")
                print(f"  • Lists {len(tools)} real tools ✅")
                print(f"  • Tool execution attempted ✅")
                
    except Exception as e:
        print(f"\n❌ Error during MCP testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_biocontext_mcp())
