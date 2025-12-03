#Learning Numpy for NNTI

import numpy as np
print(np.__version__)

#using numpy array
num_array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(num_array1)

#creating 2d array
num2d_array = np.array([[1.1,2.1,3.1],["a",5,6]]) # should be same nummbers !!!!
print(num2d_array)

#find type 
print(type(num_array1))
print(type(num2d_array))
#to find dimension
print(num_array1.shape)
print(num2d_array.shape)
#To find no of elements
print(num_array1.size)
print(num2d_array.size)
#To find dimension
print(num_array1.ndim)
print(num2d_array.ndim)
#To find data type
print(num_array1.dtype)
print(num2d_array.dtype)

#-------------------
#order
#int->float->string
#--------------------

#to explicitly use a datatype
num2d_array = np.array([[1.1,2.1,3.1],[4,5,6]], dtype=int) 
print(num2d_array)

#create arrays of zero,one,custom no (def is float)
print(np.zeros([2,4]))
print(np.ones([2,4]))
print(np.full([3,3],10))
#empty/garbade value
print(np.empty([2,3])) #values are garbage ones


#Arithmetic operations of numpy
# +  -  *   / //

num1 = np.array([1,2,3])
num2 = np.array([3,2,1])
no = 3 # internally it changes to [3,3,3]

add_num = num1+num2
sub_num = num1-num2
print(add_num, "\n", sub_num, "\n")
print(num1*num2, "\n")
print(num1 /num2 , "\n")
print(num1 // no, "\n")


# more complex addition
num1 = np.array([1,1,1]) #incase we dont need last no add zero 
num2 = np.array([[1,2,3],[4,5,6]])
print(num1+num2)

#numpy aggregation
#(sum,mean,max,min,etc)
#np.sum(), np.mean(), np.median(), np.min(), np.max()
print("\n")
num1 = np.array([1,2,3,4,5,6])
print(num1.sum())
print(np.mean(num1))


print(np.median(num1))
#whats median
'''
1st sort

odd no
[1,2,3,4,5]
middle no is 3 so median 3

even no
[1,2,3,4,5,6]
middle no 3,4 avg =3.5 
'''

print(num1.min())
print(num1.max())

#standard deviation
'''
num1 = np.array([50,60,70,80,90])
mean = 350/5 =70
x-mean = [-20, -10, 0, +10, +20]
(x-mean)^2= [400, 100, 0, 100, 400]
variance = ( 400+100++0+100+400 ) /5 = 1000/5 = 200
sq.rt = root(variance) = 14.1
'''

import math 
#To find variance
num1 = np.array([1,2,3,4,5])
print(np.var(num1))

#To get standard deviation
print("std.dev is:", np.std(num1))
print(math.sqrt(np.var(num1)))

#sum of array elements cpl vs row wise
array1 = np.array([[1,2,3],[4,5,6]])
print(np.sum(array1,axis=0))
print(np.sum(array1,axis=1))

#print sum of values > 3
print(np.sum(array1[array1>=3]))

#Indexing #boolean indexing #slicing #filtering
num1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(num1[0:5])
#skip numbers
print(num1[0:10:2])
print(num1[::-1]) #reverse order


num2 = np.array([[1,2,3],[4,5,6]])
print(num2[0][1:3])


#slicing (more ways)
array1 = np.array([[1,2,3],[4,5,6]])
print(array1[0:2,0:2])

#relational operator ! using ways
#returns bool result
filter_array = array1 > 3
print(filter_array)

print(array1[filter_array]) #or
print(array1[(array1 > 1) & (array1 < 5)])


'''
reshape - chnage the shape of an array

ravel - flattens a multi D array into 1D array

flatten - same like ravel but does it on a copy not on org

hstack - joins array horizontally

vstack - join arrays vertically

concatenate - concatenate along any axis

.T - does swap og row and col

'''

#All about reshaping
arr = np.array([1,2,3,4,5,6,7,8,9])
print("org array", arr)

reshaped_arr = arr.reshape(3,3)
print(reshaped_arr)

reshaped_arr = np.reshape(arr,(3,3))
print(reshaped_arr)

reshaped_arr[0][2] = 100   #change index value
print(reshaped_arr)

#Using ravel
arr = np.array([[1,2,3,4],[5,6,7,8]])
arr_ravel = np.ravel(arr) 
arr_ravel[0]=99
print(arr_ravel)
print(arr) #if we look here the org array got modified

#to use flatten
arr = np.array([[1,2,3,4],[5,6,7,8]])
flat_arr = arr.flatten()   # not np.flatten
flat_arr[0] = 10

print("Flat array:", flat_arr)
print("Original array:\n", arr)


#hstack and vstack
arr1 = np.array([1,2,3,4])
arr2 = np.array([4,3,2,1])
print(np.hstack([arr1,arr2])) #use double ([])
print(np.vstack((arr1,arr2)))

#Using concatenate
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[4,3],[2,1]])
print(np.concatenate([arr1,arr2], axis=1)) # add horz and place vertical
print(np.concatenate([arr1, arr2], axis=0)) #place vertical arrange vertical

#Transpose
arr = np.array([[1,2],[3,4]])
print(arr.T)
print(arr.T.T) #rev of rev = org

#--------------------------------------------------------------------------------------------------
#Random number generation
'''
Normal, uniform, Binomial distribution
'''

#Random no gen
print(np.random.rand()) #random no between o to 1
print(np.random.rand(5)) # 5 random no btw 0 to 1 as array
print(np.random.randint(10)) #10 not incl, 0 set def if not mentioned
print(np.random.randint(1,10))
print(np.random.randint(1,10,size=5)) 

