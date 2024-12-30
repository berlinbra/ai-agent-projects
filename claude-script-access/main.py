def new_chat(self):
    """Start a new chat by clicking Claude logo then New Chat"""
    # First find Claude logo
    try:
        logo_location = pyautogui.locateOnScreen(self.claude_logo_path, confidence=0.8)
        if not logo_location:
            raise Exception("Could not find Claude logo")
            
        # Get the center point of the logo
        logo_center = pyautogui.center(logo_location)
        
        # Move mouse to logo
        pyautogui.moveTo(logo_center.x, logo_center.y)
        pyautogui.click()
        time.sleep(0.5)  # Wait for menu to appear
        
        # Now find and click New Chat button
        new_chat_location = pyautogui.locateOnScreen(self.new_chat_path, confidence=0.8)
        if not new_chat_location:
            raise Exception("Could not find New Chat button")
            
        # Get center of new chat button
        new_chat_center = pyautogui.center(new_chat_location)
        
        # Move to and click new chat
        pyautogui.moveTo(new_chat_center.x, new_chat_center.y)
        pyautogui.click()
        
        time.sleep(1)  # Wait for new chat to initialize
        return True
        
    except Exception as e:
        print(f"Error in new_chat: {e}")
        return False