import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('2018-08-15T15_06_26-pupilproper.txt', delimiter=',', unpack=True)
plt.plot(y,x)

plt.xlabel('Time')
plt.ylabel('Area of Pupil')
plt.title('Area of Pupil Against Time - Data 1')

plt.show()
