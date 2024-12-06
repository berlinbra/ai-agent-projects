# Claude Interaction Examples

This project demonstrates different ways to interact with Claude programmatically using Python.

## Features

1. Official API Integration
   - Uses Anthropic's official Python package
   - Requires API key from console.anthropic.com

2. Desktop App Integration
   - Uses PyAutoGUI for desktop automation
   - Simulates user interaction with the Claude desktop app

## Setup

1. Install required packages:
```bash
pip install anthropic pyautogui python-dotenv
```

2. Create a .env file with your configurations:
```
ANTHROPIC_API_KEY=your_api_key  # Only needed for official API
CLAUDE_WINDOW_TITLE=Claude       # Adjust based on your OS
```

## Usage

See individual script documentation for detailed usage instructions.

## Note

The desktop automation approach is experimental and may require adjustments based on your specific OS and screen configuration.