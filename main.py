import random
import art

def start_game():
    print(art.logo)
    print("Welcome to the number guessing game")
    print("I am gussing the number between 1 to 100")
    
   
    random_no = random.randint(1, 100)
    
    
   
    easy_level = 10
    hard_level = 5
    
   
    select = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    
    
    if select == "easy":
        attempts = easy_level
    elif select == "hard":
        attempts = hard_level
    else:
        print("Invalid choice. Defaulting to easy mode.")
        attempts = easy_level

   
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))  
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess == random_no:
            print("You got it! The correct number was:", random_no)
            break
        elif guess < random_no:
            print("Too low.")
        else:
            print("Too high.")
        
        attempts -= 1 

    if attempts == 0:
        print(f"You've run out of guesses. The correct number was {random_no}.")
    


while True:
    print("\n" + "-" * 20 + "\n")
    start_game() 
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
