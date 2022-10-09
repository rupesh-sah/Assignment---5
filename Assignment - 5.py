'''Assignment - 5 Full Stack Web Development using Python MySirG

    Operators'''

'''(Q.1) Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)'''
num1 = 2354
print(int(str(num1)[:-1]))
# OUTPUT
# 253


'''(Q.2)Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)'''
num2 = 2089
print(int(str(num2)[-1]))
# OUTPUT
# 9

#(Q.3) Write a python script to swap data of two variables
a = 1
b = 2
a,b = b,a
print('a=',a)
print('b =', b)
# OUTPUT
# a= 2
# b = 1

# (Q.4) Write a python script to find x power y, where values of x and y are given by user
'''(Q.5) Write a python script which takes a three digit number from the user and displays
only its first digit.'''
num3 = int(input("Enter the three number "))
print(str(num3)[:1])

''' (Q.6) Write a python script which takes a three digit number from the user and displays
only its middle digit.'''

num4 = int(input("Enter the three number "))
print(str(num4)[1])

''' (Q.7) Write a python script which takes a three digit number from the user and displays
only its last digit.'''
num5 = int(input("Enter the three number "))
print(str(num5)[-1])

#(Q.8) Write a python script to use IN operator to display the data present in the list

# assign list
l = [1, 2.0, 'have', 'a', 'saurabh sir,', 'day']
 
# assign string
s = 'saurabh sir.' 
 
# check if string is present in the list
if s in l:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')

# OUTPUT
# saurabh sir is present in the list

# (Q.9) Write a python script to use NOT IN operator to display the data not present in list

#not in operator working
 
list1= [1,2,3,4,5]
string1= "My name is AskPython"
tuple1=(11,22,33,44)
 
print(5 not in list1) #False
print("is" not in string1) #False
print(88 not in tuple1) #True

''' (Q.10) Write a python script to use IS operator to display if both variables are the same
object or not?'''


# Python program to demonstrate working of 
# "is"
  
# Two different objects having same values
x1 = [10, 20, 30]
x2 = [10, 20, 30]
  
# We get "No" here
if  x1 is x2:
    print("Yes")
else:
    print("No")
  
# It creates another reference x3 to same list.
x3 = x1
  
# So we get "Yes" here
if  x1 is x3:
    print("Yes")
else:
    print("No")
  
# "==" would also produce yes anyway
if  x1 == x3:
    print("Yes")
else:
    print("No")




