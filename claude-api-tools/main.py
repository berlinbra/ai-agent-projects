from tools import BraveSearch, GitHubIntegration
from claude_assistant import ClaudeAssistant
import re
from datetime import datetime

def example_search():
    # Example using Brave Search
    search = BraveSearch()
    results = search.search("latest developments in quantum computing")
    formatted_results = search.format_results(results)
    print("Search Results:")
    print(formatted_results)
    
    # Use Claude to analyze the results
    claude = ClaudeAssistant()
    analysis = claude.ask(f"Please analyze these search results and provide a summary:\n{formatted_results}")
    print("\nClaude's Analysis:")
    print(analysis)

def generate_folder_name(code_description: str) -> str:
    """Generate a folder name based on the code description"""
    # Remove special characters and convert to lowercase
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', code_description.lower())
    # Replace spaces with underscores and limit length
    folder_name = re.sub(r'\s+', '_', cleaned_name)[:50]
    # Add timestamp to ensure uniqueness
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{folder_name}_{timestamp}"

def example_github():
    # Example using GitHub integration
    github = GitHubIntegration()
    claude = ClaudeAssistant()
    
    # First, ask Claude what kind of code to generate
    project_prompt = "Write a Python function that implements the bubble sort algorithm and includes comprehensive comments explaining how it works."
    
    # Generate the code
    code = claude.ask(project_prompt)
    
    # Ask Claude to describe what the code does (for folder naming)
    description_prompt = "In 5 words or less, what does this code implement?"
    description = claude.ask(description_prompt)
    
    # Generate folder name based on the description
    folder_name = generate_folder_name(description)
    
    # Save the code to GitHub
    result = github.create_file(
        repo_name="berlinbra/ai-agent-projects",
        file_path=f"{folder_name}/implementation.py",
        content=code,
        commit_message=f"Add {description} implementation"
    )
    print("\nProject Description:", description)
    print("Created in folder:", folder_name)
    print("GitHub Result:", result)

def main():
    print("1. Search Example")
    print("2. GitHub Example")
    choice = input("Choose an example to run (1-2): ")
    
    if choice == '1':
        example_search()
    elif choice == '2':
        example_github()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
