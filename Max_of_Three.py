# Implement a function that takes an input of three variables, and returns the largest of the three.
# Do this without using the Python max() function!

num1 = int(input('Enter a number: '))  # prompts user to input first variable
num2 = int(input('Enter a number: '))  # prompts user to input second variable
num3 = int(input('Enter a number: '))  # prompts user to input third variable
num_list = [num1, num2, num3]  # creates list of all three variables
print(num_list)


def largest(num1,num2,num3):  # function takes in 3 augments, all defined by user's input
    if num1 > num2 and num1 > num3:  # num1 is max
        print('The max is:', num1)
    elif num2 > num1 and num2 > num3:  # num2 is max
        print('The max is:', num2)
    else:
        print('The max is:', num3)  # num3 is max

largest(num1, num2, num3)  # calls function