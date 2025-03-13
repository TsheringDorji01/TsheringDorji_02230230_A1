import random

def guess_number():
    number = random.randint(1, 100)
    print("\nWelcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Guess a number: "))
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("\nWelcome to Rock Paper Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to return to the menu): ").lower()
        if user_choice == "exit":
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit program")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            guess_number()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()