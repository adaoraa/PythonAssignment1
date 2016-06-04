# Ask the user for a string and print out whether this string
# is a palindrome or not. (A palindrome is a string that reads
# the same forwards and backwards.)

string = input('Input a string: ')
if string[:] == string[::-1]:  # string[::-1]-accounts for every letter in string from start to end, but backwards
    print('Your string is a palindrome')  # string[:]-accounts for all letters in string from start to end
else:
    print('Your string is not a palindrome')



