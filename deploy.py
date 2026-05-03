import subprocess
import os

def auto_deploy():
    print("🚀 Starting Martialzii Full-Stack Deployment...")
    
    # 1. Check if we are in the right directory
    if not os.path.exists(".git"):
        print("❌ Error: Not a git repository.")
        return

    # 2. Add all new files (including guardian.py and sentinel.py)
    subprocess.run(["git", "add", "."])
    
    # 3. Commit with a timestamped message
    from datetime import datetime
    commit_msg = f"Auto-Deployment: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    
    # 4. Push to the main branch
    result = subprocess.run(["git", "push", "origin", "main"])
    
    if result.returncode == 0:
        print("✅ Deployment Successful! Repository is up-to-date.")
    else:
        print("⚠️ Deployment encountered an error.")

if __name__ == "__main__":
    auto_deploy()