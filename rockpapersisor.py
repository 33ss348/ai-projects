import random


choices = ["rock", "paper", "scissors"]


player_history = []

def ai_move(player_history):
    if not player_history:
        # First move - pick random
        return random.choice(choices)
    
    last_move = player_history[-1]

   
    if last_move == "rock":
        return "paper"    # Paper beats Rock
    elif last_move == "paper":
        return "scissors" # Scissors beat Paper
    elif last_move == "scissors":
        return "rock"     # Rock beats Scissors


    return random.choice(choices)

def winner(player, ai):
    if player == ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return "player"
    else:
        return "ai"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'quit' to stop playing.\n")

    while True:
        player = input("Choose rock, paper, or scissors: ").lower()
        if player == "quit":
            print("Thanks for playing!")
            break
        if player not in choices:
            print("Invalid choice! Try again.")
            continue

        # Save player history
        player_history.append(player)

        
        ai = ai_move(player_history)
        print(f"AI chooses: {ai}")

        # Decide winner
        result = winner(player, ai)
        if result == "draw":
            print("It's a draw!\n")
        elif result == "player":
            print("You win!\n")
        else:
            print("AI wins!\n")


if __name__ == "__main__":
    play_game()