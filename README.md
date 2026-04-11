# 100 Days of Python Challenge Automator

A tool to automatically generate a realistic learning journey by creating daily Python tasks and committing them to a Git repository with simulated timestamps.

## Features
- **Curriculum-based Generation**: 100 unique days of tasks, ranging from basics to capstone projects.
- **Git Automation**: Automatically stages and commits each day's work.
- **Realistic Backfilling**: Can generate multiple days at once with backdated commits.
- **Varied Metadata**: Randomizes commit times (evenings) and commit messages for a natural look.
- **CLI Interface**: Simple commands to manage your challenge progress.

## Setup Instructions

1. **Clone or Download** this directory.
2. **Configure Git Identity** (if not already set):
   ```bash
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   ```
3. **Run the Automator**:
   - **Backfill 30 days starting from March 1st**:
     ```bash
     python cli.py --backfill 30 --start-date 2026-03-01
     ```
   - **Generate the next day (Day 31)**:
     ```bash
     python cli.py --day 31
     ```

## GitHub Actions Automation

The system is designed to work seamlessly with GitHub Actions. A workflow file has been provided at `.github/workflows/daily_challenge.yml`.

### How it works:
1.  **Cron Job**: Every day at 6 PM UTC, the runner starts.
2.  **Auto-Detection**: The runner executes `python cli.py --next`, which scans your repository, finds the last day completed (e.g., Day 5), and generates the next one (Day 6).
3.  **Auto-Push**: The changes are committed and pushed back to your repository automatically.

### Manual Trigger:
You can also trigger a new day manually from the **Actions** tab on GitHub by selecting the "Daily Python Challenge" workflow and clicking "Run workflow".

## Structure of Generated Days
Each day consists of:
- `day_XXX/main.py`: Functional Python code.
- `day_XXX/README.md`: Task description, accomplishments, and run instructions.
