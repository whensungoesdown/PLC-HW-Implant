import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)


N = 3 
standard = (3.8, 3.8, 3.806)
overhead = (0, 0, 0)
err = (0.5, 0.5, 0.53) 
ind = np.arange(N)    # the x locations for the groups
width = 0.15       # the width of the bars: can also be len(x) sequence

#p1 = plt.bar(ind, standard, width, color='orange', edgecolor='orange', yerr=err, ecolor='gray')
p1 = plt.bar(ind, standard, width, color='#7f6d5f', yerr=err, ecolor='gray')

plt.ylabel('Execution Time (ms)')
#plt.title('test')
plt.xticks(ind, ('Original', 'Backdoor\nStandby', 'Backdoor\nAttack'))
#plt.xlabel('SMS Content Length (bytes)')
plt.yticks(np.arange(0, 5, 0.5))
#plt.gca().set_yticklabels(['{:.00f}%'.format(x*100) for x in plt.gca().get_yticks()])
plt.ylim(0, 5)
#plt.legend((p1[0], p2[0]), ('w/o mitigation', 'w/ mitigation'))
plt.rc('axes', axisbelow=True)

#plt.grid(True, linestyle='--')

ax = plt.axes()
ax.set_axisbelow(True)
#ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.grid(which='major', color='#CCCCCC', linestyle='--')
#ax.grid(which='minor', color='#CCCCCC', linestyle=':')



plt.tight_layout()
plt.show()
