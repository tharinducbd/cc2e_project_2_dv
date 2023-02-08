import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using a built-in style
plt.style.use('seaborn-v0_8')

figure, axes = plt.subplots()
axes.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
axes.set_title("Square Numbers", fontsize=24)
axes.set_xlabel("Value", fontsize=14)
axes.set_ylabel("Squre of Value", fontsize=14)

# Set size of tick labels.
axes.tick_params(axis='both', labelsize=10)

plt.show()
