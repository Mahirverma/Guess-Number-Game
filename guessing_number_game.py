from random import randint

# generate a number from 1 to 10

answer = randint(1, 10)

# Take input from a user
# Check that input is a number between 1 to 10
# Check if the  number is the right guess
# Otherwise ask again

while True:
    try:
        guess = int(input('Guess a number from 1 to 10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('Great, you guess the correct number')
                break
            elif guess > answer:
                print("Guess a shorter number.")
            elif guess < answer:
                print('Guess a larger number.')
        else:
            print('Please enter a number from 1 to 10.')
    except ValueError:
        print('Please enter a number.')
        continue
