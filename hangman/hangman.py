# Modify the game of hangman so a word is selected from a list of words.
import random

def hangman(word):
    # word - is the word player has to guess

    wordlist = []
    wordlist.append(word)
    # word-list.txt is a list of words, in the same directory with the game file.
    word = random.choice(open("C:\\Users\\debor\\PycharmProjects\\Hangman\\resources\\word-list.txt").readlines()).rstrip("\n")

    # wrong - keep track of incorrect guesses
    wrong = 0
    # stages - a picture of hangman
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    # rletters - remaining letters is a list containing each character in the variable word.
    # It keeps track of which letters are left to guess the variable
    rletters = list(word)

    # board is a list of strings you use it to keep track of the game board you display to player 2.
    # a board that looks like this this code populates the board list with an underscore for every character
    # in a variable word.
    board = ["__"] * len(word)

    # Your program also has a win variable that starts as false to keep track of whether Player 2 has won
    # the game yet.
    win = False
    print("\n***********************")
    print(" Welcome to Hangman!!!!")
    print("***********************\n")

    # A loop keeps the game going your loop continues as long as the variable wrong is less than # the length of the
    # stages list minus 1.
    # This means the game will continue until Player 2 has guessed more wrong letters and the # number of strings it
    # takes to create the hangman. You have to subtract one from the length of # the stages list to compensate for the
    # fact that the stages list starts counting from zero and # wrong starts counting at 1
    while wrong < len(stages) - 1:
        # Print a blank space to make the game look nice when it prints
        print("\n")
        # Collect player 2s guess and save it in the variable char
        msg = "Guess a letter: "
        char = input(msg)
        # You check to see if player 2 guessed correctly by seeing if their guess is in the list of remaining letters
        if char in rletters:
            # If player 2 guessed correctly you need to update your board list.
            # Python's index function returns the index the first occurrence of a character in a list to update your
            # board.
            cind = rletters.index(char)
            # You then use that index to replace the corresponding underscore in the board list with the letter they
            # guessed you replace the letter they guessed with a dollar sign so that the letter player to guest is no
            # longer in the remaining letters list replacing the letter with a character like a dollar sign is easier
            # than removing it from the list
            board[cind] = char
            rletters[cind] = '$'
        else:
            # if Player 2 guesses incorrectly you simply increment the variable wrong by 1 next.
            wrong += 1
            # You call the join method on a space and pass it to a variable board which prints out the board so Player
            # 2 can see it and use it to make their next guess.
        print((" ".join(board)))
        # Now it is time to print the hangman to print your hangman at whatever stage of the game is that you have to
        # slice your stages list.
        # You start at Stage 0 and slice up to the stage you are at represented by the variable wrong plus 1.
        # You add 1 because when you are slicing the end slice does not get included in the result slicing from 0 to
        # the integer stored in the variable wrong plus one gives you the strings you need to print the hangman at
        # whatever stage the game is at
        e = wrong + 1
        print("\n".join(stages[0: e]))
        # Finally you check if there are any more underscores left in the board list
        if "__" not in board:
            # If there aren't it means player to successfully guest every letter in the word and won the game.
            print("You win!")
            # If player 2 wins you print you in then you print the board one last time set the variable win to true
            # and break out of the loop. The program is over
            print(" ".join(board))
            win = True
            break
    if not win:
        # If they lost the variable win is false. If that is the case you print the full hangman and you lose followed
        # by the word they couldn't guess.
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


hangman("word")
