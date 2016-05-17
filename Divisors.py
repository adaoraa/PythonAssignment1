#Create a program that asks the user for a number and then
# prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that
# divides evenly into another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)

#Plan: 1)use keyword input; 2) use x%n ==0 for remainder
#3) use if statement, 4) incorporate for statement if necessary


x=int(input('Enter a number between 0 and 100: '))
n=range(1,101) # ranges from 1-100
divisor_list=[] # variable contains empty list
for i in n: # when the number the user chooses is within range...
    if x%i==0: # if x goes into a number w/no remainder...
        divisor_list+=[i] #...print the number in this variable's list
print('The following list of numbers are divisors: ',divisor_list)
# statement separated by comma because it contains 2 different
# types of augments