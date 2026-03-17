# learning numpy 
import numpy as np 

#numpy arrays are faster than lists and they are more efficient in terms of 
#memory usage. numpy is a powerful library for numerical computing in python. 
#it provides a wide range of functions for working with arrays, including mathematical operations, linear algebra, and statistical analysis. 
#numpy is widely used in data science, machine learning, and scientific computing.
# it is also the foundation for many other libraries such as pandas and scikit-learn.
#numpy is developed in c language and it is optimized for performance. 
# it is also easy to use and it has a large community of users and developers who contribute to its development and support. 
# numpy is an essential tool for anyone working with data in python, and it is a great choice for anyone looking to learn more about numerical computing.


my_list = [1,2,3,4,5]
print(my_list)

print (my_list *2) # this will concatenate the list with itself, resulting in [1,2,3,4,5,1,2,3,4,5] but the numpy array will perform element-wise multiplication, resulting in [2,4,6,8,10]

array = np.array([1,2,3,4,5,6])
print(array)
print(type(array))
print(array * 2) # this will perform element-wise multiplication, resulting in [2,4,6,8,10,12]


#multidimensional arrays

myarr= np.array(["A"])
print(myarr.ndim) # this will return the number of dimensions of the array, which is 0 in this case since it is a 1D array with only one element.

newarr = np.array([["A","B","C"],["D","E","F"]])
print(newarr)
print(newarr.ndim) # this will return the number of dimensions of the array, which is 2 in this case since it is a 2D array with two rows and three columns


multi = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                 [["J","K","L"],["M","N","O"],["P","Q","R"]],
                 [["S","T","U"],["V","W","X"],["Y","Z",""]]#because it had y and z there is no third element in the last layer so it will be filled with empty string
                 ])
print(multi)
print(multi.ndim) # this will return the number of dimensions of the array, which is 3 in this case since it is a 3D array with two layers, three rows and three columns.
print(multi.shape) # this will return the shape of the array, which is (3, 3, 3) in this case since it has three layers, three rows and three columns.

#chain indexing
print(multi[0][0][0]) # this will return the first element of the first row of the first layer, which is "A"

#multidimensional indexing
print(multi[0,0,0]) # this will return the first element of the
print(multi[1,1,1]) # this will return the second element of the second row of the second layer, which is "N"
print(multi[0,1,2]) # this will return the third element of the second row of the first layer, which is "C"


#slicing
newarr = np.array([[1,2,3,4,5],
                   [6,7,8,9,10],
                   [11,12,13,14,15],
                   [16,17,18,19,20],
                   [21,22,23,24,25]
                   ])

#array[start:end:step]
print(newarr[0:4:2]) # this will return the elements from the first and third rows and the first, third and fifth columns of the array, resulting in [[1,3,5],[11,13,15]]
print(newarr[::-1]) # this will reverse the order of the rows and columns of the array, resulting in [[25,24,23,22,21],[20,19,18,17,16],[15,14,13,12,11],[10,9,8,7,6],[5,4,3,2,1]]
print(newarr[:,1]) # this will return the second column of the array, resulting in [2,7,12,17,22]





