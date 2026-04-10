import sys
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
