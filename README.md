# PythonAssignment1
Throughout the summer, I am going to be enhancing my programming skills. One language I am trying to gain proficiency in is python. This is my first assignment. I take my assignments from: http://www.practicepython.org/ 

import datetime

name = input('What is your name?:')
print('My name is ' +name)
age = input('How old are you?:')
age = int(age)
answer=input('Would you like to know what year you turn 100? Enter "yes" or "no"')
a=datetime.datetime.now() #gives me current date and time
if answer == 'yes':
    b=(a.year+(100-age)) #a.year gives me current year
    print(b)
    d=(input('Enter a number: '))
elif answer == 'no':
    print('goodbye')

Yields: 
What is your name?:Adaora
My name is Adaora
How old are you?:18
Would you like to know what year you turn 100? Enter "yes" or "no"yes
2098

Process finished with exit code 0
