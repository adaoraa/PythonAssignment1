
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

num=input('input a number: ')
num=int(num)
check=input('input a number: ')
check=int(check)
if check%num==0:
    print('the result is even')
else:
    print('the result is not even')

Yields: 
Enter a number: 10
You entered an even number
input a number: 2
input a number: 6
the result is even

Process finished with exit code 0
