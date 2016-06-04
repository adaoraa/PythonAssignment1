import random

# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

count = int(input('How many fibonacci numbers would you like to generate?: '))  # fibonacci numbers to generate
print('We are going to generate', count, 'fibonacci numbers')
count_list = [i for i in range(count)]  # generates list of length count variable integer
fibonacci_list = [1, 1]  # the fibonacci sequence initially starts with two 1's


def main(fibonacci_list):  # function definition main has 1 augment given by fibonacci_list
    return fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    # append fibonacci list w/ pattern that starts w/ 1 and adds previous 2 elements; list ends in length given by user

for i in range(count):  # accounts for every element in range given by user
    main(fibonacci_list)  # calling function 
print(fibonacci_list)
