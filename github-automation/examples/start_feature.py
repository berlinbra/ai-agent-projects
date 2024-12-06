from src.workflows.project_templates import ProjectTemplates

def main():
    templates = ProjectTemplates()
    
    # Start a new feature
    result = templates.start_new_feature(
        repo_name="your-username/your-repo",
        feature_name="user-authentication",
        description="Implement user authentication using JWT"
    )
    
    print("Feature creation result:", result)

if __name__ == "__main__":
    main()