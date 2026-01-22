import random

def roll_dice():
    return random.randint(1, 6)

def play_game(player_name):
    score = 0

    print(f"\nWelcome, {player_name}!")
    print("Let's roll the dice!")
    print("Type 'r' to roll or 'q' to quit.")

    while True:
        choice = input("Your choice: ").lower()

        if choice == 'q':
            print(f"{player_name}, you quit the game.")
            break
        elif choice == 'r':
            dice = roll_dice()
            score += dice
            print(f"You rolled a {dice}. Total score: {score}")

            if score >= 20:
                print(f"Congratulations, {player_name}! You reached 20 points and won!")
                break
        else:
            print("Invalid choice. Please type 'r' or 'q'.")

def main():
    print("Dice Rolling Game")
    player_name = input("Enter your name: ")

    while True:
        play_game(player_name)
        again = input("Play again? (y/n): ").lower()

        if again != 'y':
            print(f"Thanks for playing, {player_name}!")
            break

if __name__ == "__main__":
    main()
