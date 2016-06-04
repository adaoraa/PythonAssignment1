import random
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
# minus all the duplicates.

length = int(input('How many integers do you want your list to have?: '))
print('You want your list to have', length, 'integers')

user_list = []  # empty list needing integers based on user's input
for i in range(length):  # generates each element for list that is within range given by user
    user_list.append(random.randrange(length))  # append list with random integers of range given by user
print(user_list)

user_set = set(user_list)  # set eliminates duplicates
print(user_set)
