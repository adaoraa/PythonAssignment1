import random
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.


num1 = 2  # variable assignment
attempts = 0  # variable assignment
while num1 > 0:  # loop will run given that initial assignment of 2 is greater than 1, which is true
    random_int = random.randint(1, 9)  # variable ranges from 1-9
    user_guess = int(input('Guess what number the random generator will produce between 1 and 9: '))  # user guesses int
    correct_guess = user_guess & random_int  # variable = user input and random int. generated
    print(random_int)
    attempts += 1  # keeps track of each time loop runs
    if user_guess < random_int and user_guess in range(1, 9):  # tells user they guessed too low
        print('You guessed too low')
    elif user_guess > random_int and user_guess in range(1, 9):  # tells user they guessed too high
        print('You guessed too high')
    elif user_guess > 9 or user_guess < 1:  # error message for when user guesses out of range
        print('Your guess is not within range')
    elif correct_guess:  # tells user they guessed right
        print('You guessed exactly right')
        print('You guessed the correct number in this many attempts:', attempts)
        break  # once user guesses correctly, quit program



