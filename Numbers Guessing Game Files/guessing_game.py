"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random



def welcome():
    print("Welcome to my Numbers Guessing Game!  Enter a number between 1 and 20 to start the game. Thanks for playing.")

welcome()


  
n = 20
random_number = int(n * random.random()) + 1
guess = 0

guess_number = 0
  

while guess != random_number:
    guess = int(input("Enter Number: "))
    guess_number += 1
    if guess > 0:
        if guess > 20:
                print("Number ouside of the range. Enter a number between 1 and 20")  
                continue
        
        elif guess > random_number:
            print("Number to large. Please try again.")
            
        elif guess < random_number:
            print("Number too small. Please try again.")
            
    else:
         break
else: 
    print("Congratulations! You guessed the correct number! It took you", guess_number, "number of tries. Would you like to play again?")
    
      
  




def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
