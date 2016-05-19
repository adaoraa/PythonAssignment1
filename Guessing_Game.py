import random
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.

num1 = 2 # variable assignment
while num1 > 0: # loop will run given that initial assignment of 2 is greater than 1, which is true
    random_int = random.randint(1, 9)  # variable ranges from 1-9
    user_guess = int(input('Guess what number the random generator will produce between 1 and 9: ')) # user guesses int.
    print(random_int)
    if user_guess < random_int: # tells user they guessed too low
        print('You guessed too low')
    elif user_guess > random_int: # tells user they guessed too high
        print('You guessed too high')
    elif user_guess > 9: # error message for when user guesses out of range
        print ('Your guess is not within range')
    else: # tells user they guessed right
        print('You guessed exactly right')
        break # once user guesses correctly, quit program
    
