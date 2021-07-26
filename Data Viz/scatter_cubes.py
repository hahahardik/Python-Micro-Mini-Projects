import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Wistia, s=10)

# Set the chart title and label the axis.
ax.set_title("Cubes", fontsize=22)
ax.set_xlabel("Numbers", fontsize=12)
ax.set_ylabel("Cube of Numbers", fontsize=12)

# Set the size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=12)

# Set the range for each axis.
ax.axis([0, 5100, 0, 130000000000])

# plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()
