import matplotlib.pyplot as plt # Importing the matplotlib library for plotting

#Lets plot a simple line graph of hours vs. marks scored
hours = [1, 2, 3, 4, 5] # Hours studied
marks = [10, 20, 30, 40, 50] # Marks scored

#Plotting

plt.scatter(hours, marks, color='blue', label='Marks vs Hours') # Scatter plot
plt.legend() # Show legend
plt.xlabel('Hours Studied') # X-axis label
plt.ylabel('Marks Scored') # Y-axis label
plt.title('Study Hours vs Marks Scored') # Title of the graph
plt.show()   # Display the plot window
