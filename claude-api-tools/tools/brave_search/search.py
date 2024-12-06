import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

class BraveSearch:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('BRAVE_API_KEY')
        if not self.api_key:
            raise ValueError('BRAVE_API_KEY not found in environment variables')
            
    def search(self, query: str, count: int = 10) -> Dict:
        """Perform a web search using Brave Search API
        
        Args:
            query (str): Search query
            count (int, optional): Number of results. Defaults to 10.
            
        Returns:
            Dict: Search results containing web pages, descriptions, etc.
        """
        url = 'https://api.search.brave.com/res/v1/web/search'
        headers = {'X-Subscription-Token': self.api_key}
        params = {'q': query, 'count': count}
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        
        return response.json()
    
    def format_results(self, results: Dict, max_results: int = 3) -> str:
        """Format search results into a readable string
        
        Args:
            results (Dict): Search results from brave_search()
            max_results (int, optional): Maximum number of results to include. Defaults to 3.
            
        Returns:
            str: Formatted search results
        """
        formatted = ""
        
        for result in results.get('web', {}).get('results', [])[:max_results]:
            formatted += f"\nTitle: {result['title']}"
            formatted += f"\nURL: {result['url']}"
            formatted += f"\nDescription: {result['description']}"
            formatted += "\n" + "-"*50 + "\n"
            
        return formatted
