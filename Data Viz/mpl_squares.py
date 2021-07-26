import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.plot(input_values, cubes, linewidth=3)

# Set the chart title and label the axis.
ax.set_title("Graph", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Result", fontsize=14)

# Set the size of tick labels.
ax.tick_params(axis="both", labelsize=14)

plt.show()
