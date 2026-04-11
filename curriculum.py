import random

CURRICULUM = {
    1: {
        "title": "Hello Python World",
        "description": "Start the journey with basic output and user interaction.",
        "tasks": ["Print greeting", "Ask for name", "Simple string concatenation"],
        "code": """# Day 1: Hello World
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the 100 Days of Python challenge.")
print("Today I learned about variables and basic input/output.")
"""
    },
    5: {
        "title": "Number Guessing Game",
        "description": "Building a simple game using loops and random numbers.",
        "tasks": ["Generate random number", "Loop until guessed", "Provide feedback (higher/lower)"],
        "code": """import random

def guess_game():
    target = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < target:
            print("Higher...")
        elif guess > target:
            print("Lower...")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            break

if __name__ == '__main__':
    guess_game()
"""
    },
    15: {
        "title": "Simple File Logger",
        "description": "Learning to read from and write to text files.",
        "tasks": ["Append log entries to a file", "Read and display log history"],
        "code": """import datetime

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\\n")

def show_logs():
    try:
        with open("activity_log.txt", "r") as f:
            print("\\n--- Recent Activity ---")
            print(f.read())
    except FileNotFoundError:
        print("No logs found yet.")

if __name__ == '__main__':
    log_event("Started Day 15 task")
    log_event("Learned about file handling with 'with' statements")
    show_logs()
"""
    },
    30: {
        "title": "Static Web Scraper",
        "description": "Extracting information from a local HTML simulation.",
        "tasks": ["Parse HTML structure", "Extract specific tags", "Display formatted data"],
        "code": """# Simulate web scraping logic (using concepts from BeautifulSoup)
from html.parser import HTMLParser

class SimpleParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            print(f"Found link: {dict(attrs).get('href')}")

html_content = \"\"\"
<html>
    <body>
        <h1>My Favorite Links</h1>
        <a href="https://python.org">Python Official</a>
        <a href="https://github.com">GitHub</a>
    </body>
</html>
\"\"\"

print("Scraping links...")
parser = SimpleParser()
parser.feed(html_content)
"""
    },
    60: {
        "title": "Weather API Client Mock",
        "description": "Simulate interaction with a REST API for weather data.",
        "tasks": ["Construct request URL", "Parse JSON-like response", "Format output"],
        "code": """import json

def get_weather(city):
    # Simulating an API response
    api_response = {
        "London": {"temp": 15, "condition": "Cloudy"},
        "New York": {"temp": 22, "condition": "Sunny"},
        "Tokyo": {"temp": 18, "condition": "Rainy"}
    }
    
    data = api_response.get(city, {"temp": "Unknown", "condition": "N/A"})
    print(f"Weather in {city}: {data['temp']}°C, {data['condition']}")

if __name__ == '__main__':
    cities = ["London", "New York"]
    for city in cities:
        get_weather(city)
"""
    },
    100: {
        "title": "Capstone: Personal CLI Assistant",
        "description": "Final project combining multiple concepts learned.",
        "tasks": ["CLI interface", "Data persistence", "Modular design"],
        "code": """import sys
import os

class Assistant:
    def __init__(self):
        self.commands = {
            "greet": self.greet,
            "add": self.add_task,
            "exit": sys.exit
        }

    def greet(self):
        print("Hello! I am your Day 100 Python Assistant.")

    def add_task(self):
        task = input("What task should I add? ")
        print(f"Task '{task}' added successfully.")

    def run(self):
        while True:
            cmd = input("Assist> ").lower()
            if cmd in self.commands:
                self.commands[cmd]()
            else:
                print("Unknown command. Try: greet, add, exit.")

if __name__ == '__main__':
    bot = Assistant()
    bot.run()
"""
    }
}

# Helper to fill in the gaps for a 100-day simulation with realistic code
def get_day_data(day):
    if day in CURRICULUM:
        return CURRICULUM[day]
    
    # Categories with realistic code templates
    categories = [
        {
            "name": "Logic & Math",
            "topics": [
                ("Prime Checker", """def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

num = 29
print(f'{num} is prime: {is_prime(num)}')"""),
                ("Fibonacci Series", """def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(10)))"""),
                ("Unit Converter", """def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp = 25
print(f'{temp}C is {celsius_to_fahrenheit(temp)}F')""")
            ]
        },
        {
            "name": "Strings",
            "topics": [
                ("Word Counter", """text = 'Python is amazing and fun'
words = text.split()
print(f'Word count: {len(words)}')"""),
                ("Palindrome Test", """def is_palindrome(s):
    clean = ''.join(e for e in s if e.isalnum()).lower()
    return clean == clean[::-1]

word = 'Racecar'
print(f'{word} is palindrome: {is_palindrome(word)}')"""),
                ("Text Formatter", """def bold(text): return f'**{text}**'
def italic(text): return f'*{text}*'
print(bold(italic('Hello World')))""")
            ]
        },
        {
            "name": "Automation",
            "topics": [
                ("File Organizer", """import os
import shutil
def organize_files(path):
    print(f'Organizing files in {path}...')
    # Mock organization logic
    pass
organize_files('./downloads')"""),
                ("Batch Renamer", """import os
def rename_files(prefix):
    print(f'Renaming files with prefix: {prefix}')
    pass
rename_files('v1_')"""),
                ("Backup Script", """import datetime
def create_backup(source, dest):
    print(f'Backing up {source} to {dest} on {datetime.datetime.now()}')
    pass
create_backup('./data', './backups')""")
            ]
        },
        {
            "name": "Data Structures",
            "topics": [
                ("List Comprehensions", """numbers = range(1, 11)
squares = [x**2 for x in numbers if x % 2 == 0]
print(f'Even squares: {squares}')"""),
                ("Dictionary Mapping", """prices = {'apple': 0.5, 'banana': 0.3}
stock = {'apple': 10, 'banana': 20}
total_value = sum(prices[k] * stock[k] for k in prices)
print(f'Total stock value: ${total_value:.2f}')"""),
                ("Set Operations", """a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f'Union: {a | b}, Intersection: {a & b}')""")
            ]
        }
    ]
    
    # Pick a category based on the day
    cat = categories[day % len(categories)]
    title, code_snippet = cat["topics"][day % len(cat["topics"])]
    
    return {
        "title": f"Exploring {cat['name']}: {title}",
        "description": f"Internalizing {cat['name']} concepts through the {title} exercise.",
        "tasks": [f"Implement {title}", "Test edge cases", "Documentation"],
        "code": f"# Day {day}: {title}\n{code_snippet}\n"
    }
