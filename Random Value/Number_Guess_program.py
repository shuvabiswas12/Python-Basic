# This is guess the number game

import random as rd, sys

print('Hello, What\'s your name')
name = input()

print('Well '+name+', I am thinking number between 1 to 20. \nCan you guess the number ?')
print('You can only try for 6 time at a time ...')

guessNumber = rd.randint(1, 20)

attempt = 0

for i in range(0, 6):
    attempt = attempt + 1
    print('Enter the number: ')
    global number
    number = int(input())
    if number > guessNumber:
        print('Hey '+name+', the secret number is smaller than you guess which one.')
    elif number < guessNumber:
        print('Hey '+name+', the secret number is bigger than you guess which one.')
    else:
        break;
        

if number == guessNumber:    
    print('Your guess number is '+str(number)+' and the thinking number is '+str(guessNumber))
    print('You have try '+str(attempt)+' times')
else:
    print('Sorry! You have not to success to find that secret number')
    print('You have try '+str(attempt)+' times')
    
print('Program terminated')
sys.exit()
