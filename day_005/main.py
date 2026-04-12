import random

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
