import random
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
# to largest) and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.

user_list = []  # list is empty
elements = int(input('how many elements do you want your list to have?: '))  # user defines range for list
for i in range(elements):  # i represents each variable in range of 'elements'
    user_list.append(random.randrange(elements))  # elements of list are random given user input for range
list.sort(user_list)  # sorts random list of integers from least to greatest
print(user_list)

num1 = int(input('enter a number: '))


def inside_list(num1):  # function takes in one augment given by user input
    if num1 in user_list:  # if num1 is in list
        print('The number you entered is in the list')
    else:  # if num1 is not in list
        print('The number you entered is not in the list')
inside_list(num1)  # calls function