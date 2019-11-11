import numpy as np
import matplotlib.pyplot as plt


N = 6 
standard = (12.8, 14.4, 20.0, 28.0, 48.0, 80.8)
overhead = (0, 0, 0, 0, 0, 0)
err = (1.32, 0.49, 1.09, 2.89, 1.41, 10.4) 
ind = np.arange(N)    # the x locations for the groups
width = 0.45       # the width of the bars: can also be len(x) sequence

#p1 = plt.bar(ind, standard, width, color='orange', edgecolor='orange', yerr=err, ecolor='gray')
p1 = plt.bar(ind, standard, width, color='orange', yerr=err, ecolor='gray')

plt.ylabel('SMS Transmission Time (seconds)')
#plt.title('test')
plt.xticks(ind, ('1', '10', '100', '200', '400', '800'))
plt.xlabel('SMS Content Length (bytes)')
plt.yticks(np.arange(0, 100, 10))
#plt.gca().set_yticklabels(['{:.00f}%'.format(x*100) for x in plt.gca().get_yticks()])
plt.ylim(0, 95)
#plt.legend((p1[0], p2[0]), ('w/o mitigation', 'w/ mitigation'))
plt.rc('axes', axisbelow=True)

plt.grid(True, linestyle='--')

ax = plt.axes()
ax.set_axisbelow(True)


plt.tight_layout()
plt.show()
