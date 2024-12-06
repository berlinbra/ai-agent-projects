import os
from typing import Dict, List, Optional
from anthropic import Anthropic
import requests
from dotenv import load_dotenv

load_dotenv()

class ClaudeWithTools:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.brave_api_key = os.getenv('BRAVE_API_KEY')
        
    def brave_web_search(self, query: str, count: int = 10) -> Dict:
        """Perform a web search using Brave Search API"""
        url = 'https://api.search.brave.com/res/v1/web/search'
        headers = {'X-Subscription-Token': self.brave_api_key}
        params = {'q': query, 'count': count}
        
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def ask_claude(self, user_message: str, system_message: Optional[str] = None) -> str:
        """Send a message to Claude and get its response"""
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
            
        messages.append({"role": "user", "content": user_message})
        
        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=messages
        )
        
        return response.content[0].text
    
    def research_topic(self, topic: str) -> str:
        """Research a topic using both web search and Claude's analysis"""
        # First, search for information
        search_results = self.brave_web_search(topic)
        
        # Format the search results for Claude
        formatted_results = "Search results:\n"
        for result in search_results.get('web', {}).get('results', [])[:3]:
            formatted_results += f"\nTitle: {result['title']}\n"
            formatted_results += f"Description: {result['description']}\n"
        
        # Ask Claude to analyze the results
        prompt = f"I've searched for information about '{topic}'. Here are the results:\n\n{formatted_results}\n\nPlease analyze these results and provide a comprehensive summary."
        
        return self.ask_claude(prompt)

def main():
    claude = ClaudeWithTools()
    
    # Example usage
    topic = "latest developments in quantum computing"
    print(f"Researching: {topic}\n")
    
    analysis = claude.research_topic(topic)
    print("Analysis:")
    print(analysis)

if __name__ == "__main__":
    main()