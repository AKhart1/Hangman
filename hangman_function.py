import random

def greeting():
    print("                        __                                           ")
    print("    _    _      ____    LJ    ____      ____     _ _____      ____   ")
    print("   FJ .. L]    F __ J   FJ   F ___J.   F __ J   J '_  _ `,   F __ J  ")
    print("  | |/  \| |  | _____J J  L | |---LJ  | |--| |  | |_||_| |  | _____J ")
    print("  F   /\   J  F L___--.J  L F L___--. F L__J J  F L LJ J J  F L___--.")
    print(" J\__//\\__/LJ\______/FJ__LJ\______/FJ\______/FJ__L LJ J__LJ\______/F")
    print("  \__/  \__/  J______F |__| J______F  J______F |__L LJ J__| J______F \n")

    print("Select difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

def get_words(file_path, difficulty):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            country, capital = map(str.strip, line.split('|'))
            if difficulty == "1":
                words.append(country)
            elif difficulty == "2":
                words.append(country)
                words.append(capital)
            elif difficulty == "3":
                words.append(capital)
    return words

def choose_word(words):
    return random.choice(words)

def initialize_game_state(word):
    return ['_' if letter.isalpha() else letter for letter in word]

def display_hangman(lives):
    hangman_art = [
        "  _____ ",
        " |     | ",
        " |     O ",
        " |    /|\\",
        " |    / \\",
        "_|_"
    ]
    return "\n".join(hangman_art[:len(hangman_art) - lives])

def display_game_status(game_state):
    return " ".join(game_state)

def is_guess_correct(word, guessed_letter):
    return guessed_letter.lower() in word.lower()

def update_game_state(word, game_state, guessed_letter):
    for i, letter in enumerate(word):
        if letter.lower() == guessed_letter.lower():
            game_state[i] = letter
    return game_state