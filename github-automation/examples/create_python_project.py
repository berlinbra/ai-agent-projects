from src.workflows.project_templates import ProjectTemplates

def main():
    templates = ProjectTemplates()
    
    # Create a new Python project
    result = templates.create_python_project(
        repo_name="your-username/new-project",
        project_name="example_project",
        description="A sample Python project with standard structure"
    )
    
    print("Creation result:", result)

if __name__ == "__main__":
    main()