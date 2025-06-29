import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nScore => You: {user_score} | Computer: {computer_score}")
        
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
