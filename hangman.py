import random


def get_word_and_hint(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    random_line = random.choice(lines)
    f.close
    return random_line


def get_word(word_and_hint):
    word = word_and_hint.split("-")[0]
    return word


def get_hint(word_and_hint):
    hint = word_and_hint.split("-")[1]
    return hint


def win(revealed_word):
    return "_" not in revealed_word


def play(word, hint):
    revealed_word = []

    for char in word:
        if char == " ":
            revealed_word.append(" ")
        else:
            revealed_word.append("_")

    print("".join(revealed_word))

    used_words = []
    lives = 3

    while True:
        letter = input("Guess a letter: ")

        if letter in used_words:
            print("This letter has already been guessed. Try a different letter.")

        else:

            if letter not in word:
                print("Incorrect!")
                lives -= 1

                if lives > 1:
                    print(lives, " lives left")
                if lives == 1:
                    print(lives, "life left")

                    want_hint = input("Do you want a hint?")

                    if want_hint == "yes":
                        print(hint)

                    print("".join(revealed_word))

                if lives == 0:
                    print("You've lost.")
                    break

                used_words.append(letter)

            else:
                print("Correct!")

                for i in range(len(word)):
                    if word[i] == letter:
                        revealed_word[i] = letter

                print("".join(revealed_word))
                used_words.append(letter)

                if win(revealed_word):
                    print("You win!")
                    break


word_and_hint = get_word_and_hint("words_list.txt").replace("_", " ")
word = get_word(word_and_hint)
hint = get_hint(word_and_hint)

play(word, hint)
