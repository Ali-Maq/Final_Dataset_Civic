#!/usr/bin/env python3
"""
REAL MCP Protocol Testing
Actually communicate with MCP server using JSON-RPC protocol
"""

import subprocess
import json
import sys
import time

def send_mcp_request(process, method, params=None):
    """Send JSON-RPC request to MCP server via stdin"""
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {}
    }
    
    request_str = json.dumps(request) + "\n"
    process.stdin.write(request_str)
    process.stdin.flush()
    
    # Read response
    response_line = process.stdout.readline()
    if response_line:
        return json.loads(response_line)
    return None

def test_mcp_server():
    """Test MCP server with actual protocol communication"""
    
    print("="*80)
    print("REAL MCP PROTOCOL TEST")
    print("="*80)
    
    print("\n[1] Starting MCP server via stdio...")
    
    try:
        # Start MCP server
        process = subprocess.Popen(
            ["uvx", "biocontext_kb@latest"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            env={"MCP_ENVIRONMENT": "DEVELOPMENT"}
        )
        
        print(f"✅ Server started (PID: {process.pid})")
        time.sleep(2)  # Let server initialize
        
        # Test 1: Initialize
        print("\n[2] Sending 'initialize' request...")
        response = send_mcp_request(process, "initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        })
        
        if response:
            print(f"✅ Initialize response received")
            print(f"   Server: {response.get('result', {}).get('serverInfo', {}).get('name', 'Unknown')}")
        
        # Test 2: List tools
        print("\n[3] Sending 'tools/list' request...")
        response = send_mcp_request(process, "tools/list")
        
        if response and 'result' in response:
            tools = response['result'].get('tools', [])
            print(f"✅ Got {len(tools)} tools!")
            print("\n   Available tools:")
            for i, tool in enumerate(tools[:10], 1):
                print(f"   {i}. {tool.get('name', 'Unknown')} - {tool.get('description', '')[:60]}")
            
            if len(tools) > 10:
                print(f"   ... and {len(tools) - 10} more")
        
        # Test 3: Call a tool
        if tools:
            print("\n[4] Calling first tool as test...")
            first_tool = tools[0]
            print(f"   Tool: {first_tool.get('name')}")
            
            response = send_mcp_request(process, "tools/call", {
                "name": first_tool.get('name'),
                "arguments": {}
            })
            
            if response:
                print(f"✅ Tool call response received")
                if 'result' in response:
                    print(f"   Result preview: {str(response['result'])[:200]}")
        
        print("\n" + "="*80)
        print("✅ REAL MCP PROTOCOL TEST COMPLETE")
        print("="*80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if 'process' in locals():
            process.terminate()
            process.wait(timeout=5)
            print("\n[Cleanup] Server stopped")

if __name__ == "__main__":
    test_mcp_server()
