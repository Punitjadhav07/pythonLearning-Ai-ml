import pandas as pd

print(pd.__version__)   # this will print the version of pandas that is currently installed in your Python environment.

# The output of the above code will depend on the version of pandas that you have installed. For example, if you have pandas version 1.3.0 installed

#series vs DataFrame 
# A Series is a one-dimensional array-like object that can hold any data type, while a DataFrame is a two-dimensional table-like data structure that consists of rows and columns.

#series = A pandas Series is a one-dimensional array-like object that can hold any data type, such as integers, floats, strings, or even other Python objects. It is similar to a column in a spreadsheet or a database table. Each element in a Series has an associated index, which can be used to access and manipulate the data.

import pandas as pd

data = [100,102,304,706,500]

series = pd.Series(data, index=["a","b","c","d","e"])

print(series) # this will create a pandas Series with the given data and index, and print it to the console.

print(series.loc["c"]) # this will return the value at index "c" in the Series, which is 304.

series.loc["c"] = 400 # this will update the value at index "c" in the Series to 400.
print(series) # this will print the updated Series to the console, showing that the value at index "c" has been changed to 400.


#dataframe = A pandas DataFrame is a two-dimensional table-like data structure that consists of rows and columns. It is similar to a spreadsheet or a SQL table, and it can hold a variety of data types, including integers, floats, strings, and even other Python objects. Each column in a DataFrame has an associated name, and each row has an associated index. DataFrames are commonly used for data manipulation, analysis, and visualization in Python.

data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
         "Age": [25, 30, 35, 40, 45]
 }
df = pd.DataFrame(data , index =["employee1","employee2","employee3","employee4","employee5"])
print(df) # this will create a pandas DataFrame with the given data and index, and
print(df.iloc[2]) # this will return the third row of the DataFrame, which contains the data for "Charlie" and his age of 35.

# adding a new colomun to the DataFrame
df["Salary"] = [50000, 60000, 70000, 80000, 90000]
print(df) # this will add a new column called "Salary" to the DataFrame with the given values, and print the updated DataFrame to the console. The new column will contain the salary information for each employee.        
print("-----------------------------")
#adding a new row to the DataFrame
new_row = {"Name": "Frank", "Age": 50, "Salary": 100000}
df.loc["employee6"] = new_row
print(df) # this will add a new row to the DataFrame with the given data for "Frank", and print the updated DataFrame to the console. The new row will contain the name, age, and salary information for the new employee.

