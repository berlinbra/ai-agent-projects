# Project Simulator

A tool for generating GitHub projects with realistic development patterns using Claude AI.

## Features

- Create new GitHub repositories with proper structure
- Simulate realistic development activity over time
- Generate different types of commits:
  - Feature additions
  - Bug fixes
  - Code refactoring
  - Documentation updates
  - Test additions
- Use Claude to generate realistic code and content
- Configure development patterns and timeframes

## Usage

```python
from project_simulator import ProjectSimulator
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize simulator
simulator = ProjectSimulator(
    github_token=os.getenv("GITHUB_TOKEN"),
    anthropic_key=os.getenv("ANTHROPIC_API_KEY")
)

# Create a new repository
repo = simulator.create_repository(
    name="example-project",
    description="An example project with simulated development history"
)

# Simulate 30 days of development
simulator.simulate_development(repo, duration_days=30)
```

## Environment Variables

Required environment variables:

```
GITHUB_TOKEN=your_github_token
ANTHROPIC_API_KEY=your_anthropic_key
```

## Development Activity Types

1. Feature Development
   - Generates new Python classes for various features
   - Includes proper documentation and type hints
   - Realistic implementation patterns

2. Bug Fixes
   - Identifies potential issues in existing code
   - Generates realistic fixes with explanatory comments
   - Creates appropriate commit messages

3. Code Refactoring
   - Improves code structure and organization
   - Implements best practices
   - Adds documentation and error handling

4. Documentation
   - Generates various types of documentation
   - API references
   - Setup guides
   - Contributing guidelines

5. Testing
   - Creates pytest test suites
   - Includes unit and integration tests
   - Proper test organization and structure