
#Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that
#  are less than 5.

a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[x for x in a if x < 5] #creates new list of integers < 5
print(b)
