"""
What will the Program do?
1 Start
2 Generate random number to guess
3 Ask player for guess
4 Was the Guess correct?

----> If YES ----> Print Out Results
----> If NO  ---->

5 Was the Guess Lower?----->YES---> 6 Print lower Message
6 NO ----> Print Higher Message
7 Are number of goes up?---> If NO Go to step 3
8 If YES ----> Print Out Results

Logic
1. The program randomly selects a number between 1 and 10.
2. It will then ask the player to enter their guess.
3. It will then check to see if that number is the same as the one the
   computer randomly generated, if it is then the player has won.
4. If the player’s guess is not the same, then it will check to see if the number is
   higher or lower than the guess and tell the player.
5. The player will have 4 goes to guess the number correctly; if they don’t guess
   the number within this number of attempts, then they will be informed that they
   have lost the game and will be told what the actual number was.


look for exception handling
functions
make code reusable
change the code format to make functions reusable.

"""
import random

print("Welcome to the Number Guessing Game!")
play_again = 'y'

while play_again.lower() == 'y':
    # Return random Integer between 1 and 10 inclusive
    number_to_guess = random.randint(1,10)
    # Counter
    guess_counter = 1

    # Check if the counter is no more than 4 attempts.
    while guess_counter <= 4:
        # user_guess = int(input("Please guess a number between 1 and 10: "))

        try:
            user_guess = int(input("Please guess a number between 1 and 10: "))

        except ValueError as e:
            print("Invalid Input! Please enter only numbers!")
            user_guess = int(input("Please guess a number between 1 and 10: "))

        # if user further gives invalid input

        if user_guess < 1 or user_guess > 10:
            print("Please guess a number between 1 and 10")
            # if the condition is correct, continue, else repeat the same message.
            continue

        # Check if user guessed the right number
        if number_to_guess == user_guess:
            print("Great, your guess is correct!")
            print(f"You took {guess_counter} number of tries to complete the game.")
        elif user_guess < number_to_guess:
                print("Your guess was lower than the number.")
        else:
            print("Your guess was higher than the number.")

        # Update the counter
        guess_counter +=1
        if guess_counter >4:
            print("Sorry, you've reached the maximum number of attempts!")
            print(f"The number you need to guess was {number_to_guess}")

    # Choice to play again or abort the game
    play_again = input("Would you like to guess the number again? (y/n): ")
# Once the game is over, print the msg
print("Game Over!")
# user input


