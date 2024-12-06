from typing import Dict, List, Optional
from ..core.github_operations import GitHubOperations

class ProjectTemplates:
    def __init__(self):
        self.github = GitHubOperations()
    
    def create_python_project(self,
                             repo_name: str,
                             project_name: str,
                             description: str = None) -> Dict:
        """Create a new Python project with standard structure"""
        try:
            # Create repository
            repo_result = self.github.create_repository(
                name=project_name,
                description=description
            )
            if repo_result["status"] == "error":
                return repo_result
            
            # Define project structure
            structure = {
                "src": {
                    f"{project_name}": {
                        "__init__.py": "",
                        "main.py": "def main():\n    pass\n\nif __name__ == '__main__':\n    main()"
                    }
                },
                "tests": {
                    "__init__.py": "",
                    "test_main.py": "def test_example():\n    assert True"
                },
                "requirements.txt": "pytest>=7.0.0\n",
                "setup.py": f"from setuptools import setup, find_packages\n\nsetup(\n    name=\"{project_name}\",\n    version=\"0.1.0\",\n    packages=find_packages(where=\"src\"),\n    package_dir={{\"\":\"src\"}},\n    install_requires=[\n        'pytest>=7.0.0',\n    ],\n)",
                ".gitignore": "__pycache__/\n*.py[cod]\n*$py.class\n.pytest_cache/\n.coverage\nhtml/\n.tox/\n.env\n.venv\nvenv/\nENV/\n",
                "README.md": f"# {project_name}\n\n{description if description else ''}\n\n## Installation\n\n```bash\npip install -e .\n```\n\n## Usage\n\n```python\nfrom {project_name} import main\n```\n\n## Development\n\n1. Clone the repository\n2. Create a virtual environment\n3. Install dependencies\n4. Run tests\n```bash\npytest\n```\n"
            }
            
            # Create project structure
            structure_result = self.github.create_project_structure(
                repo_name=repo_result["repo"],
                structure=structure
            )
            
            return {"status": "success", "repo": repo_result["repo"], "structure": structure_result}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def start_new_feature(self,
                         repo_name: str,
                         feature_name: str,
                         description: str = None) -> Dict:
        """Start a new feature branch with associated PR and issue"""
        try:
            # Create feature branch
            branch_name = f"feature/{feature_name}"
            branch_result = self.github.create_branch(
                repo_name=repo_name,
                branch_name=branch_name
            )
            if branch_result["status"] == "error":
                return branch_result
            
            # Create issue
            issue_result = self.github.create_issue(
                repo_name=repo_name,
                title=f"Feature: {feature_name}",
                body=description or f"Implement {feature_name}",
                labels=["feature"]
            )
            
            # Create draft PR
            pr_result = self.github.create_pull_request(
                repo_name=repo_name,
                title=f"Feature: {feature_name}",
                head=branch_name,
                base="main",
                body=f"Implements #{issue_result['issue_number']}\n\n{description if description else ''}",
                draft=True
            )
            
            return {
                "status": "success",
                "branch": branch_name,
                "issue": issue_result["issue_number"],
                "pr": pr_result["pr_number"]
            }
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
