import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'cc2e_codes/project_2/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and hight temps from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperaturs.
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, c='red')

# Format plot.
ax.set_title("Daily high temps, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
