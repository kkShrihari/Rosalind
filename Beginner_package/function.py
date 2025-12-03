
#Basic function definition
def print_it ():
    print("Hello world!!!")

print_it()
print_it()
print_it()

'''
#user input example
def add ():
    a = int(input())
    b = int(input())
    print("the sum is: ",a+b)

add()



#different types of function
#void and non-void fn
#if returns someting non-void
#not return anything void (eg above example)

def add ():
    a = int(input())
    b = int(input())
    return a+b

sum = add()
print("The sum is: ",sum)
'''


#function parameters
def sub (a,b):
    return a-b

def mul (a,b):
    return a*b

a = 10
b = 5
sub1 = sub(a,b)
mul1 = mul(a,b)
print(sub1,mul1)

#docstring
def sub (a,b):
    '''
    This function does subtraction
    '''
    return a-b


#Arguments vs Parameters
def area_of_rectangle(length, width) :#parameters
  '''
  This function calculates the area of a rectangle.
  '''
  area = length*width
  return area


rectangle_area = area_of_rectangle(5, 3)#arguments
print (rectangle_area)

#Keyword argument
def area_of_rectangle(length, width) :#parameters
  '''
  This function calculates the area of a rectangle.
  '''
  area = length*width
  return area


rectangle_area = area_of_rectangle(width = 5, length= 3)#arguments
print (rectangle_area)



'''
#positional argument
#The function order is used by parameter
#example
area_of_rectangle(length, width)
area_of_rectangle(5, 3)
length = 5 and width = 3
'''


#Default argument
#positional arguments should be followed by default argument (default should be at last)
#this above rule is same in param and arguments

def area_of_rectangle(length =1, width=1) :#parameters
  '''
  This function calculates the area of a rectangle.
  '''
  area = length*width
  return area


rectangle_area = area_of_rectangle()#arguments
print (rectangle_area)


rectangle_area = area_of_rectangle(1)#arguments
print (rectangle_area)

rectangle_area = area_of_rectangle(width = 10)#arguments
print (rectangle_area)



#Scope of a variable
def add():
   a =7
   b =10 #local scope
   print(a+b)

a = 10
b = 10 
print(a+b)
add()

#global scope
def add():
   global a #takes a from outside
   b =1000 #local scope
   print(a+b)

a = 1000
b = 10
print(a+b)
add()

#another example for global
#global keyword can only be used inside a function
x = 10
def change_x ():
   global x
   x = 20

change_x()
print(x)


#pass statement in fucntion
def add():
   pass

#Arbitrary arguments
'''
If you don’t know how many arguments will be passed into your function, you can use *args.
* means collect all extra positional arguments into a tuple.
'''

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Keyword Arguments
#You can send arguments with name = value. The order doesn’t matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil",  child3="Linus", child2="Tobias")

#3. Arbitrary Keyword Arguments – **kwargs
'''
If you don’t know how many named arguments will be passed, use **kwargs.
** means collect all extra keyword arguments into a dictionary.
'''
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")



#4. Positional-Only Arguments – /
'''
If you add / in the function definition, all arguments before / must be passed positionally, not as keywords.
'''
def my_function(x, /):
    print(x)

my_function(3)        # ✅ works
#my_function(x=3)      # ❌ Error

#5. Keyword-Only Arguments – *
'''
If you add *, all arguments after * must be passed as keywords, not positionally.
'''
def my_function(*, x):
    print(x)

my_function(x=3)   # ✅ works
#my_function(3)     # ❌ Error

#6. Combine Positional-Only and Keyword-Only
'''
You can use both / and * in one function.
'''
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)   # ✅ works

#a and b before / and allows only positionala rgument, whereas c an d after * allows only keyword arguments


'''
#Recursion
#calling a function inside its defintion
def add(n):
   print(n)
   return add(n-1)

ans = add(10)
#gor results plus error
'''

#2 things imp base case(final goal state) and recursive case
def sum_of_n(n):
   #Base case   #without base case recursive done inf and cause error
   if (n ==1):
      return 1 
   #Recursice case
   return n + sum_of_n(n-1)


print(sum_of_n(3))


#Factorial with recursion
def factorial(n):
   if n ==0:
      return 1
   else:
       return n*factorial(n-1)

result = factorial(5)
print(result)


'''
#Modules
to import code from one file to another 
Example add.py contain function called adder

now to use it in another file calculator.py
give:

import add # in calculator.py

print(add.adder(5,8))

if we use like:

from add import adder,sub
print(adder(5,8))
print(sub(1,2))

To import all function
from add import *

can we import variables? yes we can
from add import * #helps to import variables also
print(num1) #num1 in add.py

'''

#math
#default module
import math

print(math.sqrt(25))
print(math.pi)


#What is packages
#collection of modules is a package
#folder vs package
#everypackage shoud contain __init__.py
#this is how pythin diff btw package and folder
#inside a package we can keep many modules inside

'''
from Package(package name) import add(module name)
print(add.adder(1,2))

'''




































































































