import os
import requests
import subprocess

# Configure your details
GITHUB_USERNAME = "Martialzii"
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN" # You'll generate this in Settings > Developer Settings

def forge_project(project_name):
    # 1. Create local directory
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    
    # 2. Create GitHub Repo via API
    url = "https://api.github.com/user/repos"
    payload = {"name": project_name, "private": False}
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print(f"🚀 Repository {project_name} created on GitHub!")
        
        # 3. Initialize Git and Push
        with open("README.md", "w") as f:
            f.write(f"# {project_name}\nAutomated by Martialzii Project-Forge")
            
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Initial Forge"])
        subprocess.run(["git", "branch", "-M", "main"])
        subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{GITHUB_USERNAME}/{project_name}.git"])
        subprocess.run(["git", "push", "-u", "origin", "main"])
    else:
        print(f"❌ Failed: {response.json().get('message')}")

# Usage
project = input("Enter new project name: ")
forge_project(project)