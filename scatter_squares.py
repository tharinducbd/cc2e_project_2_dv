import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick lables.
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()
