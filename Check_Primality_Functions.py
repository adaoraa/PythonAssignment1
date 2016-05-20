# Ask the user for a number and determine whether the number is prime or not.


x = int(input('Enter a number between 1 and 100: '))
divisors = []
n=range(1,101)
for i in n:
    if x % i == 0:
        divisors += [i]
print(divisors)
if len(divisors) == 2:
    print('The number you entered is prime')
else:
    print('The number you entered is not prime')