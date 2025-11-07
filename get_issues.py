import os
import gitlab
from gitlab.exceptions import GitlabGetError

# -----------------------------------------
# Configuration
# -----------------------------------------

# Base GitLab URL
GITLAB_URL_BASE = "https://gitlab.com"

# Exact project path from your GitLab URL:
# https://gitlab.com/msba285_fall24/msba285_fall25/nguyen_my_san
PROJECT_PATH = "msba285_fall24/msba285_fall25/nguyen_my_san"

# -----------------------------------------
# Load Personal Access Token from env var
# -----------------------------------------

PERSONAL_ACCESS_TOKEN = os.getenv("GITLAB_TOKEN")

if not PERSONAL_ACCESS_TOKEN:
    raise ValueError(
        "❌ No token found.\n"
        "Before running this script, in this terminal run:\n"
        "  export GITLAB_TOKEN='your_token_here'\n"
    )

# -----------------------------------------
# Connect to GitLab
# -----------------------------------------

gl = gitlab.Gitlab(GITLAB_URL_BASE, private_token=PERSONAL_ACCESS_TOKEN)

# Optional: verify auth (will raise if token invalid)
gl.auth()

print(f"Using PROJECT_PATH = {PROJECT_PATH}")

# -----------------------------------------
# Get project
# -----------------------------------------

try:
    project = gl.projects.get(PROJECT_PATH)
except GitlabGetError as e:
    raise SystemExit(
        f"❌ Could not access project '{PROJECT_PATH}'.\n"
        f"GitLab returned: {e}\n"
        "- Make sure this matches your project URL exactly.\n"
        "- Make sure the token belongs to the same GitLab account and has 'read_api'.\n"
    )

# -----------------------------------------
# List and print issues
# -----------------------------------------

issues = project.issues.list(all=True)

if not issues:
    print("No issues found in this project.")
else:
    print(f"Issues for project: {PROJECT_PATH}")
    for issue in issues:
        print(f"- #{issue.iid}: {issue.title}")
