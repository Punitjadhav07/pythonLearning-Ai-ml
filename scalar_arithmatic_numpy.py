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



