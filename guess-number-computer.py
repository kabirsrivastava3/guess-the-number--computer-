'''
Project on guessing of a secret number of computer by user using random library.
'''

import random

def guessNumberComputer(number):
    randomNumber = random.randint(1, number)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {number}: "))
        if guess < randomNumber:
            print(f"Sorry! Try to guess again. Too low!!")
        elif guess > randomNumber:
            print(f"Sorry! Try to guess again. Too high!!")
    
    print(f"Wow!! Nice job!! You guess the number correctly as {randomNumber}!!!")


print("Enter the range of number")
output = int(input())
guessNumberComputer(output)

# Test Case
#guessNumberComputer(10)