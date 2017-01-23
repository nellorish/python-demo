import random


def get_random_word():
    words = ["pizza", "cheese", "apples", "oranges", "Manju"]
    word = words[random.randint(0, len(words) - 1)]
    return word


def show_word(word):
    for character in word:
        print(character, "", end="")
    print("")


def get_guess_word():
    print("Enter the letter word")
    return input()


def process_letter(letter, secret_word, blanked_word):
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            blanked_word[i] = letter
            result = True
    return result


def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print("X", end="")
    print("")


def play_word_game():
    strikes = 0
    max_strikes = 3
    word = get_random_word()

    blanked_word = list("_" * len(word))

    playing = True

    while playing:
        show_word(blanked_word)
        letter = get_guess_word()

        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)
        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("LOSER...!")
    else:
        print("Winner")


print("Started Playing Word Game")
play_word_game()
print("Game Over ..!")
