from anthropic import Anthropic
from typing import Optional
from dotenv import load_dotenv
import os

class ClaudeAssistant:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError('ANTHROPIC_API_KEY not found in environment variables')
            
        self.client = Anthropic(api_key=api_key)
    
    def ask(self, 
            user_message: str, 
            system_message: Optional[str] = None,
            max_tokens: int = 1024) -> str:
        """Send a message to Claude and get its response
        
        Args:
            user_message (str): The message to send to Claude
            system_message (Optional[str], optional): System message for context. Defaults to None.
            max_tokens (int, optional): Maximum tokens in response. Defaults to 1024.
            
        Returns:
            str: Claude's response
        """
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
            
        messages.append({"role": "user", "content": user_message})
        
        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=max_tokens,
            messages=messages
        )
        
        return response.content[0].text
