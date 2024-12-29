import json
import subprocess
import os
import pyautogui
import time
import pyperclip
from typing import Optional

class ClaudeDesktop:
    def __init__(self):
        # Define paths
        self.config_path = os.path.expandvars(r'%APPDATA%\\Claude\\claude_desktop_config.json')
        self.exe_path = r'C:\\Users\\psnbm\\AppData\\Local\\AnthropicClaude\\claude.exe'

        # Add a safety delay for pyautogui
        pyautogui.PAUSE = 0.5  # Reduced from 1 to 0.5 for better responsiveness
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

    def new_chat(self, retry_count: int = 3):
        """Start a new chat using keyboard shortcut
        
        Args:
            retry_count (int): Number of times to retry if the operation fails
        """
        for attempt in range(retry_count):
            try:
                pyautogui.hotkey('ctrl', 'alt', 'space')
                time.sleep(1.5)  # Increased wait time for new chat initialization
                return True
            except Exception as e:
                if attempt == retry_count - 1:  # Last attempt
                    raise Exception(f"Failed to start new chat after {retry_count} attempts: {str(e)}")
                time.sleep(1)  # Wait before retrying

    def send_prompt(self, prompt: str, chunk_size: Optional[int] = None, retry_count: int = 3):
        """Send a prompt to Claude using clipboard for reliability
        
        Args:
            prompt (str): The prompt to send
            chunk_size (Optional[int]): Size of chunks to split text into if needed
            retry_count (int): Number of times to retry if the operation fails
        """
        original_clipboard = pyperclip.paste()  # Save original clipboard content
        
        try:
            if chunk_size and len(prompt) > chunk_size:
                # Split into chunks if needed
                chunks = [prompt[i:i + chunk_size] for i in range(0, len(prompt), chunk_size)]
                for chunk in chunks:
                    self._paste_text(chunk, retry_count)
                    time.sleep(0.5)  # Wait between chunks
            else:
                self._paste_text(prompt, retry_count)
            
            # Send the message
            time.sleep(0.3)  # Short wait before pressing enter
            pyautogui.press('enter')
            
        finally:
            # Restore original clipboard content
            pyperclip.copy(original_clipboard)
    
    def _paste_text(self, text: str, retry_count: int = 3):
        """Helper method to paste text using clipboard
        
        Args:
            text (str): Text to paste
            retry_count (int): Number of retry attempts
        """
        for attempt in range(retry_count):
            try:
                # Copy to clipboard
                pyperclip.copy(text)
                time.sleep(0.2)  # Wait for clipboard
                
                # Paste using Ctrl+V
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.2)  # Wait for paste to complete
                return
            except Exception as e:
                if attempt == retry_count - 1:  # Last attempt
                    raise Exception(f"Failed to paste text after {retry_count} attempts: {str(e)}")
                time.sleep(1)  # Wait before retrying


# Example usage
if __name__ == "__main__":
    claude = ClaudeDesktop()

    # Launch Claude
    claude.launch()

    # Wait for app to fully load
    time.sleep(2)  # Increased initial load time
    claude.new_chat()
    time.sleep(1)

    # Send a prompt - using chunk_size for very long prompts
    claude.send_prompt("Tell me the weather today", chunk_size=1000)  # Will split if > 1000 chars