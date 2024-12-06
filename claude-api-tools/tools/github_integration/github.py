import osrom github import Github
from typing import Optional
from dotenv import load_dotenv

class GitHubIntegration:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('GITHUB_TOKEN')
        if not self.token:
            raise ValueError('GITHUB_TOKEN not found in environment variables')
        
        self.github = Github(self.token)
    
    def create_file(self, 
                    repo_name: str, 
                    file_path: str, 
                    content: str, 
                    commit_message: str,
                    branch: str = "main") -> Dict:
        """Create or update a file in a GitHub repository
        
        Args:
            repo_name (str): Name of the repository (format: 'username/repo')
            file_path (str): Path where to create/update the file
            content (str): Content to write to the file
            commit_message (str): Commit message
            branch (str, optional): Branch name. Defaults to "main".
            
        Returns:
            Dict: Response from GitHub API
        """
        try:
            repo = self.github.get_repo(repo_name)
            
            # Check if file exists
            try:
                contents = repo.get_contents(file_path, ref=branch)
                repo.update_file(
                    file_path,
                    commit_message,
                    content,
                    contents.sha,
                    branch=branch
                )
                return {"status": "updated", "path": file_path}
            
            except Exception:
                # File doesn't exist, create it
                repo.create_file(
                    file_path,
                    commit_message,
                    content,
                    branch=branch
                )
                return {"status": "created", "path": file_path}
                
        except Exception as e:
            return {"status": "error", "error": str(e)}
