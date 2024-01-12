from hangman_function import *
def play_hangman():
    greeting()

    difficulty_choice = input("Enter the number: ")

    if difficulty_choice not in ("1", "2", "3"):
        print("Invalid difficulty. Exiting.")
        return

    lives = {"1": 7, "2": 5, "3": 3}[difficulty_choice]

    words = get_words('countries-and-capitals.txt', difficulty_choice)
    word_to_guess = choose_word(words)
    already_tried_letters = []
    current_game_state = initialize_game_state(word_to_guess)

    while True:
        print(display_game_status(current_game_state))
        print(display_hangman(lives))

        guess = input("Enter a letter or type 'quit' to exit: ").lower()

        if guess == 'quit':
            print("Bye!")
            break

        while guess in already_tried_letters:
            print("You already guessed that letter. Try again.")
            guess = input("Enter a letter or type 'quit' to exit: ").lower()

        already_tried_letters.append(guess)

        if is_guess_correct(word_to_guess, guess):
            current_game_state = update_game_state(word_to_guess, current_game_state, guess)
        else:
            lives -= 1
            print("Incorrect guess. Try again.")
            if lives == 0:
                print("Game over. The word was:", word_to_guess)
                break

        if '_' not in current_game_state:
            print("Congratulations! You guessed the word:", word_to_guess)
            break
        elif lives == 0:
            print("Game over. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    play_hangman()