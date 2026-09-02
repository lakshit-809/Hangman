import random

# Function to choose a random word
def choose_word():
    words = ["python", "hangman", "computer", "keyboard", "internship"]
    return random.choice(words)


# Function to display current progress of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


# Function to show hangman stages (simple text version)
def show_hangman(wrong_guesses):
    stages = [
        "Good luck!",
        "You made 1 wrong guess.",
        "2 wrong guesses... be careful!",
        "3 wrong guesses... halfway there!",
        "4 wrong guesses... danger zone!",
        "5 wrong guesses... last chance!",
        "6 wrong guesses... GAME OVER!"
    ]
    print(stages[wrong_guesses])


# Main game function
def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("=" * 50)
    print("       WELCOME TO PYTHON HANGMAN GAME")
    print("=" * 50)
    print(f"The word has {len(word)} letters. Guess one letter at a time!")

    while wrong_guesses < max_wrong_guesses:
        print("\n" + display_word(word, guessed_letters))
        show_hangman(wrong_guesses)

        guess = input("Guess a letter: ").lower()

        # Check valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + display_word(word, guessed_letters))
            print(f"Congratulations! You guessed the word: {word}")
            break

    else:
        print(f"\nGame over! The word was: {word}")

    print("-" * 50)
    print("Thanks for playing!")


# Run the game
if __name__ == "__main__":
    play_hangman()