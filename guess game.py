import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I've picked a random number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed it right. The secret number was {secret_number}.")
                print(f"You took {attempts} attempts to win!")
                break
            elif user_guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