# for a particular seed always same no
np.random.seed(20)


#Normal distribution (centered around 50)
print(np.random.normal(loc=50, scale=10, size=5))
#loc = mean , sclae = std.dev , size = no of output
#loc -> here most no will be around 50
#scale = 10 -> a few units will be 10 higher or lower than 50


#Uniform distribution
print(np.random.uniform(10,50,5))
#low,high,size -> small possible value, high possible value, no of ele


#Data visualization !!!!!!
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=50, scale=5, size=10)
x = np.arange(len(data))  # x = [0,1,2,...,9]

plt.scatter(x, data)
plt.xlabel("Index")
plt.ylabel("Random Value")
plt.title("Normal Distribution Samples (mean=50, sd=5)")
#plt.show()

'''
Example of mean,median,mode
data = [1,2,2,3,4,7,9]

1) mean = 1+2+2+3+4+7+9/7 = 28/7 = 4

2) median = (sortedlist)
   data = [7,9,1,2,2,3,4]
   sorted_data = [1,2,2,3,4,7,9]
   if odd -> 3
   if even = center values a+b/2

3)mode -> most frequent no
   data = [1,2,2,3,4,7,9]
   here -> 2
'''


#Linear Algebra
'''
Matrix multiplication
Determinant
Matrix inverse
Linear algebra with NumPy (dot, matmul, eigenvalues, solving equations)
'''

# matrix multiplication
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])
print(A.shape,B.shape)

#3 ways of matrix multiplication
c = A @ B
print(c)

#or
#most efficent one
x = np.matmul(A,B)
print(x)

#or

y = np.dot(A,B)
print(y)


#Matrix inverse
'''
Matrix inverse
for eg 8 ----inverse> 1/8
 A^-1
 inverse done only for square matrix 2x2 , 3x3

 for 2x2
[a b / c d]^-1 = 1/ad-bc[d -b / -c a]
determinant = 1/ad-bc and it shoulnd be zero
'''
import numpy as np
from numpy.linalg import inv, det

A = np.array([[1, 2],
              [3, 4]])

# Find inverse
inv_A = inv(A)
print("Inverse:\n", inv_A)

# Find determinant
det_A = det(A)
print("Determinant:", int(round(det_A, 3)))

# Prove A × A⁻¹ = I
print("A × A⁻¹:\n", A @ inv_A)

#Formulas to remember
'''
XA=B
X = BA-1
AA-1 = I
'''

#A samll mini project
B = np.array([118.4,135.2])
A = np.array([[3,3.5],[3.2,3.6]])
#x= BA-1
x1,x2 = np.matmul(B,inv(A))
print("child",int(round(x1)), "\n","adult",int(round(x2)))

#2nd small question
'''
Students mark analysis
----------------------

1. Average by subject and student
2. Highest & lowest per subject
3. Overall class topper
4. Pass count per subject
5. Which subject is difficult?
6. Ranking students
'''

np.random.seed(40)
marks = np.random.randint(1,101,size=(20,5)) #20 student , 5 subject
print(marks)

#Average by subject
avg_sub = np.mean(marks,axis=0)
print(avg_sub)

#Average by student
avg_stu = np.mean(marks,axis=1)
print(avg_stu)

#Highest and lowest per subject
max_mark_subj = np.max(marks,axis=0)
print(max_mark_subj)

min_mark_subj = np.min(marks,axis=0)
print(min_mark_subj)

#Overall class topper
overall_mark = np.sum(marks,axis=1)
class_topper = np.max(overall_mark) #we will get only mx value not student 
class_topper = np.argmax(overall_mark) #returns argument/position 
print(class_topper)

#Pass count per subject(set 40 and above)
pass_mark = marks >= 40
print(pass_mark)
pass_count = np.sum(pass_mark,axis=0) # F =0 and T = 1
print(pass_count)

#which subject is difficuilt
#max fail and avg less
diff_sub = np.argmin(avg_sub)
print(diff_sub)

#Ranking students
rank = np.argsort(-overall_mark)
print(rank)
print(overall_mark[rank[0]])

print(rank[0:5])
print(overall_mark[rank[0:5]])






#question 1
#Task1
np.random.seed(903)

import numpy as np
#To create an 1D array of 12 elements
array_1D = np.arange(7062520,7062532)
#To reshape the 1D array into 3x4 matrix
reshaped_array = array_1D.reshape(3,4)
print(reshaped_array)
#Printing its final shape
print(reshaped_array.shape)

#Task2
submatrix_2x2 = reshaped_array[1:3,1:3]
print(submatrix_2x2)

#Task3
random_1D = np.random.randint(0,100,16)
matrix_4x4 = random_1D.reshape(4,4)
print(matrix_4x4)

above_10 = (matrix_4x4 > 10) 
final_matrix = matrix_4x4[above_10] = -1
print(matrix_4x4)

## 4. Create a 2x4 matrix A and a 4x3 matrix B with any numerical values you choose.
#  Compute and print the matrix product of A and B using the @ operator. 
# Calculate the mean of the values along the columns of 
# the resulting matrix
#  (i.e., the result should be a 1D array with 3 values).

a_1D = np.arange(1,9)
A = a_1D.reshape(2,4)
b_1D = np.random.randint(0,10,12)
B = b_1D.reshape(4,3)
print(A)
print(B)

Matrix_product = A @ B
print(Matrix_product, "\n",Matrix_product.shape)

#To calculate mean
print(np.mean(Matrix_product,axis=0))
