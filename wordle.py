
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import random

def green(text):
    print(Fore.GREEN+text+Style.RESET_ALL, end="")

def red(text):
    print(Fore.RED+text+Style.RESET_ALL, end="")

def white(text):
    print(Fore.WHITE+text+Style.RESET_ALL, end="");

def newline():
    print()

#reading answers.txt
file1 = open("answers.txt", "r")
#splitting string into list
answers=file1.read().split()
file1.close()

#reading valid guesses.txt
file2 = open("validGuesses.txt", "r")
validGuesses=file2.read().split()
file2.close()

for answer in answers:
    validGuesses.append(answer)

randomAns = random.choice(answers)

def wordle(guess, attempt):
    for i in range (5):
        #guessing character from user input
        guessChar = guess[i]
        #answer word character being compared
        ansChar = randomAns[i]

        if(guess == randomAns):
            print("you guessed the word")
            return True
        elif(guessChar == ansChar):
            green(guessChar)
        elif(guessChar in randomAns):
            red(guessChar)
        else:
            white(guessChar)

    #if attemps exceeds limit, the word will be revealed
    if attempt == 10:
        print("\n you lost! The word was: ", randomAns)
        return True

    return False
attempts = 0

while (True):

    guess = input("\nguess: ")
    output = ("")
    result = wordle(guess, attempts)
    attempts += 1
    if(result == True):
        break

colorama_init()

newline()
