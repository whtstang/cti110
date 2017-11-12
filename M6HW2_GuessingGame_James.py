# CTI 110
# M6HW2 - Guessing Game
# Jeremiah James
# 5 NOV 2017

import random

def generateRandomNumber():
    secretNumber = random.randint(1, 100)
    return secretNumber

def askUserForNumber(message = 'Guess a number between 1 and 100: '):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber(userNumber, secretNumber):
    if userNumber > secretNumber:
        return "Too high, try again."
    elif userNumber < secretNumber:
        return "Too low, try again."
    else:
        return "Congratulations!"

def main():
    playAgain = 'yes'
    

    while playAgain == 'yes':
        userNumberOfGuesses = 0
        secretNumber = generateRandomNumber()
        #print('For testing purposes: secret number: ', secretNumber)
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber(userNumber, secretNumber)

        while message != "Congratulations!":
            print(message)
            userNumber = askUserForNumber('Try again: ')
            userNumberOfGuesses += 1
            message = checkUserNumber(userNumber, secretNumber)

        print()
        print(message, "\n"'It took you', userNumberOfGuesses,\
              'try(s) to guess the number correctly\n')
        playAgain = input('Would you like to play again?(yes or no): ')

    print('\nThanks for playing!')
        

main()


# -In this assignment, you will create a simple computer game in Python.
# -Write a program that does the following:
#   -Generate a random number in the range of 1 through 100.
#    (We’ll call this the “secret number”).
#   -Ask the user to guess what the secret number is.
#       -If the user’s guess is higher than the secret number,
#       the program should tell the user Too high, try again.
#       -If the user’s guess is lower than the secret number,
#       the program should tell the user Too low, try again.
#       -If the user guesses the number correctly,
#       the program should congratulate the user!
#       Write whatever message you think is appropriate for this case.
#   -The program should then ask the user Play again? (y for yes).
#   -If the user enters ‘y’, then the program should generate
#   a new random number and start the game over again.


# -Extra Credit (optional)
#For extra credit, add the following enhancement to the game:
#   -Have the game keep track of the number of guesses the user makes.
#   When they guess correctly, tell the user how many guesses they used.
#   -You might also decide that user only gets X number of guesses per game,
#   and the game ends in a loss if they use all guesses before they guess the number.
#   (You will need to test for yourself and decide what a fair value for X would be!)









