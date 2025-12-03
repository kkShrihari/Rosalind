#Lists in Python
#To store a set of data
#start with square racker
#have have  heterogenous data in one list, accespts any datatype 
#Eg : list1 = [1,2,3,4,5,6]
#Its mutable

list2 = [1,2,3.4,"Hi"]

#Empty list
list1 = []

#type of list
height_list = [170,170,156,166,167,190,181,180]
print(type(height_list))


#List indexing (forward and backward)
print(height_list[0])
print(height_list[-1])

#list addition
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1+lst2
print(lst3)


#List replication
lst4 = lst3*2
print(lst4)

#List functions
list1 = [0,1,2,3,4,5,6,7,8,9]

#length of list
print(len(list1))

#element insert
list1.append(10)
print(list1)

#Extend
lst1 = ["hi","hello","Bye"]
lst2 = [1,2,3]
lst1.extend(lst2) #same as lst1+lst2
print(lst1)

#Insert in between 
lst1 = [0,1,2,3,5]
lst1.insert(-1,4) #pos,value
print(lst1)


#Nested list 
lst1 = [1,2,3,[1,2,3]]
print(lst1[3])

#clear everything
lst1 =[1,2,3,5]
lst1.clear()
print(lst1)

#count
lst1 = [1,2,2,2,2,2,3,4,5]
print(lst1.count(2))

#Index of element #look only the 1st occurence
print(lst1.index(2))

#find min and max element

lst1 =[1,2,3,4,5,6,7,8,9]
print(max(lst1))
print(min(lst1))

#List sorting
lst1 = [2,5,4,3,1,5,7,8,9]
lst1.sort()
print(lst1)

#for reverse sort
lst1 = [2,5,4,3,1,5,7,8,9]
lst1.sort(reverse=1)
print(lst1)

#sum of list
lst1 = [2,5,4,3,1,5,7,8,9]
print(sum(lst1))


#Mutability (it is)
lst1 = [2,5,4,3,1,5,7,8,9]
lst1[0] = 500
print(lst1)

#pop of
lst1 = [2,5,4,3,1,5,7,8,9]
lst1.pop() #last value by default
print(lst1)

lst1 = [2,5,4,3,1,5,7,8,9]
lst1.pop(2)
print(lst1)

#remove
lst1 = [1,2,3,4,5,60] #only the 1st occurence
lst1.remove(60)
print(lst1)

#Nested list
lst1 = [[1,2,3],[4,5,6]]
print(lst1[0][0])



######################## Tuples ####################################
#immutable
#one of the 4 built in datatypes
#ordered, allow duplicates and unchangeable
#use round brackets

#type of datatype
tup1 = (1,2,3,4,5,6,7,8,9)
print(type(tup1))


#indexing
print(tup1[0])
print(tup1[-1])

#can update value
#tup1[0] = 100 #wrong


#Tuple methods
#length
print(len(tup1))

#min and max
print(min(tup1))
print(max(tup1))

#counting
print(tup1.count(7))

#sort not supported coz immutable

#check element index
#print(tup1.index(61)) #value error value not found
print(tup1.index(1))


#list to tuple
lst1 = list(tup1)
print(lst1)

#tuple to list
tup2 = tuple(lst1)
print(tup2)

#single char in tuple alone little diff
tup3 = (3)
print(type(tup3))  #class type int
tup3 = (3,)
print(type(tup3))

#one diff example (reassign)
fruits = ("apple", "banana")
print(fruits)

fruits += ("grapes",)
print(fruits)



################# Traversal #############################
fruits = ("apple","banana","Kiwi")

for i in range(len(fruits)):
    print(fruits[i],end=' ')
    

print()
for i in fruits:
    print(i)


####### Slicing
#Applicable for string, list, tuple
string1 = "apple"
print(string1[0:3])  # 0,1,2
print(string1[0:5:2])
print(string1[5:0:-1])


fruits = ("apple","banana","Kiwi")
print(fruits[0:2])  #if goes out of index no error thrown [0:20]; [20:50]->empty tuple


fruits = ["apple","banana","Kiwi"]
print(fruits[0:2])



numbers = [2,5,1,8,4]
print(numbers[1:4]) 

numbers[2:4] = [3,7]
print(numbers)



########################### Dictionary #####################################
#no duplicates, cant sort, non-ordered
#one key can only be used once
map = {1:"one",2:"two",3:"three",4:"four",5:"five"}
print(map)
print(type(map))

#elements access  / no indexing here
print(map[1], map[2])
#print(map[10])   #Key error


#what can be key, what can be value
#key can only be immutable datatype
map1 = {("apple"):1,2:"two","three":3,4:[1,2,3,4]}
print(map1)


#the get function
map1 = {("apple"):1,2:"two","three":3,4:[1,2,3,4]}
print(map1.get(2))
print(len(map1))


#isolate keys alone  / isolate values alone
map1 = {("apple"):1,2:"two","three":3,4:[1,2,3,4]}
print(map.keys())
print(map.values())

#want key-value pairs but in list format
print(map1.items())

#insert new element
map1 = {("apple"):1,2:"two","three":3,4:[1,2,3,4]}
map1[5] = "dragon"
print(map1)

#remove
map1.pop(5)
print(map1)

#clear
map1.clear()
print(map1)

#dict()
map2 = dict() # empty dictioanry


map2 = {5: {'P': {5: "p"}, 6:"Q"}, 7: "R", 'Q': "S", "S": 'T'}
print(map2[map2[map2[5][6]]] )
#prints answer as T


######################## SET ##################################
#unordered but sorted and cant use indexing
#no duplicates

set1 = {4,1,2,3}
print(set1)
print(type(set1))

#add element  #True and 1 considered as 1
set1.add(67)
print(set1)

#remove
set1.remove(67)
print(set1)

#clear all
set1.clear()
print(set1)

#list to set
lst = [1,2,3,4,5]
set2 = set(lst)
print(set2)

#union, intersection etc
set1 = {0,1,2,3,4}
set2 = {5,6,7,8,9,1}

print(set1.union(set2))
print(set1.intersection(set2))

set1 = {2,3,4}
set2 = {1,4,5}
print(set1.difference(set2))

#looping a set
for i in set1:
    print(i)

#check the element present or not
#membership operator
print(1 in set1)
print(1 in set2)

#example sum
set1 = {1,2,3,4}
set2 = {4,5}
set3 = {2,3,4,5,7,8}

print(set1.union(set2).intersection(set3))
#set1.union(set2) ----> {1,2,3,4,5}
#{1,2,3,4,5}.intersection(set3)  ----> {2,3,4,5}



#################### List comprehension ####################

arr = [1,2,3,4,5,6]
odd_list = []

for i in arr:
    if (i % 2 == 1):
        odd_list.append(i)
print(odd_list)

#instead
arr = [1,2,3,4,5,6]
odd_list = [i       for i in arr       if i%2==1]
print(odd_list)

arr = [1,2,3,4,5,6]
div5_list = [i       for i in arr       if i%5==0]
print(div5_list)

arr = [1,2,3,4,5,6]
even_list = [i       for i in arr       if i%2==0]
print(even_list)


#more examples
lst =[]
for i in range(1,101):
    lst.append(i)
print(lst)

#instead

lst = [i for i in range(1,101) ]
print(lst)