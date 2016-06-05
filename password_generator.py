import random
import string
import locale
# Write a password generator in Python. Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

name = input('User, what do you want to set as your username?: ')  # allows user to create username
print('Your username is: '+name)
strength = input('How strong do you want your password (strong or weak): ')  # strength of password given by user
print('You want a '+strength, 'password')
number = random.randint(0, 9)  # generates random number between 0 and 9
symbol = string.punctuation  # generates random punctuation
lower_letters = string.ascii_lowercase  # generates lower case letters
upper_letters = string.ascii_uppercase  # generates upper case letters
password = []  # password is initially empty


def lowercase(lower_letters):  # function for lowercase letters
    return password.append(random.choice(lower_letters))  # generates random lowercase letter and appends to password


def uppercase(upper_letters):  # function for uppercase letters
    return password.append(random.choice(upper_letters))  # generates random uppercase letters and appends to password


def digit(number):  # function for integers
    return password.append(number)  # generates random integers and appends to password


def punctuation(symbol):  # functions for symbols
    return password.append(random.choice(symbol))  # generates random symbol and appends to password


if strength == 'strong':  # condition for strong password
    for _ in range(2):  # generates 2 random lowercase letters for password
        lowercase(lower_letters)
    for _ in range(2):  # generates 2 random uppercase letters for password
        uppercase(upper_letters)
    digit(number)  # calls number function
    punctuation(symbol)  # calls punctuation function
    print('Your new password is:', password)  # combination appended to password
else:  # condition for weak password
    for _ in range(5):  # generates 5 random lower case letters
        lowercase(lower_letters)
    print('Your new password is:', password)  # combination appended to password

# '_' after 'for' signifies a variable whose value you don't care about; commonly referred to as 'i' or 'j'
