import csv

import matplotlib.pyplot as plt

filename = 'cc2e_codes/project_2/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = [int(row[5]) for row in reader]

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lows = [int(row[6]) for row in reader]

# Plot the high temperaturs.
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(highs, c='red')
ax.plot(lows, c='yellow')

# Format plot.
ax.set_title("Daily high temps, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
