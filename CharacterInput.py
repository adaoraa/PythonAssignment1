import datetime

#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

#1. Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)

#2. Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

name = input('What is your name?:')
print('My name is ' +name)
age = input('How old are you?:')
age = int(age)
answer=input('Would you like to know what year you turn 100? Enter "yes" or "no"')
a=datetime.datetime.now() #gives me current date and time
if answer == 'yes':
    b=(a.year+(100-age)) #a.year gives me current year
    print(b)
elif answer == 'no':
    print('goodbye')

