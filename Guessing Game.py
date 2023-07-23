import random

target = random.randint(1, 10)
# 1 is lowest 10 is highest
attempts = 0

while True:
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1

    if guess == target:
        print("Congratulations! You guessed the correct number in", attempts, "attempts.")
        break
    elif guess < target:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
