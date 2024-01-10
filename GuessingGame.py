import random
def display_title():  
    print ("Guess the Number!")
    print()
def play_game(limit):
    number=random.randint(1,limit)
    print(f"I'm thinking of a number between 1 and {limit}\n.")
    count=1
    guess=int(input("What is your guess? "))
    
    while(guess!=number):
        if guess>number:
            print("Too high.")
            count+=1
        elif guess<number:
            print("Too low.")
            count+=1
        guess=int(input("Your guess: "))
            
    print(f"You guessed it in {count} attempts.\n")
def main():
    display_title()
    again="yes"
    while again.lower()=="yes":
        limit=int(input("Enter the limit:"))
        play_game(limit)
        again=input("Would you like to play again? Type yes or no: ")
        print()
    print("Thanks for playing! See Ya!")
     
if __name__=="__main__":
    main() 