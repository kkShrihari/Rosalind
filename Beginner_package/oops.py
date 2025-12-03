#CLASS /OOPS

class car:
    no_of_wheels = 0
    mileage =  0
    no_of_airbags = 0

    def mileage1(self):
        print("The mileage is:", self.mileage)

    def no_of_wheels1(self):
        print("The no_of_wheels is:", self.no_of_wheels)

    def no_of_airbags1(self):
        print("The no_of_wheels is:", self.no_of_airbags)

car1 = car()  #instance of a class #instantiation
print(car1.no_of_wheels)
print(car1.mileage)
print(car1.no_of_airbags)

car1.no_of_wheels = 4
car1.mileage   = 24
car1.no_of_airbags = 2

print(car1.no_of_wheels)
print(car1.mileage)
print(car1.no_of_airbags)

car1.no_of_wheels1()



#Bankk class

class Bank_Account:
    customer_name = ""
    balance =0
    account_number =0

    def customer_details(self):
        print("The customer details are:",'\n', self.customer_name, '\n', self.balance, '\n', self.account_number)
    
    def start(self):
        print("Welcome to Mysparkasee portal")

bank_acc1 = Bank_Account()
bank_acc1.customer_name = "shri"
bank_acc1.balance = 10000000000000000000000000000000000000000000
bank_acc1.account_number = "SK762520"

bank_acc1.start()
bank_acc1.customer_details()
print('\n\n\n\n\n')

#####################################Constructor###################

'''
default constructor syntax
def __init__(self):
  print("HI!")
A destructor is called automatically
  '''

#Bankk class
class Bank_Account:
    def __init__(self,c_name,bal,acc_no):
       print("Welcome")
       self.customer_name = c_name
       self.balance = bal
       self.account_number = acc_no
    
    # def __del__(self):
    #     print("This is a destructor!",self)

    # def __str__(self):
    #     return self.customer_name

    def customer_details(self):
        print("The customer details are:",'\n', self.customer_name, '\n', self.balance, '\n', self.account_number)
    
    def start(self):
        print("Mysparkasee portal")

bank_acc1 = Bank_Account("shri",10000000000000000000000000000000000000,"HX278")
bank_acc1.start()
bank_acc1.customer_details()
#DESTUCTOR




############################ ENCAPSULATION ##################################
#Binding of variables and methods
#a class with attributes and functions
#But it doesnt end there we need to know getters and setters














############### Inheritance ##################
#Multi level inheritance
class Vehicle:  # parent
    no_of_types = 4
    def moveForward(self):
        print("The Vehicle is moving forward")

class Car(Vehicle): # child
    no_of_airbags = 2
    def moveForward(self):
        print("The car is moving forward")

class Maruthi(Car): # child
    cost = 6,00,000
    def moveForward(self):
        print("The Maruthi is moving forward")

Maruthi1 = Maruthi()
print(Maruthi1.no_of_types)   # Output: 4
Maruthi1.moveForward()


#Hierarchial inheritance

class Vehicle:  # parent
    no_of_types = 4
    def moveForward(self):
        print("The Vehicle is moving forward")

class Car(Vehicle): # child
    no_of_airbags = 2
    def moveForward(self):
        print("The car is moving forward")

class Bike(Vehicle): # child
    no_of_gears = 6
    def moveForward(self):
        print("The Bike is moving forward")


KTM = Bike()
print(KTM.no_of_gears)
print(KTM.no_of_types)


#Multiplr inheritance

class Car: # child
    no_of_airbags = 2
    range = 24
    def moveForward(self):
        print("The car is moving forward")

class Bike: # child
    no_of_gears = 6
    range = 30
    def moveForward(self):
        print("The Bike is moving forward")


class Vehicle(Car,Vehicle):  # parent
    no_of_types = 4
    def moveForward(self):
        print("The Vehicle is moving forward")

Vehicle1 = Vehicle()
print(Vehicle1.no_of_airbags)
Vehicle1.moveForward()
print(Vehicle1.range)  #Car range printed coz it was the 1sst i gave (Car,Vehicle)

#Diamond probelm and solving ambiguity
class Car:
    type = "car"

class Toyota(Car):
    type = "toyota"

class Kiya(Car):
    type = "Kiya"

class Sedan(Toyota,Kiya):
    model_type = "Sedan"

S1 = Sedan()
print(S1.type) #prints toyota 1st becoZ of order(Toyota,Kiya)


#############Lets learn args ##############
def sum(a, *args):
    ans =0
    for i in args:
        ans += i
    return a + ans

print(sum(1,2,3,4,5,6,7,8,9))


#############Polymorphism ###########################
#compile time vs runtime
#pythoon- no method overloading coz automatically determines dataype (compile time)

#But we can do runtime overloading (overriding)
class Father:
    def __init__(self):
        print("Father construtor")

    def say_hello(self):
        print("Hello from father")
      
class Child(Father):
    def __init__(self):
        print("Child construtor")
        
    def say_hello(self,name):
        print("Hello from ",name)
    

Child1 = Child()
Child1.say_hello("Lion")

Father1 = Father()
Father1.say_hello()

#################3 Abstraction ############################
#hide unwanted data and display only needed one

  



























































