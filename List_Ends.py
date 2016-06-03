# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list.
# For practice, write this code inside a function.


num1 = int(input('Enter a number: '))  # prompts user to input number representing first element of list
num2 = int(input('Enter a number: '))  # prompts user to input number representing second element of list
num3 = int(input('Enter a number: '))  # prompts user to input number representing third element of list
num4 = int(input('Enter a number: '))  # prompts user to input number representing fourth element of list
num5 = int(input('Enter a number: '))  # prompts user to input number representing fifth element of list
user_list = [num1, num2, num3, num4, num5]  # creates list of integers
print(user_list)
print(user_list[0], user_list[-1])  # returns first and last elements of list
