# Number Guessing Game Project

import random

def guessing_game():
    secret_number = random.randint(1 ,100)
    attempts = 0
    print("choose one number between 1 to 100 : ")
    
    while True:
        guess = int(input("guess you no :"))
        attempts += 1
        
        if guess == secret_number:
            print(f"correct answer! you {attempts} try in right guess ।")
            break
        else:
            print("wrong  answer! plese Try Again।")

# Function call
guessing_game()
