import random

guessesTaken = 0
Name = input(str('Hello! What is your name?'))
number = random.randint(1, 10)
print('Well, ' + Name + ', I am thinking of a number between 1 and 10.')
while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input('Take a guess on a number bewteen 1 and 10')
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + Name + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number and guessesTaken == 6:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)