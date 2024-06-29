import random

print("Welcome to rock_paper_scissor game. There are some instruction that you need to know before paying this game:\n",
      "1. Objective:\n"
            " The goal of the game is to select a move (rock, paper, or scissors) that"
            "defeats your opponent's move according to the game rules.\n"
      "2. Moves and rules:\n"
            "  Rock crushes Scissors (Rock wins)"
            ", Scissors cuts Paper (Scissors wins),"
            " Paper covers Rock (Paper wins),"
            " If both players choose the same move, it is a tie.")
print("Feedback:\n"
      "If the player win: You win this round!\n"
      "If the player defeat: Computer wins this round!\n"
      "If it's a tie: It's a tie! Try again.\n")
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = int(input("Enter the number of rounds you want to play: "))

    user_score = 0
    computer_score = 0

    for round in range(1, rounds + 1):
        print(f"\nRound {round}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie! Try again.")

        print(f"Score after round {round}: You {user_score} - Computer {computer_score}")

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations, you won the game!")
    elif computer_score > user_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("It's a tie! Try again")
if __name__ == "__main__":
    play_game()