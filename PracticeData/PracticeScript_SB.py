import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

x, y = np.loadtxt('2018-08-15T15_06_26-pupilproper.txt', delimiter=',', unpack=True)
plt.plot(y,x)

x, y = np.loadtxt('pupilarea2.txt', delimiter=',', unpack=True,)
plt.plot(y,x, color='green')

plt.xlabel('Time')
plt.ylabel('Area of Pupil')
plt.title('Area of Pupil Against Time')


plt.savefig("GraphOneSB.png")

plt.show()

