import random
from datetime import datetime, timedelta

def generate_commit_schedule(start_date, duration_days):
    """Generate a realistic commit schedule"""
    schedule = []
    current_date = start_date
    
    for _ in range(duration_days):
        # More commits on weekdays
        if current_date.weekday() < 5:
            num_commits = random.randint(1, 5)
        else:
            num_commits = random.randint(0, 2)
            
        for _ in range(num_commits):
            hour = random.randint(9, 18)  # Business hours
            commit_time = current_date.replace(hour=hour)
            schedule.append(commit_time)
            
        current_date += timedelta(days=1)
    
    return sorted(schedule)

def generate_commit_message(context):
    """Generate a realistic commit message"""
    templates = [
        "Add {feature} functionality",
        "Update {component} implementation",
        "Fix {issue} in {component}",
        "Refactor {component} for better {aspect}",
        "Improve {aspect} in {component}",
        "Remove deprecated {feature}",
        "Optimize {component} performance"
    ]
    
    return random.choice(templates).format(**context)