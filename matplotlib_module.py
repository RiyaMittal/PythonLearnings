import matplotlib.pyplot as plt
import numpy as np

x3=[1,2,3]
y3=[0.2 , 0.4, 0.6]

plt.plot(x3, y3)
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('First plot using python')
plt.show()

# line 1 points
x1 = [1, 2, 3]
y1 = [2, 4, 1]
# plotting the line 1 points
plt.plot(x1, y1, label="line 1")

# line 2 points
x2 = [1, 2, 3]
y2 = [4, 1, 3]
# plotting the line 2 points
plt.plot(x2, y2, label="line 2")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

# x axis values
x = [1, 2, 3, 4, 5, 6]
# corresponding y axis values
y = [2, 4, 1, 5, 2, 6]

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
plt.ylim(1, 8)
plt.xlim(1, 8)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Some cool customizations!')

# function to show the plot
plt.show()

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]

# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['cyan', 'pink'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
plt.show()


##################HISTOGRAM########


# frequencies
ages = [2, 5, 70, 40, 30, 45, 50, 45, 43, 40, 44,
        60, 7, 13, 57, 18, 90, 77, 32, 21, 20, 40]

# setting the ranges and no. of intervals
range = (0, 100)
bins = 10

# plotting a histogram
plt.hist(ages, bins, range, color='brown',
         histtype='bar', rwidth=0.8)

# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')

# function to show the plot
plt.show()


# scatter plot

# x-axis values
x5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y-axis values
y5 = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]

# plotting points as a scatter plot
plt.scatter(x5, y5, label="stars", color="green",
            marker="*", s=30)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

# function to show the plot
plt.show()

# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
        radius=1.2, autopct='%1.1f%%')

# plotting legend
plt.legend()

# showing the plot
plt.show()