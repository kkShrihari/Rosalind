#String Replication
a = "Hi "
print("    ",a*1)
print( "  ",a*1,a*1)
print( " ",a*1,"   ",a*1)
print( "",a*1,"     ",a*1)
print( " ",a*1,"   ",a*1)
print( "  ",a*1,a*1)
print( "    ",a*1)

#string concatenation
str1 = "apple "
str2 = "milk shake"
print(str1+str2)

#combo of both
hash = "#"*20
greeting = "Welcome !!!"
name = "Shrihari"

print(hash, greeting, name , hash, sep = "\n")


'''
#User input
user = input()
print(user+" Welcome")

#A problem / input always get values as string
user = input()
print(type(user))
#here even if i give 71 as input the type is retruned as string



#then how to get it as int for eg
#Type casting
user = int(input())
print(type(user))
#incase i expect float input then i can enter string as input


#Sum1
user = int(input("Enter the value u want the power of :"))
print(user**2)

#Sum2
mark1 = float(input("Enter mark 1:"))
mark2= float(input("Enter mark 2:"))
mark3 = float(input("Enter mark 3:"))
print("The total average marks is: " ,(mark1+mark2+mark3)/3)

#Sum3
#try a^3 + 2bc + c^2
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
print("Value of a^3 + 2bc + c^2 is:", ((a**3) + 2*b*c + c**2 ))


no1 = (input("Enter number here:"))
#To get unit digit
print(int(no1[len(no1)-1]))
print(int(no1[-1]))
print(int(no1)%10)

#To get 1oth digit
digit10 = int(no1)//10
print(int(digit10)%10)

#To get 1o0th digit
digit10 = int(no1)//100
print(int(digit10)%10)



#Statements
1st ------> simple statements
2nd ------> compound statements
3rd ------> empty statements (pause)
'''

#already seen example are simpl

#Now --> compound stat (Eg, conditional statements)
i = 17
if (i < 100): 
    print(i)

i = 999

if (i < 100):
    print(i)
else:
    print("i is bigger than 100")

i = 18
m = "18"

if (i == m ):
    print("i and m are equal")
elif (int(i) == int(m)):
    print("i and m are euqal but check datatype") 
else:
    print("i and m are not euqal")



x = 5
y = 10
if (x > y):
    largest = x
else:
    largest = y
print ("The largest number is:", largest)


#Nested if
age = 29
pizza = "like"
workout = "yes"
if (age <= 30):
    if (pizza == "like"):
        print("unhealthy diet/unfit")
    else:
        print("fit and healthy")
else:
    if (workout == "yes"):
        print("workout/fit")
    else:
        print("no workout/unfit")
#Ternary operator
#eg 1
print(("unhealthy diet/unfit" if pizza == "like" else "fit and healthy") if age <=30 else ("workout/fit" if workout == "yes" else "no workout/unfit"))  

#Ternary operator
#eg 2
i = 10
print("yes" if i == 10 else "No")


#small example
age = 25
income = 50000
if age < 18:
    message = "You are too young to work."
elif age >= 18 and age <= 25:
    if income < 30000:
        message = 'You are eligible for a student discount.'
    else:
        message = 'You are eligible for a regular discount.'
else:
    message = 'You are eligible for a regular discount.'
print (message)


#example 2
#odd or even
num = 1
if (num%2 == 0):
    print("its even")
else:
    print("its odd")

#by ternary operator
print("Even" if num%2 ==0 else "Odd")



#Iteration/looping (for and range)
num = 5
for i in range(num): #def value starting is zero till num -1 as last
  num *= 10
  print(i)
print(num)


num = 10
for i in range(1,num): #def value starting is one till num -1 as last
  num *= 10
  print(i)
print(num)


num = 10
for i in range(1,num,2): #def value starting is one till num -1 as last , btw jumb by 2
  num *= 10
  print(i)
print(num)


num = 5
for i in range(100,50,-5): #def value starting is 100 till 50 as last , btw jumb by -5
  num *= 10
  print(i)
print(num)



#while
i = 0
while (i <= 100):
    print("The no is:",i)
    i +=1   #dont use i++ or ++i its only in c++

#pass statement
if 5==5:
    pass
#skip it for now

#jump statement
#Break and continue
#mostly used with loops

for i in range(1,11):
    if (i == 5):
        continue
    if (i == 7):
        break
    print(i)


i = 10
while(True):
   i *=10
   if (i == 10000000000000000):
       break
   print(i)



# for/while with else

for i in range(1,11):
    print(i)
    if (i == 3):
        continue
else:
    print("printing done")


i =10
while (i >= 0):
    print(i)
    i -= 1
    if (i == 1):
        continue
else:
    print("Succesfully completed")


#Nested loops
n = 4
for j in range(n+1):
    for i in range(1, j+1):
        print(i,end =' ')
    print()




n = 30
for  i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end =' ')
    print()