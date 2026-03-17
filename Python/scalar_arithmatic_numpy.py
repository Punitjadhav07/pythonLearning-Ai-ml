import numpy as np


#scalar arithmatic

array = np.array([1,2,3,4,5])
print(array + 2 ) # this will perform element-wise addition, resulting in [3,4,5,6,7]
print(array - 2) # this will perform element-wise subtraction, resulting in [-1,0,1,2,3]
print(array * 2) # this will perform element-wise multiplication, resulting in [2,4,6,8,10]
print(array / 2) # this will perform element-wise division, resulting in [0.5,1.0,1.5,2.0,2.5]
print(array ** 2) # this will perform element-wise exponentiation, resulting in [1,4,9,16,25]

# vectorised maths functons
array1 = np.array([1.02,2.44,3.34,4.029,5.44])
print(np.sqrt(array1)) # this will perform element-wise square root
print(np.round(array1)) # this will perform element-wise rounding to the nearest integer
print(np.floor(array1)) # this will perform element-wise floor, which rounds down to the nearest integer
print(np.ceil(array1)) # this will perform element-wise ceiling, which rounds up to the nearest integer


# excercise

radii= np.array([1,2,3])
print(np.pi*radii**2)


#element-wise arrithmatic

new_array1 = np.array([1,2,3,4,5])
new_array2 = np.array([6,7,8,9,10])
print(new_array1 + new_array2) # this will perform element-wise addition, resulting in [7,9,11,13,15]
print(new_array1 - new_array2) # this will perform element-wise subtraction, resulting in [-5,-5,-5,-5,-5]
print(new_array1 * new_array2) # this will perform element-wise multiplication, resulting in    [6,14,24,36,50]
print(new_array1 / new_array2) # this will perform element-wise division, resulting in [0.16666667,0.28571429,0.375,0.44444444,0.5]
print(new_array1 ** new_array2) # this will perform element-wise exponentiation, resulting in [1,128,6561,262144,9765625]


#comparring operations

compare_array1 = np.array([100,29,38,44,59])
compare_array2 = np.array([50,29,40,44,60])
print(compare_array1 == 100 ) # this will perform element-wise comparison, resulting in [True,False,False,False,False]
print(compare_array1 > 100) # this will perform element-wise comparison, resulting in [False,False,False,False,False]
print(compare_array1 < 100) # this will perform element-wise comparison, resulting in [True,True,True,True,True]
print(compare_array1 == compare_array2) # this will perform element-wise comparison, resulting in [False,True,False,True,False] 
print(compare_array1 > compare_array2) # this will perform element-wise comparison, resulting in [True,False,False,False,False]
print(compare_array1 < compare_array2) # this will perform element-wise comparison, resulting in [False,False,True,False,True]  
compare_array1[compare_array1 < 60] = 0
print(compare_array1)

# broadcasting in numpy

# newarray= np.array([[1,2,3,4,5],[6,7,8,9,10]])
# newarray2 = np.array([[1],[2],[3],[4],[5]])
# print(newarray.shape)
# print(newarray2.shape)
# print(newarray * newarray2) # this will perform element-wise multiplication, resulting in [[1,2,3,4,5],[2,4,6,8,10],[3,6,9,12,15],[4,8,12,16,20],[5,10,15,20,25]] 
#because the shapes of the arrays are compatible for broadcasting. The first array has shape (2,5) and the second array has shape (5,1), so they can be broadcasted 
#to a common shape of (2,5) for the multiplication operation.


arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
arr2 = np.array([[1],[2],[3],[4],[5]])
print(arr1 * arr2) # this will perform element-wise multiplication, resulting in [[1,2,3,4,5],[12,14,16,18,20],[33,36,39,42,45],[64,68,72,76,80],[105,110,115,120,125]]

#aggregate functions = summarize data and return a single value

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])


print(np.sum(arr)) # this will return the sum of all the elements in the array, which is 55
print(np.mean(arr)) # this will return the mean of all the elements in the array, which is 5.5
print(np.median(arr)) # this will return the median of all the elements in the array, which is 5.5
print(np.std(arr)) # this will return the standard deviation of all the elements in the array, which is 2.8722813232690143
print(np.var(arr)) # this will return the variance of all the elements in the array, which is 8.25  
print(np.min(arr)) # this will return the minimum value in the array, which is 1
print(np.max(arr)) # this will return the maximum value in the array, which is 10
print(np.argmin(arr)) # this will return the index of the minimum value in the array, which is 0
print(np.argmax(arr)) # this will return the index of the maximum value in the array, which is 9    

print(np.sum(arr, axis=0)) # this will return the sum of the elements in each column, resulting in [7,9,11,13,15]

#filtering 

ages = np.array([[20,25,39,45,19,16,53],[18,13,15,22,35,40,50]])
teenagers = ages[ages < 20] # this will return a new array containing only the elements of the ages array that are less than 20, resulting in [18]
print(teenagers)
adults = ages[(ages >= 20)&(ages <= 50)] # this will return a new array containing only the elements of the ages array that are greater than or equal to 20 and less than or equal to 50, resulting in [20,25,39,45,19,16,53,18,13,15,22,35,40,50]

#random numbers
random_array = np.random.uniform(low=0, high=1, size=(3,2)) # this will generate a 3x2 array of random numbers between 0 and 1, where low is the lower bound of the random numbers, high is the upper bound of the random numbers, and size is the shape of the output array. The resulting array will contain random values that are uniformly distributed between 0 and 1.
print(random_array) 

print(np.random.seed(42)) # this will set the seed for the random number generator to 42, which means that the same sequence of random numbers will be generated each time the code is run. This is useful for reproducibility and debugging purposes, as it allows you to generate the same random numbers across different runs of the code.

