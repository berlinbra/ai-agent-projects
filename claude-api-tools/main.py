from tools import BraveSearch, GitHubIntegration
from claude_assistant import ClaudeAssistant

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

def example_github():
    # Example using GitHub integration
    github = GitHubIntegration()
    
    # Ask Claude to generate some code
    claude = ClaudeAssistant()
    code = claude.ask("Write a Python function that implements the bubble sort algorithm")
    
    # Save the code to GitHub
    result = github.create_file(
        repo_name="your-username/your-repo",
        file_path="algorithms/bubble_sort.py",
        content=code,
        commit_message="Add bubble sort implementation"
    )
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
