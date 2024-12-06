import os
import random
from datetime import datetime, timedelta
from anthropic import Anthropic
from github import Github
from dotenv import load_dotenv

class ProjectSimulator:
    def __init__(self, github_token, anthropic_key):
        self.github = Github(github_token)
        self.anthropic = Anthropic(api_key=anthropic_key)
        self.development_phases = [
            "initial_setup",
            "core_functionality",
            "feature_development",
            "testing",
            "documentation",
            "optimization"
        ]
        
    def create_repository(self, name, description):
        """Create a new repository with basic structure"""
        try:
            repo = self.github.get_user().create_repo(
                name=name,
                description=description,
                private=False,
                auto_init=True
            )
            self._setup_initial_structure(repo)
            return repo
        except Exception as e:
            print(f"Error creating repository: {e}")
            return None

    def _setup_initial_structure(self, repo):
        """Set up the initial project structure"""
        files = {
            "README.md": self._generate_readme(repo.name, repo.description),
            "requirements.txt": "anthropic\ngithub\npython-dotenv\npytest",
            ".gitignore": "*.pyc\n__pycache__\n.env\n.venv\n*.log\n.DS_Store",
            "src/__init__.py": "",
            "tests/__init__.py": "",
            "docs/README.md": "# Documentation\n\nProject documentation will be added here.",
        }
        
        for path, content in files.items():
            self._create_file(repo, path, content, "Initial project structure")

    def simulate_development(self, repo, duration_days=30):
        """Simulate development activity over a period of time"""
        start_date = datetime.now() - timedelta(days=duration_days)
        
        for day in range(duration_days):
            current_date = start_date + timedelta(days=day)
            if current_date.weekday() < 5:  # Weekday
                self._simulate_day_activity(repo, current_date, more_active=True)
            else:  # Weekend
                self._simulate_day_activity(repo, current_date, more_active=False)

    def _simulate_day_activity(self, repo, date, more_active=True):
        """Simulate a day's worth of development activity"""
        num_commits = random.randint(3, 8) if more_active else random.randint(0, 2)
        
        for _ in range(num_commits):
            hour = random.randint(9, 18)
            commit_date = date.replace(hour=hour)
            
            # Simulate different types of commits
            activity_type = random.choice([
                "feature",
                "bugfix",
                "refactor",
                "docs",
                "tests"
            ])
            
            self._create_activity(repo, activity_type, commit_date)

    def _create_activity(self, repo, activity_type, date):
        """Create a specific type of development activity"""
        if activity_type == "feature":
            self._simulate_feature_development(repo, date)
        elif activity_type == "bugfix":
            self._simulate_bugfix(repo, date)
        elif activity_type == "refactor":
            self._simulate_refactoring(repo, date)
        elif activity_type == "docs":
            self._simulate_documentation_update(repo, date)
        elif activity_type == "tests":
            self._simulate_test_addition(repo, date)

    def _simulate_feature_development(self, repo, date):
        """Simulate adding a new feature"""
        feature_prompt = f"""Generate a Python class that implements one of these features:
        - User authentication
        - Data processing
        - API integration
        - Configuration management
        - Logging system
        Include docstrings and type hints.
        """
        
        response = self.anthropic.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=2000,
            temperature=0.7,
            messages=[{"role": "user", "content": feature_prompt}]
        )
        
        feature_code = response.content[0].text
        feature_name = self._extract_feature_name(feature_code)
        
        self._create_file(
            repo,
            f"src/{feature_name.lower()}.py",
            feature_code,
            f"Add {feature_name} feature",
            date
        )

    def _simulate_bugfix(self, repo, date):
        """Simulate fixing a bug"""
        files = repo.get_contents("src")
        if files:
            file = random.choice(files)
            content = file.decoded_content.decode()
            
            bugfix_prompt = f"""Given this code:
            {content}
            
            Suggest a realistic bug fix with a comment explaining the issue.
            """
            
            response = self.anthropic.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0.5,
                messages=[{"role": "user", "content": bugfix_prompt}]
            )
            
            updated_code = response.content[0].text
            self._update_file(
                repo,
                file.path,
                updated_code,
                "Fix bug: " + self._generate_bug_message(),
                date
            )

    def _generate_bug_message(self):
        """Generate a realistic bug fix commit message"""
        bug_types = [
            "Fix null pointer exception in",
            "Fix race condition in",
            "Fix memory leak in",
            "Fix incorrect error handling in",
            "Fix edge case in"
        ]
        components = [
            "user authentication",
            "data processing",
            "API client",
            "configuration manager",
            "logging system"
        ]
        return f"{random.choice(bug_types)} {random.choice(components)}"

    def _simulate_refactoring(self, repo, date):
        """Simulate code refactoring"""
        refactor_prompts = [
            "Extract duplicate code into helper functions",
            "Improve error handling and add logging",
            "Optimize performance of database queries",
            "Convert functions to use async/await",
            "Implement dependency injection"
        ]
        
        prompt = random.choice(refactor_prompts)
        
        refactor_message = f"Refactor: {prompt.lower()}"
        self._create_file(
            repo,
            f"src/refactored_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py",
            self._generate_refactored_code(prompt),
            refactor_message,
            date
        )