import os
import time
import random

# --- Setup basic functions ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_board(board, ball_row):
    clear()
    for i, line in enumerate(board):
        # show the ball in this row
        if i == ball_row:
            print(line[:4] + "🟣" + line[5:])
        else:
            print(line)
    print("\n")

# --- R1 (double score) mode ---
def r1_game(board, round_num, score):
    ball_row = len(board) - 1
    print(f"\n🎯 Round {round_num + 1} — Double Score Mode!")
    strike_choice = input("Choose your strike (left / right / straight): ").lower()

    # Random outcome
    random_end = random.choice(["left", "straight", "right"])

    # Move ball animation
    while ball_row >= 0:
        show_board(board, ball_row)
        time.sleep(0.1)
        ball_row -= 1

    # Result
    if random_end == "straight":
        print("💥 STRIKE! All pins down! 🎳🎳🎳")
        score += 2
    else:
        print(f"😅 The ball went {random_end} and missed!")
    return score

# --- Classic mode ---
def classic_game(board, round_num, score):
    ball_row = len(board) - 1
    print(f"\n🎯 Round {round_num + 1} — Classic Mode!")
    strike_choice = input("Choose your strike (left / right / straight): ").lower()

    # Random outcome
    random_end = random.choice(["left", "straight", "right"])

    # Move ball animation
    while ball_row >= 0:
        show_board(board, ball_row)
        time.sleep(0.1)
        ball_row -= 1

    # Result
    if random_end == "straight":
        print("💥 STRIKE! All pins down! 🎳🎳🎳")
        score += 1
    else:
        print(f"😅 The ball went {random_end} and missed!")
    return score

# --- Main game function ---
def play_game():
    clear()
    print("🎳 Welcome to the Bowling Game! 🎳")
    print("Choose your game type:")
    print("👉 R1 - Double score per strike")
    print("👉 CLASSIC - Normal scoring")
    
    user_game = input("Enter your choice (R1 / CLASSIC): ").upper()

    board = [
        "    🎳🎳🎳",
        "     🎳🎳",
        "      🎳",
        "      | |",
        "      | |",
        "      | |",
        "      | |",
        "      | |"
    ]

    score = 0
    rounds = 3 if user_game == "R1" else 7

    print("\nAvailable balls: Blue, Red, Black, White")
    user_ball = input("Select your desired ball color: ").lower()
    print(f"\nYou selected a {user_ball} ball! Let's start 🎳\n")
    time.sleep(1)

    for r in range(rounds):
        if user_game == "R1":
            score = r1_game(board, r, score)
        else:
            score = classic_game(board, r, score)
        time.sleep(1)

    print(f"\n🏆 Game over! Your total score in {user_game} mode is {score} points!")
    return user_game, score

# --- Play loop ---
while True:
    game_mode, total_score = play_game()
    play_again = input("\nDo you want to play again? (Y/N): ").upper()
    if play_again != "Y":
        print("\nThanks for playing! Have a great day! 🎳")
        break


