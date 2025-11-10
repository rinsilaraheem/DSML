# from matplotlib import pyplot
# from numpy import array
# fig,ax=pyplot.subplot(1,1)
# a=array([
#     [22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]
# ])
# ax.hist(a,bins=[0,10,20,30,40,50,60,70,80,90,100])
# ax.set_title("Histogram of result")
# ax.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
# ax.set_xlabel("marks")
# ax.set_glabel("no.of student")
# pyplot.show()




from matplotlib import pyplot
from numpy import array

# Create the figure and axis
# fig, ax = pyplot.subplots()

# Data array
# a = array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])

# Create histogram
# ax.hist(a, bins=[0,10,20,30,40,50,60,70,80,90,100])

# Titles and labels
# ax.set_title("Histogram of Result")
# ax.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
# ax.set_xlabel("Marks")
# ax.set_ylabel("No. of Students")

# Show plot
# pyplot.show()


marks=[22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]
bins=[0,10,20,30,40,50,60,70,80,90,100]
pyplot.hist(marks,bins=bins)
pyplot.xlabel("Marks Range")
pyplot.ylabel("Number of student")
pyplot.title("Histogram of student mark")

pyplot.show()