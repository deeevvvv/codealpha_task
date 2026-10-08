import random

WORDS = ["python", "apple", "robot", "garden", "planet"]
MAX_WRONG = 6


def display_word(word, guessed):
    shown = ""
    for letter in word:
        if letter in guessed:
            shown += letter + " "
        else:
            shown += "_ "
    return shown.strip()


def play():
    word = random.choice(WORDS)
    guessed = []   # all letters the player has tried
    wrong = 0

    print("Welcome to Hangman!")
    print("Guess the word. You can make", MAX_WRONG, "wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", display_word(word, guessed))
        print("Wrong guesses left:", MAX_WRONG - wrong)
        print("Guessed letters:", " ".join(guessed))

        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed:
            print("You already guessed that letter.\n")
        else:
            guessed.append(guess)
            if guess in word:
                print("Good guess!\n")
            else:
                wrong += 1
                print("Wrong guess!\n")

        # Win check: every letter of the word has been guessed
        if all(letter in guessed for letter in word):
            print("Word:", display_word(word, guessed))
            print("Congratulations, you won!")
            return

    print("Game over! The word was:", word)


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()