import random

# Step 1: Random number generate
secret_number = random.randint(1, 100)

print("🎮 Welcome to Number Guessing Game!")
print("guess a number between 1 to 100 .")

# Step 2: Loop until correct guess
while True:
    guess = int(input("enter your guess number: "))
    
    if guess < secret_number:
        print("Too Low!  try again:")
    elif guess > secret_number:
        print("Too High! try again")
    else:
        print("🎉 Congratulations! you guess right :", secret_number)
        break