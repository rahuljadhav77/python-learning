import argparse
import datetime
import sys
from automator import PythonChallengeAutomator

def main():
    parser = argparse.ArgumentParser(description="100 Days of Python Challenge Automator")
    parser.add_argument("--repo", default=".", help="Path to the repository")
    parser.add_argument("--day", type=int, help="Generate a specific day")
    parser.add_argument("--next", action="store_true", help="Automatically generate the next day based on existing folders")
    parser.add_argument("--backfill", type=int, help="Number of days to backfill from today")
    parser.add_argument("--start-day", type=int, default=1, help="Day number to start backfill from")
    parser.add_argument("--start-date", help="Start date for backfill (YYYY-MM-DD). Defaults to X days ago if --backfill is used.")
    parser.add_argument("--push", action="store_true", help="Push to origin after generating")

    args = parser.parse_args()

    automator = PythonChallengeAutomator(repo_path=args.repo)
    automator.setup_repo()

    if args.day:
        automator.generate_day(args.day, push=args.push)
    elif args.next:
        # Find the next day by looking at existing folders
        dirs = [d.name for d in automator.repo_path.glob("day_*") if d.is_dir()]
        day_nums = [int(d.split("_")[1]) for d in dirs if d.split("_")[1].isdigit()]
        next_day = max(day_nums, default=0) + 1
        print(f"Detected next day: {next_day}")
        automator.generate_day(next_day, push=args.push)
    elif args.backfill:
        if args.start_date:
            try:
                start_dt = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid date format. Use YYYY-MM-DD.")
                sys.exit(1)
        else:
            # Calculate start date based on number of days to backfill
            start_dt = datetime.datetime.now() - datetime.timedelta(days=args.backfill - 1)
        
        automator.backfill(args.start_day, args.start_day + args.backfill - 1, start_dt)
        if args.push:
            print("Pushing all commits...")
            automator._run_git(["push", "origin", automator.branch])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
