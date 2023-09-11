import random
# constant variable for max attempts a user/player can try.
MAX_ATTEMPTS = 4
def welcome_msg():
    print("Welcome to the Number Guessing Game!")

def get_user_input():
    # check until a valid user input is provided.
    while True:
        try:
            user_input = int(input("Please enter your number in between 1 to 10."))
            if 1 <= user_input <= 10:
                return user_input
        except ValueError as e:
            print(f"Invalid Entry : please enter a number between 1 - 10 only.")

def play_again():
    while True:
        game_play_choices = input("Would you like to play again? y/n: ").lower()
        if game_play_choices == 'y':
            return  True
        elif game_play_choices == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
def play_num_g_game():
    while True:
        # define a random integer to a variable
        number_to_guess = random.randint(1,10)
        # initiate a counter/attempts once the user starts guessing
        attempts_left = MAX_ATTEMPTS

        while attempts_left > 0 :
            # get the user input
            user_input = get_user_input()
            if number_to_guess == user_input:
                print(f"Great guess {user_input}, you won!")

                # condition to play again
                if play_again() == 'y':
                    # if the user wants to play again, exit the inner loop.
                    break
                else:
                    # exit the entire function
                    return
            elif number_to_guess >= user_input:
                print(f"Your guess {user_input} was lower than the actual number.")
            else:
                print(f"Your guess {user_input} is higher than the actual number.")

            # update counter BY -1
            attempts_left -=1
        print(f"You used all of your 4 attempts. The actual number is {number_to_guess}"
                      f"but your guess was {user_input}. Sorry you lost.")
        # If user do not want to play again, call the play_again()
        if not play_again():
            # exit the game loop and terminate the program.
            return
def main():
    welcome_msg()
    play_num_g_game()
    print("Game over!")

# Only execute the main() func if the script is run as the main program
# not when imported as a module into another script.
if __name__ == "__main__":
    main()
