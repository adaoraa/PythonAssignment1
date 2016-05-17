import random
# Take two lists, say for example these two:...
# and write a program that returns a list that
# contains only the elements that are common between
# the lists (without duplicates). Make sure your program
# works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_list=list(set(a).intersection(b)) # intersection: finds commonalities
print(common_list)

num1=int(input('How many numbers do you want list1 to have? '
      'enter a number between 5 and 12: '))
num2=int(input('How many numbers do you want list2 to have? '
      'enter a number between 5 and 12: '))
range_list1= int(input('Starting at 1, at what integer do '
                       'you want your list to end?: '))
range_list2= int(input('Starting at 1, at what integer do '
                       'you want your list to end?: '))
x=random.sample(range(range_list1),num1)
y=random.sample(range(range_list2),num2)
print(x)
print(y)
common_elements=list(set(x).intersection(y))
print(common_elements)

# variable x generates random list given range the user inputs
# variable y does the same as variable x
# The varaible common_elements prints the common elements between the random lists
    # Sometimes there will be no common elements which is why this is impractical