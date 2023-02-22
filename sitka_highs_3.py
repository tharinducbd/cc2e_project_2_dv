import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'cc2e_codes/project_2/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get high temperatures from the file.
    highs = [int(row[5]) for row in reader]
    print(highs)

# Plot the high temperaturs.
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(highs, c='red')

# Format plot.
ax.set_title("Daily high temps, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
