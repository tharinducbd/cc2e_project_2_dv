import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick lables.
ax.tick_params(axis='both', which='major', labelsize=10)

# Set the range for each axis.
ax.axis([0,1100, 0, 1100000])

plt.show()
