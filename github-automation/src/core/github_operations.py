from github import Github
from typing import Dict, List, Optional, Union
from dotenv import load_dotenv
import os

class GitHubOperations:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('GITHUB_TOKEN')
        if not self.token:
            raise ValueError('GITHUB_TOKEN not found in environment variables')
        
        self.github = Github(self.token)
    
    def create_repository(self, 
                         name: str, 
                         private: bool = False, 
                         description: str = None,
                         homepage: str = None,
                         has_wiki: bool = True,
                         has_issues: bool = True) -> Dict:
        """Create a new repository"""
        try:
            repo = self.github.get_user().create_repo(
                name=name,
                private=private,
                description=description,
                homepage=homepage,
                has_wiki=has_wiki,
                has_issues=has_issues
            )
            return {"status": "success", "repo": repo.full_name}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def create_branch(self, 
                      repo_name: str, 
                      branch_name: str, 
                      from_branch: str = "main") -> Dict:
        """Create a new branch in repository"""
        try:
            repo = self.github.get_repo(repo_name)
            source = repo.get_branch(from_branch)
            repo.create_git_ref(f"refs/heads/{branch_name}", source.commit.sha)
            return {"status": "success", "branch": branch_name}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def create_project_structure(self, 
                                repo_name: str, 
                                structure: Dict,
                                branch: str = "main",
                                base_path: str = "") -> Dict:
        """Create a project structure from dictionary"""
        results = []
        try:
            for name, content in structure.items():
                path = f"{base_path}/{name}" if base_path else name
                
                if isinstance(content, dict):
                    # Recursive call for nested directories
                    sub_results = self.create_project_structure(
                        repo_name, content, branch, path
                    )
                    results.extend(sub_results.get("results", []))
                else:
                    # Create file
                    result = self.create_file(
                        repo_name=repo_name,
                        file_path=path,
                        content=content,
                        commit_message=f"Add {path}",
                        branch=branch
                    )
                    results.append(result)
            
            return {"status": "success", "results": results}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def create_file(self,
                    repo_name: str,
                    file_path: str,
                    content: str,
                    commit_message: str,
                    branch: str = "main") -> Dict:
        """Create or update a file in repository"""
        try:
            repo = self.github.get_repo(repo_name)
            
            try:
                # Try to get existing file
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
    
    def create_pull_request(self,
                           repo_name: str,
                           title: str,
                           head: str,
                           base: str = "main",
                           body: str = None,
                           draft: bool = False) -> Dict:
        """Create a pull request"""
        try:
            repo = self.github.get_repo(repo_name)
            pr = repo.create_pull(
                title=title,
                body=body,
                head=head,
                base=base,
                draft=draft
            )
            return {"status": "success", "pr_number": pr.number}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def create_issue(self,
                     repo_name: str,
                     title: str,
                     body: str = None,
                     labels: List[str] = None,
                     assignees: List[str] = None) -> Dict:
        """Create an issue"""
        try:
            repo = self.github.get_repo(repo_name)
            issue = repo.create_issue(
                title=title,
                body=body,
                labels=labels,
                assignees=assignees
            )
            return {"status": "success", "issue_number": issue.number}
        except Exception as e:
            return {"status": "error", "error": str(e)}
