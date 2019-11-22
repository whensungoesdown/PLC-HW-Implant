import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(50, 7))
plt.subplots_adjust(hspace = 0.4)
#fig.suptitle('Vertically stacked subplots')

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

with open('C2Trace00005.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append((float(row[0]) + 10.0) / 2.0)
        y1.append((float(row[1]) / 2.5) * 1000)

with open('C2Trace00008.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append((float(row[0]) + 10.0) / 2.0)
        y2.append((float(row[1]) / 2.5) * 1000 + 3.2)

with open('C1Trace00012.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append((float(row[0]) + 10.0) / 2.0)
        y3.append(float(row[1]))

ax1.set_title('1. Switch on and connect to cellular network')
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


ax2.set_title('2.a Receive command message and send JTAG commands')
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(0, 11, 1))
ax2.set_ylim(0, 40)
ax2.set_ylabel('Current (mA)')
#ax2.set_xlabel('Time (s)')
# Change major ticks
ax2.xaxis.set_major_locator(MultipleLocator(1))
ax2.yaxis.set_major_locator(MultipleLocator(10))
ax2.xaxis.set_minor_locator(AutoMinorLocator(5))
ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
ax2.grid(which='major', color='#CCCCCC', linestyle='--')
ax2.grid(which='minor', color='#CCCCCC', linestyle=':')
ax2.set_axisbelow(True);

ax3.set_title('2.b One PLC pin output "1" due to the JTAG commands')
ax3.set_xlim(0, 10)
ax3.set_xticks(np.arange(0, 11, 1))
ax3.set_ylim(0, 30)
ax3.set_ylabel('Voltage (V)')
ax3.set_xlabel('Time (s)')
# Change major ticks
ax3.xaxis.set_major_locator(MultipleLocator(1))
ax3.yaxis.set_major_locator(MultipleLocator(10))
ax3.xaxis.set_minor_locator(AutoMinorLocator(5))
ax3.yaxis.set_minor_locator(AutoMinorLocator(5))
ax3.grid(which='major', color='#CCCCCC', linestyle='--')
ax3.grid(which='minor', color='#CCCCCC', linestyle=':')
ax3.set_axisbelow(True);

ax1.plot(x1,y1, linewidth=0.5, color='orange')
ax2.plot(x2,y2, linewidth=0.5, color='orange')
ax3.plot(x3,y3, linewidth=0.5, color='red')

plt.show()
