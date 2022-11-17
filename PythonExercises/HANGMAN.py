###HANGMAN GAME###
from random_word import RandomWords
r = RandomWords()

word = list(r.get_random_word().upper())
numLives = 10
blank = "_"
blankList = ["_"]*len(word)

def HangMan():
    global numLives
    global word
    global blank
    correct = False
    while not correct:
        if blank in blankList:
            print(blankList)
            guess = input("Guess a Letter: ")
            guess = guess.upper()
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        blankList[i] = guess
                print(f"Lives Left: {numLives}")
            else:
                if numLives == 1:
                    print("Game Over:(")
                    print(f"The Word was: {''.join(word)}")
                    break
                else:
                    print("Incorrect! Try again")
                    numLives -= 1
                    print(f"Lives Left: {numLives}")
        else:
            print("You Win!!!!!!!!!")
            print(''.join(blankList))
            break
    
HangMan()
