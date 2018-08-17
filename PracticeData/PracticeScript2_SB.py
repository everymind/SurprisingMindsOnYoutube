import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

x, y = np.loadtxt('gazeone.txt', delimiter=',', unpack=True)
plt.scatter(x,y, label='Trial1')
x, y = np.loadtxt('gazetwo.txt', delimiter=',', unpack=True,)
plt.scatter(x,y, color='green', label='Trial2')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Position of Gaze On Screen')

plt.legend()
plt.savefig("GraphTwoSB.png")
plt.show()
