import random #import the random package that is used to choose a random word
from words import words #imports the variable words from the words.py file
import string #used to import all uppercase letters in the alphabet

def getValidWord(words):
    word =random.choice(words) # randomly chooses somthing from the list
    while '-' in word or ' ' in word: #while loop that looks at the variable word to determine
        word = random.choice(words)#if it has a space or '-' in the word. if so it chooses another random word

    return word.upper()

def hangman():
    word = getValidWord(words) 
    wordLetters = set(word) #a set of all the letters in the random word chosen
    alphabet =  set(string.ascii_uppercase) #uppercase characters in the english dictionary
    usedLetters = set() #what the user has guessed
    lives = 6

    while len(wordLetters) > 0 and lives > 0: #creates a loop that keeps the game going until there are no more letters in wordLetters
        #letters used
        print(f'You have {lives} amount of lives left.','You have used these letters: ', ' '.join(usedLetters))

        # what current word is (i.e. W - R D)
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print("Current Word: ",' '.join(wordList))
        
        inputLetter = input("Guess a letter: ").upper() #user input
        if inputLetter in alphabet - usedLetters:
            usedLetters.add(inputLetter) #if the letter the user inputs is in the wordLetters set, then it will be added to the variable usedLetters
            if inputLetter in wordLetters:
                wordLetters.remove(inputLetter) #if the letter the user inputs is in the wordLetters set, then it removes the word form wordLetters

            else:
                lives = lives - 1 # takes a life away
                print('The letter you selected is not in the word. Try again')

        #if the input word is in usedLetters, then it prints exception statement
        elif inputLetter in usedLetters:
            print("This letter has been used already, please choose another letter.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You lost, the word was ", word)
    else:
        print('You guessed the word', word, '!!')

hangman()

#userInput = input("Type")