
import random

def start_game():

    def welcome():
        print("Welcome to my Numbers Guessing Game!  Enter a number between 1 and 20 to start the game. Thanks for playing.")

    welcome()

    n = 20
    random_number = random.randint(1,20)
    guess = 0

    guess_number = 0
    empty_list = []
    
    def add_to_list(item):
        empty_list.append(item)
        print(empty_list)
        

    while guess != random_number:
        guess = int(input("Enter Number: "))
        
        guess_number += 1
        
        if guess > 0:
            if guess > 20:
                print("Number ouside of the range. Enter a number between 1 and 20")  
                
            elif guess > random_number:
                print("Number to large. Please try again.")
            
            elif guess < random_number:
                print("Number too small. Please try again.")
            
        else:
            break
    else: 
    
        print("Congratulations! You guessed the correct number! It took you", guess_number, "number of tries. Would you like to play again? If yes, enter 'YES'. If no, enter 'NO'.")
        
    
    add_to_list(guess_number)
    
    

    answer = input()

    while answer != "":
    
        if answer == "YES":
            
            start_game()
        elif answer == "NO":
            print("Game Over. Thank you for playing.")
            break
            
    
        
        

    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
