import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

blue_line = mpatches.Patch(color='blue', label='Dataset 1')
orange_line = mpatches.Patch(color='orange', label='Dataset 2')
plt.legend(handles=[blue_line,orange_line])

a, b = np.loadtxt('2018-08-15T15_02_00-gaze.txt', delimiter=',', unpack=True)
Dataset_1= plt.plot(a,b)

c, d = np.loadtxt('2018-08-15T15_06_26-gaze.txt', delimiter=',', unpack=True)
Dataset_2= plt.plot(c,d)


plt.xlabel('x position')
plt.ylabel('y position')
plt.title('Position of gaze')


plt.show()
