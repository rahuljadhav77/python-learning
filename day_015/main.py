import datetime

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def show_logs():
    try:
        with open("activity_log.txt", "r") as f:
            print("\n--- Recent Activity ---")
            print(f.read())
    except FileNotFoundError:
        print("No logs found yet.")

if __name__ == '__main__':
    log_event("Started Day 15 task")
    log_event("Learned about file handling with 'with' statements")
    show_logs()
