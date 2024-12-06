import json
import subprocess
import os
import pyautogui
import time

class ClaudeDesktop:
    def __init__(self):
        # Define paths
        self.config_path = os.path.expandvars(r'%APPDATA%\Claude\claude_desktop_config.json')
        self.exe_path = r'C:\Users\psnbm\AppData\Local\AnthropicClaude\claude.exe'

        # Add a safety delay for pyautogui
        pyautogui.PAUSE = 1
        # Enable fail-safe (move mouse to corner to abort)
        pyautogui.FAILSAFE = True
        
    def update_token(self, server: str, token: str, env_var: str):
        """Update a specific MCP server token"""
        with open(self.config_path, 'r') as f:
            config = json.load(f)
            
        if server in config['mcpServers']:
            config['mcpServers'][server]['env'][env_var] = token
            
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent='\t')
            
    def launch(self):
        """Launch Claude desktop"""
        subprocess.Popen([self.exe_path])

    def new_chat(self):
        """Start a new chat using Ctrl+N"""
        pyautogui.hotkey('ctrl', 'alt', 'space')
        time.sleep(1)  # Wait for new chat to initialize

    def send_prompt(self, prompt: str):
        """Send a prompt to Claude"""
        # Type the prompt
        pyautogui.write(prompt)
        # Press Enter to send
        pyautogui.press('enter')


# Example usage
claude = ClaudeDesktop()

# Update tokens if needed
# claude.update_token('github', 'new_token', 'GITHUB_PERSONAL_ACCESS_TOKEN')
# claude.update_token('brave-search', 'new_token', 'BRAVE_API_KEY')

# Launch Claude
claude.launch()

# Wait for app to fully load
time.sleep(1)  # Adjust this delay as needed
claude.new_chat()
time.sleep(1)

# Send the weather prompt
claude.send_prompt("Tell me the weather today")