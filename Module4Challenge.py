# Author: Elias Sjostrom
# Date: 6/28/26
import random

print("Welcome to the Magical Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("But watch out, the number could change if you use too many guesses!")
secret_number = random.randint(1, 100)
print("Start guessing!")

# variable for determining guess count (I find this easier to do than a loop to be honest)
guesses = 0

# the whole guessing code
while True:
    guess = int(input())
    guesses += 1
    
    # if we guess the right number
    if guess == secret_number:
        print("Congratulations! you guessed the number!")
        break
    # if we didnt guess the right number
    else:
        print("Not quite! Try again:")
        # counts the number of guesses and guesses remaining
        guesses_left = 5 - guesses
        if guesses_left == 1:
            print(f"You have {guesses_left} guess remaining. Last chance!")
        else:
            print(f"You have {guesses_left} guesses left. Keep trying!")
    
    # account for some number errors
    if guess > 100:
        print("The number will never be above 100.")
    # too high/low hints
    if guess > secret_number:
        print("Hint: your guess is too high!")
    elif guess < secret_number:
        print("Hint: your guess is too low!")

    # the end of the game
    if guesses == 5:
        print("Your 5 guesses are up!")
        print("Would you like to keep playing?(yes/no)")
        continue_answer = input().lower()
        
        # if the user wants to keep playing
        if continue_answer == "yes":
            print("A new number has been generated.")
            secret_number = random.randint(1, 100)
            guesses = 0
        # if they no longer want to play
        else:
            print("The secret number is:")
            print(secret_number)
            break
