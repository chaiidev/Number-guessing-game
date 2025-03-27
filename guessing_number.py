import random

# Pick a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("🎉 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it!")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():  # Check if input is a number
        print("❌ Invalid input! Please enter a number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("🔽 Too low! Try again.")
    elif guess > secret_number:
        print("🔼 Too high! Try again.")
    else:
        print(f"🎯 Correct! You guessed the number {secret_number} in {attempts} attempts. 🎉")
        break  # Exit loop when correct
