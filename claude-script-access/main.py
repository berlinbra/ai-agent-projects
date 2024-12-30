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

    # Move to logo, click, and wait
    pyautogui.moveTo(logo_location)
    pyautogui.click()
    time.sleep(0.5)

    # Find and click New Chat
    if not self.find_and_click_image(self.new_chat_path):
        raise Exception("Could not find New Chat button")

    time.sleep(1)  # Wait for new chat to initialize
    return True