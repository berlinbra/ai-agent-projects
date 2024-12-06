import pyautogui
import time
from dotenv import load_dotenv
import os

load_dotenv()

class ClaudeDesktop:
    def __init__(self):
        self.window_title = os.getenv('CLAUDE_WINDOW_TITLE', 'Claude')
        
    def focus_window(self):
        """Focus the Claude desktop window"""
        try:
            # This is a basic approach - might need adjustment for your OS
            window = pyautogui.getWindowsWithTitle(self.window_title)
            if window:
                window[0].activate()
                time.sleep(0.5)  # Wait for window to focus
                return True
            return False
        except:
            return False
    
    def send_message(self, message: str):
        """Send a message to Claude via the desktop app
        
        Args:
            message (str): Message to send
        """
        if not self.focus_window():
            raise Exception("Could not find Claude window")
            
        # Find and click the input box
        # Note: You'll need to adjust coordinates based on your screen
        pyautogui.click(x=500, y=800)  # Example coordinates
        time.sleep(0.2)
        
        # Type the message
        pyautogui.write(message)
        time.sleep(0.2)
        
        # Send the message (Enter key)
        pyautogui.press('enter')

def main():
    claude = ClaudeDesktop()
    
    # Example usage
    try:
        claude.send_message("What's the current date?")
        print("Message sent successfully")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()