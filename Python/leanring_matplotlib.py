
import matplotlib.pyplot as plt
import numpy as np
# x= np.array([2023,2024,2025,2026,2027])
# y1= np.array([10,20,37,20,10])
# y2= np.array([27,34,43,52,30])
# plt.title("class size", fontsize = 20, 
#                         color = "blue",
#                         fontweight = "bold",
#                         fontfamily = "serif")
# plt.xlabel("year", fontsize = 15,
#                         color = "red",
#                         fontweight = "bold",
#                         fontfamily = "serif")
# plt.ylabel("number of students", fontsize = 15,
#                         color = "red",
#                         fontweight = "bold",
#                         fontfamily = "serif")

# plt.plot(x,y1, marker= "."
#             ,markersize = "10"
#             ,markerfacecolor = "red"
#             ,markeredgecolor = "blue"
#             ,markeredgewidth = "2"
#             ,linestyle = "solid")
# plt.plot(x,y2, marker= "."
#             ,markersize = "10"
#             ,markerfacecolor = "green"
#             ,markeredgecolor = "black"
#             ,markeredgewidth = "2"
#             ,linestyle = "solid")

# plt.xticks(x)
# plt.tick_params(axis = "x", labelsize = 12, color = "red")
# plt.show()



#grid() = helps to add gridlines to the plot, which can make it easier to read and interpret the data.

# a = np.array([1,2,3,4,5])
# b = np.array([10,20,37,20,10])

# plt.plot(
#     a, b,
#     marker=".",
#     markersize=10,
#     markerfacecolor="red"
# )

# plt.grid(axis="y", color="blue", linestyle="--", linewidth=0.5)

# plt.show()


#barcharts = used to represent categorical data with rectangular bars, where the length of each bar is proportional to the value it represents. They are commonly used to compare different categories or groups of data.

# categories = np.array(["Grains","Fruits","Vegetables","Dairy","Meat"])
# values = np.array([30,20,25,15,10])

# plt.bar(categories, values, color=["blue","orange","green","red","purple"])
# plt.title("Food Consumption", fontsize=20, color="black", fontweight="bold")
# plt.xlabel("Food Categories", fontsize=15, color="black", fontweight="bold")
# plt.ylabel("Percentage of Consumption", fontsize=15, color="black", fontweight="bold")
# plt.show()

#pie charts = used to represent data as a circular graph, where the circle is divided into sectors that represent the proportion of each category in the data. They are commonly used to show the relative sizes of different categories or groups of data.

# categories = np.array(["Freshman","Sophomore","Junior","Senior"])
# values = np.array([25,30,20,25])

# plt.pie(values, labels=categories, autopct="%1.1f%%", colors=["blue","orange","green","red"],explode=[0.1,0,0,0])
# plt.title("Yearly Distribution", fontsize=20, color="black", fontweight="bold")
# plt.show()


#scatter plots = used to represent the relationship between two variables, where each point on the plot represents a pair of values for the two variables. They are commonly used to identify patterns or trends in the data, such as correlations or clusters.

# x1= np.array([0,1,1,2,4,4,2,4,4,6,8,8,10])
# y1= np.array([55,62,60,75,90,20,35,46,92,24,35,45,40])
# x2= np.array([0,1,1,2,4,4,2,4,4,6,8,8,10])
# y2= np.array([50,60,65,70,85,25,30,40,90,30,40,50,45])
# plt.scatter(x1,y1, color="blue", alpha=0.5, s=100, edgecolor="black", label="Class A")
# plt.scatter(x2,y2, color="red", alpha=0.5, s=100, edgecolor="black", label="Class B")
# plt.title("Study Hours vs Exam Scores", fontsize=20, color="black", fontweight="bold")
# plt.xlabel("Study Hours", fontsize=15, color="black", fontweight="bold")
# plt.ylabel("Exam Scores", fontsize=15, color="black", fontweight="bold")
# plt.legend()
# plt.show()

#histograms = used to represent the distribution of a single variable, where the data is divided into bins or intervals, and the frequency or count of data points in each bin is represented by the height of a bar. They are commonly used to show the shape of the data distribution, such as whether it is skewed or symmetric.

# scores=np.random.normal(loc=75, scale=10, size=100)
# scores=np.clip(scores, 0, 100) # this will limit the values in the scores array to be between 0 and 100, which is a common range for exam scores.
# plt.hist(scores, bins=10, color="blue", edgecolor="black")
# plt.title("Distribution of Exam Scores", fontsize=20, color="black", fontweight="bold")
# plt.xlabel("Exam Scores", fontsize=15, color="black", fontweight="bold")
# plt.ylabel("Frequency", fontsize=15, color="black", fontweight="bold")
# plt.show()

#bins = the intervals or ranges into which the data is divided in a histogram. The number of bins can be specified by the user, and it can affect the appearance of the histogram and the interpretation of the data distribution. Choosing an appropriate number of bins is important to accurately represent the underlying distribution of the data.
#scale = the standard deviation of the normal distribution from which the exam scores are generated. It controls the spread or variability of the scores around the mean (loc). A larger scale value will result in a wider distribution of scores, while a smaller scale value will result in a narrower distribution. In this case, a scale of 10 means that most of the scores will fall within 10 points of the mean score of 75.

#subplots = used to create multiple plots in a single figure, allowing for easy comparison and visualization of different datasets or variables. They are commonly used to show the relationship between multiple variables or to compare different groups of data.

#figure = the entire canvas
#ax = A single plot 

# print(plt.subplots(2,2)) 
# # this will create a 2x2 grid of subplots and return a tuple containing the figure and an array of axes objects. The figure object represents the entire canvas, while the axes objects represent each individual plot within the grid. The output will show the figure and the array of axes objects, which can be used to customize each subplot as needed.
x = np.array([1,2,3,4,5])

figure, axes = plt.subplots(2,2)

axes[0,0].plot(x, x*2, color="blue")
axes[0,0].set_title("Linear")

axes[0,1].bar(x, x**2, color="red")
axes[0,1].set_title("Quadratic")

axes[1,0].hist(x**3, color="green")
axes[1,0].set_title("Cubic")

axes[1,1].scatter(x**4, x**5, color="purple")
axes[1,1].set_title("Quartic")

plt.tight_layout()

plt.show()