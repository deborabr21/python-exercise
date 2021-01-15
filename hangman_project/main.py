import random


def hangman(word):
    wordlist = [word]
    word = random.choice(
        open("C:\\Users\\Debora\\PycharmProjects\\hangman\\resources\\word-list.txt").readlines()).rstrip("\n")

    wrong_guesses = 0
    stages = ["",
              "__________      ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    # letters - letters is a list containing each character in the variable word.
    letters = list(word)

    board = ["__"] * len(word)
    win = False
    print("\n***********************")
    print(" Welcome to Hangman!!!!")
    print("***********************\n")
    guessed = []
    tries = 6

    while not win and tries > -1:
        print("\n")
        # Collect player guess and save it in the variable guess
        guess = input("Guess a letter: ").strip()
        guessed.append(guess)
        clist = [x.upper() for x in guessed]
        print(f"Guessed letters: {clist}")
        # enumerate letters so that if there are multiple instances of a letter, they may all be found
        for ind, item in enumerate(letters):
            if item == guess:
                board[ind] = item.upper()
        # Check if guess is in the list of letters
        if guess in letters:
            print(f"Letter {guess.upper()} was found!")
            if tries == 1:
                print(f"You have {tries} try left!")
            else:
                print(f"You have {tries} tries left!")
            # If player guessed correctly we get the index of the first occurrence of a character
            cind = letters.index(guess)
            # replace the letter guessed with a dollar sign
            letters[cind] = '$'
        else:
            print(f"Letter {guess.upper()} is not on the board!")
            if tries == 1:
                print(f"You have {tries} try left!")
            else:
                print(f"You have {tries} tries left!")
            # if player guess is incorrect we increment the variable wrong_guesses by 1.
            wrong_guesses += 1
            tries -= 1
            # Call the join method on a space and pass it to a variable board which prints out the board
        print((" ".join(board)))
        e = wrong_guesses + 1
        print("\n".join(stages[0: e]))
        # Check if there are any more underscores left
        if "__" not in board:
            print("Congrats, you guessed the word! You win!")
            print(" ".join(board).upper())
            win = True
            break
    if not win:
        print(f"Sorry, you ran out of tries. The word was {word.upper()}.")


if __name__ == "__main__":
    hangman("word")