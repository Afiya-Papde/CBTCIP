import random

def guess_number():
    return str(random.randint(1000, 9999))

def check_guess(secret, guess):
    correct_digits = sum(a == b for a, b in zip(secret, guess))
    return correct_digits

def play_game(player1, player2):
    print(f"{player1}, set your secret number.")
    player1_secret = input("Enter your 4-digit number: ")
    print("\n" * 50)  # Clear the screen

    print(f"{player2}, it's your turn to guess.")
    attempts = 0
    while True:
        guess = input("Guess the 4 digit number: ")
        attempts += 1
        if guess == player1_secret:
            print(f"Congratulations {player2}! You've guessed the number in {attempts} tries! You're a Mastermind!")
            return player2
        else:
            correct_digits = check_guess(player1_secret, guess)
            print(f"Not quite the number. But you did get {correct_digits} digit(s) correct!\n")

def main():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    print(f"Welcome {player1} and {player2} to the Mastermind game!")

    player1_score = 0
    player2_score = 0

    while True:
        winner = play_game(player1, player2)
        if winner == player2:
            player2_score += 1
        else:
            player1_score += 1

        print(f"\nCurrent score: {player1}: {player1_score}, {player2}: {player2_score}\n")

        input("Press Enter to continue...")

        print("\n" * 50)  # Clear the screen

        winner = play_game(player2, player1)
        if winner == player1:
            player1_score += 1
        else:
            player2_score += 1

        print(f"\nCurrent score: {player1}: {player1_score}, {player2}: {player2_score}\n")

        input("Press Enter to continue...")

        print("\n" * 50)  # Clear the screen

if __name__ == "__main__":
    main()
