# Claude MCP Server Implementation

This project implements a custom MCP (Model Context Protocol) server that provides similar functionality to the chat interface, allowing Claude to access external functions.

## Setup

1. Install dependencies:
```bash
pip install fastapi uvicorn anthropic python-dotenv
```

2. Set up your environment variables in a .env file:
```
ANTHROPIC_API_KEY=your_api_key
```

3. Add the server configuration to your Claude desktop config file (usually located at `~/.claude-config.json` or similar):
```json
{
  "servers": [
    {
      "name": "custom",
      "url": "http://localhost:8000"
    }
  ]
}
```

## Running the Server

```bash
python mcp_server.py
```

## Available Functions

The server implements several functions similar to those available in the chat interface:
- Web search
- GitHub integration
- File operations

## Note

This is an experimental implementation and may need adjustments based on your specific needs and setup.