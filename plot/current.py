import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

fig, (ax1, ax2) = plt.subplots(2, figsize=(50, 4))
plt.subplots_adjust(hspace = 0.4)
#fig.suptitle('Vertically stacked subplots')

x1 = []
y1 = []

x2 = []
y2 = []

with open('C2Trace00005.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append((float(row[0]) + 10.0) / 2.0)
        y1.append((float(row[1]) / 2.5) * 1000)

with open('C2Trace00004.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append((float(row[0]) + 10.0) / 2.0)
        y2.append((float(row[1]) / 2.5) * 1000)

ax1.set_title('switch on and connect to cellular network')
ax1.set_xlim(0, 10)
ax1.set_xticks(np.arange(0, 11, 1))
ax1.set_ylim(0, 40)
ax1.set_ylabel('Current (mA)')
#ax1.set_xlabel('Time (s)')
# Change major ticks
ax1.xaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_major_locator(MultipleLocator(10))
ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.grid(which='major', color='#CCCCCC', linestyle='--')
ax1.grid(which='minor', color='#CCCCCC', linestyle=':')
ax1.set_axisbelow(True);


ax2.set_title('receive command message and perform an attack')
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(0, 11, 1))
ax2.set_ylim(0, 40)
ax2.set_ylabel('Current (mA)')
ax2.set_xlabel('Time (s)')
# Change major ticks
ax2.xaxis.set_major_locator(MultipleLocator(1))
ax2.yaxis.set_major_locator(MultipleLocator(10))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.grid(which='major', color='#CCCCCC', linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')
ax2.set_axisbelow(True);

ax1.plot(x1,y1, linewidth=0.5, color='orange')
ax2.plot(x2,y2, linewidth=0.5, color='orange')

plt.show()
