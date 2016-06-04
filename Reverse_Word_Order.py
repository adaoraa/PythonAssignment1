# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

user_strings = input('input a string of words: ')  # prompts user to input string
user_set = user_strings.split()  # converts string to list
print(user_set)
backwards_list = user_set[::-1]  # makes user_set list print backwards
print(backwards_list)
