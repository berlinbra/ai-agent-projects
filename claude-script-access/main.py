import json
import subprocess
import os
import pyautogui
import time
from PIL import ImageGrab, Image
import cv2
import numpy as np

class ClaudeDesktop:
    def __init__(self):
        self.config_path = os.path.expandvars(r'%APPDATA%\Claude\claude_desktop_config.json')
        self.exe_path = r'C:\Users\psnbm\AppData\Local\AnthropicClaude\claude.exe'

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.allow_button_path = os.path.join(self.script_dir, 'allow_button.png')
        self.chat_button_path = os.path.join(self.script_dir, 'chat_button.png')
        
        # Add a safety delay for pyautogui
        pyautogui.PAUSE = 1
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
        print("checking for dialoge")
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
        
    def send_prompt(self, prompt: str):
        """Send a prompt to Claude"""
        pyautogui.write(prompt)
        pyautogui.press('enter')
        # Check for permissions popup after sending prompt
        self.handle_permissions()

# Example usage
claude = ClaudeDesktop()

# Launch Claude
claude.launch()

# Start a new chat
claude.new_chat()

# Send the weather prompt
claude.create_github_project("Create a python project that is a game of battleship", "battleships-test", "berlinbra")