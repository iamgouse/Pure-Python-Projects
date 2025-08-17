import random

def number_guessing_game():
    target = random.randint(1, 100)
    attempts = 0

    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
                continue

            if guess < target:
                print("🔽 Too low! Try a higher number.")
            elif guess > target:
                print("🔼 Too high! Try a lower number.")
            else:
                print(f"✅ Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("🚫 Invalid input. Please enter a number.")

# 🔁 Run the game
number_guessing_game()
