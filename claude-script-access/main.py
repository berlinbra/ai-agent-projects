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
import psutil

class ClaudeDesktop:
    def __init__(self):
        self.config_path = os.path.expandvars(r'%APPDATA%\\Claude\\claude_desktop_config.json')
        self.exe_path = r'C:\\Users\\psnbm\\AppData\\Local\\AnthropicClaude\\claude.exe'

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.allow_button_path = os.path.join(self.script_dir, 'allow_button.png')
        self.chat_button_path = os.path.join(self.script_dir, 'chat_button.png')
        self.claude_logo_path = os.path.join(self.script_dir, 'claude_logo.png')
        self.new_chat_path = os.path.join(self.script_dir, 'new_chat.png')
        
        # Add a safety delay for pyautogui
        pyautogui.PAUSE = 0.5
        pyautogui.FAILSAFE = True

    def find_and_click_image(self, image_path: str, timeout: int = 5, confidence: float = 0.8) -> bool:
        """Find and click on an image with timeout and retry
        
        Args:
            image_path: Path to the image to find
            timeout: How long to search for in seconds
            confidence: Confidence level for image matching (0-1)
            
        Returns:
            bool: True if image was found and clicked, False otherwise
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                if location:
                    pyautogui.click(location)
                    return True
            except Exception as e:
                print(f"Error finding image {image_path}: {e}")
            time.sleep(0.5)
        return False

    def new_chat(self):
        """Start a new chat by clicking Claude logo then New Chat"""
        # First find and move to Claude logo
        logo_location = None
        try:
            logo_location = pyautogui.locateOnScreen(self.claude_logo_path, confidence=0.8)
            if not logo_location:
                raise Exception("Could not find Claude logo")
        except Exception as e:
            print(f"Error finding Claude logo: {e}")
            return False

        # Move to logo and wait
        pyautogui.moveTo(logo_location)
        time.sleep(0.5)

        # Find and click New Chat
        if not self.find_and_click_image(self.new_chat_path):
            raise Exception("Could not find New Chat button")

        time.sleep(1)  # Wait for new chat to initialize
        return True

    def check_for_permission_dialog(self, timeout=2):
        """Check if the permission dialog is visible"""
        start_time = time.time()
        print("checking for dialog")
        while time.time() - start_time < timeout:
            try:
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
        time.sleep(2)
        self.handle_permissions()

    def _paste_text(self, text: str, retry_count: int = 3):
        """Helper method to paste text using clipboard"""
        for attempt in range(retry_count):
            try:
                # Copy to clipboard
                pyperclip.copy(text)
                time.sleep(0.2)
                
                # Paste using Ctrl+V
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.2)
                return
            except Exception as e:
                if attempt == retry_count - 1:
                    raise Exception(f"Failed to paste text after {retry_count} attempts: {str(e)}")
                time.sleep(1)
        
    def send_prompt(self, prompt: str, chunk_size: Optional[int] = None, retry_count: int = 3):
        """Send a prompt to Claude using clipboard for reliability"""
        original_clipboard = pyperclip.paste()
        
        try:
            if chunk_size and len(prompt) > chunk_size:
                chunks = [prompt[i:i + chunk_size] for i in range(0, len(prompt), chunk_size)]
                for chunk in chunks:
                    self._paste_text(chunk, retry_count)
                    time.sleep(0.5)
            else:
                self._paste_text(prompt, retry_count)
            
            time.sleep(0.3)
            pyautogui.press('enter')
            
        finally:
            pyperclip.copy(original_clipboard)
            
        self.handle_permissions()

# Example usage
if __name__ == "__main__":
    claude = ClaudeDesktop()

    # Start a new chat
    claude.new_chat()

    # Create a GitHub project
    claude.create_github_project(
        "Create a python project that is a game of battleship",
        "battleships-test",
        "berlinbra"
    )