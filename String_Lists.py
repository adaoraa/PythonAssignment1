#Ask the user for a string and print out whether this string
# is a palindrome or not. (A palindrome is a string that reads
# the same forwards and backwards.)

string=input('Input a string: ')
if string[:]==string[::-1]:
    print('Your string is a palindrome')
else:
    print('Your string is not a palindrome')
for i in range[0:len(string)-1:]:
    j=len(string)-1
    if string[i]==string[j]:


# string[:]-accounts for all letters in string from start to end
# string[::-1]-accounts for every letter in string from start to end, but backwards

#practice exercise
practice_string='howdy'
print(practice_string[::-1])

practice_string1='kaya'
print(practice_string1[0:len(practice_string1)])



