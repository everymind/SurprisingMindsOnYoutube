import matplotlib.pyplot as plt
import numpy as np

time, pupil_size = np.loadtxt('pupilareadata.csv', delimiter=',', unpack=True)
plt.plot(time,pupil_size, label='Dataset 1')

time2, pupil_size2 = np.loadtxt('pupilareadata2.csv', delimiter=',', unpack=True)
plt.plot(time2,pupil_size2, label='Dataset 2')

plt.xlabel('Course of video')
plt.ylabel('Size of pupil')
plt.title('Changes in the size of the pupil during video')

plt.legend()
plt.show()
