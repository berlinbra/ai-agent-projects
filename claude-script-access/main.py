import json
import subprocess
import os
import pyautogui
import time
from PIL import ImageGrab, Image
import cv2
import numpy as np
import pyperclip
from typing import Optional

class ClaudeDesktop:
    def __init__(self):
        self.config_path = os.path.expandvars(r'%APPDATA%\\Claude\\claude_desktop_config.json')
        self.exe_path = r'C:\\Users\\psnbm\\AppData\\Local\\AnthropicClaude\\claude.exe'

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.allow_button_path = os.path.join(self.script_dir, 'allow_button.png')
        self.chat_button_path = os.path.join(self.script_dir, 'chat_button.png')
        
        # Add a safety delay for pyautogui
        pyautogui.PAUSE = 0.5  # Reduced from 1 to 0.5 for better responsiveness
        pyautogui.FAILSAFE = True
        
    def launch(self):
        """Launch Claude desktop"""
        subprocess.Popen([self.exe_path])
        time.sleep(3)
        
    def new_chat(self):
        """Start a new chat using Ctrl+Alt+Space"""
        pyautogui.hotkey('ctrl', 'alt', 'space')
        time.sleep(1)
        # Clear any existing text
        pyautogui.hotkey('ctrl', 'a')

    def check_for_permission_dialog(self, timeout=2):
        """Check if the permission dialog is visible"""
        start_time = time.time()
        print("checking for dialog")
        while time.time() - start_time < timeout:
            try:
                # Look for the chat permission text/button
                chat_button = pyautogui.locateOnScreen(self.chat_button_path, confidence=0.8)
                if chat_button:
                    return True
            except Exception as e:
                print(f"Error checking for chat button: {e}")
            time.sleep(0.2)
        return False

    def handle_permissions(self, timeout=10):
        """Look for and click 'Allow for This Chat' button"""
        start_time = time.time()
        while self.check_for_permission_dialog():
            try:
                # Look for button by text
                print(f"Looking for button image at: {self.allow_button_path}")
                allow_button = pyautogui.locateOnScreen(self.allow_button_path, confidence=0.8)
                if allow_button:
                    pyautogui.click(allow_button)
                    time.sleep(0.5)
                    return True
            except Exception as e:
                print(f"Error looking for button: {e}")
            time.sleep(0.5)
        return False

    def create_github_project(self, project_name: str, description: str, owner: str):
        """Ask Claude to create a new GitHub project"""
        prompt = f"""Create a new GitHub project with the following details:
        Project Instructions: {project_name}
        Description: {description}
        Owner: {owner}
        
        Please initialize it with a basic structure including:
        - Code for program
        - README.md
        - .gitignore
        
        Use the GitHub MCP to create this project."""

        self.send_prompt(prompt)
        # Handle both GitHub and general permissions
        self.handle_permissions()
        time.sleep(2)  # Wait a bit in case of multiple permission requests
        self.handle_permissions()

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
            
        # Check for permissions popup after sending prompt
        self.handle_permissions()

# Example usage
if __name__ == "__main__":
    claude = ClaudeDesktop()

    # Launch Claude
    claude.launch()

    # Start a new chat
    claude.new_chat()

    # Create a GitHub project
    claude.create_github_project(
        "Create a python project that is a game of battleship",
        "battleships-test",
        "berlinbra"
    )