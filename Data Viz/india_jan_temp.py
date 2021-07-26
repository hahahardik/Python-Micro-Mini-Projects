import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = "data/Mean_Temp_IMD_2017.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get years and temperature from this file.
    years, jan, feb, mar, apr = [], [], [], [], []
    for row in reader:
        year = datetime.strptime(row[0], '%Y')
        try:
            temp_jan = float(row[1])
            temp_feb = float(row[2])
            temp_mar = float(row[3])
            temp_apr = float(row[4])
        except ValueError:
            print(f"Missing data for Jan-{year}.")
        else:
            years.append(year)
            jan.append(temp_jan)
            feb.append(temp_feb)
            mar.append(temp_mar)
            apr.append(temp_apr)

# Plot the temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(years, jan)
ax.plot(years, feb)
ax.plot(years, mar)
ax.plot(years, apr)

# Format plot.
title = "India-January Temperatures\n1901-2017"
plt.title(title, fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
