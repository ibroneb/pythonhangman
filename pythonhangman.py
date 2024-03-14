#In this game of hangman, the computer will select a random word and the user will attempt to guess
#the correct letters of the word before the hangman stick figure is completely shown.
#(If a letter appears twice in the chosen word, then it must be guessed twice).



import random


#Creating a function to store the game. Creating variable for word list and variable to track wrong guesses.
def hangman():
    word_list = ["Python", "programmer", "words", "hacker", "gamer", "fun", "computer", "internet"]
    random_num = random.randint(0, 7)
    word = word_list[random_num]
    wrong_guesses = 0
    #strings to draw the hangman and letter board. Variable to keep track of remaining letters.
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["_ "] * len(word)
    win = False
    print('Welcome to Hangman')
    #while loop to keep game going. If player guesses more wrong letters than strings of the hangman, game is over.
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        #if player guesses correctly, update board list to display remaining letters.
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
    #loops to determine of player won or lost.
        if '_ ' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()