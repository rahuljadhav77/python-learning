import os
import subprocess
import datetime
import random
from pathlib import Path
from curriculum import get_day_data

class PythonChallengeAutomator:
    def __init__(self, repo_path, branch="main"):
        self.repo_path = Path(repo_path).absolute()
        self.branch = branch
        self.os_env = os.environ.copy()

    def _run_git(self, args, commit_date=None):
        env = self.os_env.copy()
        if commit_date:
            # Format: 'YYYY-MM-DD HH:MM:SS'
            date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
            env['GIT_AUTHOR_DATE'] = date_str
            env['GIT_COMMITTER_DATE'] = date_str
        
        result = subprocess.run(
            ["git"] + args,
            cwd=self.repo_path,
            env=env,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Git Error: {result.stderr}")
        return result

    def setup_repo(self):
        if not (self.repo_path / ".git").exists():
            print(f"Initializing new git repository at {self.repo_path}")
            self.repo_path.mkdir(parents=True, exist_ok=True)
            self._run_git(["init"])
            # Create an initial commit if empty
            with open(self.repo_path / ".gitignore", "w") as f:
                f.write("__pycache__/\\n*.pyc\\n.DS_Store\\n")
            self._run_git(["add", ".gitignore"])
            self._run_git(["commit", "-m", "Initial commit: Set up 100 Days of Python Challenge"])

    def generate_day(self, day_number, custom_date=None, push=False):
        day_data = get_day_data(day_number)
        folder_name = f"day_{day_number:03d}"
        dir_path = self.repo_path / folder_name
        dir_path.mkdir(exist_ok=True)

        # Create main.py
        with open(dir_path / "main.py", "w") as f:
            f.write(day_data["code"])

        # Create README.md
        readme_content = f"""# Day {day_number}: {day_data['title']}

## Description
{day_data['description']}

## Tasks Accomplished
{chr(10).join([f"- {t}" for t in day_data['tasks']])}

## How to Run
Run the code using:
```bash
python main.py
```
"""
        with open(dir_path / "README.md", "w") as f:
            f.write(readme_content)

        # Git operations - only add the specific folder for this day
        self._run_git(["add", folder_name])
        
        # Varied commit messages
        verbs = ["Built", "Implemented", "Created", "Explored", "Finished", "Developed"]
        msg = f"Day {day_number}: {random.choice(verbs)} {day_data['title']}"
        
        # Simulate local time randomization (e.g., between 6 PM and 10 PM)
        if custom_date:
            # Add some randomness to seconds too
            commit_time = custom_date.replace(
                hour=random.randint(18, 22), 
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
        else:
            commit_time = datetime.datetime.now()

        commit_result = self._run_git(["commit", "-m", msg], commit_date=commit_time)
        
        if "nothing to commit" in commit_result.stdout or "nothing to commit" in commit_result.stderr:
             print(f"Skipping commit for {folder_name} - no changes detected.")
        else:
             print(f"Successfully committed {folder_name} for date {commit_time.strftime('%Y-%m-%d %H:%M:%S')}")

        if push:
            self._run_git(["push", "origin", self.branch])

    def backfill(self, start_day, end_day, start_date):
        """
        Backfill multiple days starting from start_date.
        start_date should be a datetime object.
        """
        current_date = start_date
        for day in range(start_day, end_day + 1):
            self.generate_day(day, custom_date=current_date)
            current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    # Example usage (can be moved to a CLI script)
    automator = PythonChallengeAutomator(repo_path=".")
    automator.setup_repo()
    # To test one day:
    # automator.generate_day(1)
