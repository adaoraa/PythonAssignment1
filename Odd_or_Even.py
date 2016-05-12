
#Ask the user for a number. Depending on whether the number is even or odd,
#  print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

a=int(input('Enter a number: '))
if a%2 == 0 and a%4 ==0:
    print('You entered an even number that is a multiple of 4')
elif a%2==0:
    print('You entered an even number')
else:
    print('You entered an odd number')

num=int(input('input a number: '))
check=int(input('input a number: '))
if check%num==0:
    print('the result is even')
else:
    print('the result is not even')
