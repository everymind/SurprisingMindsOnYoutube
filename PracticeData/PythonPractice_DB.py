
# coding: utf-8

# In[107]:


import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import os;

# print(os.getcwd())
# actualData = pd.read_csv("/Users/oibabalola/pupil_cvs_data.csv")

data = np.genfromtxt('pupil_cvs_data.csv', delimiter=',', skip_header=10, skip_footer=10, names=['c1', 'c2', 'c3', 'c4', 'c5'])
#data = np.genfromtxt('pupil_cvs_data.csv', delimiter=',', skip_header=10, skip_footer=10, names=['Item1.Centroid.X', 'Item1.Centroid.Y', 'Item1.MajorAxisLength', 'Item1.MinorAxisLength', 'Item1.Area'])

#data2 = np.genfromtxt('gaze2.csv', delimiter=',', skip_header=10, skip_footer=10, names=['g1', 'g2'])


x=data['c1']
y=data['c5']

print(x.size)
# Plot the data
plt.scatter(x, y, label='c1 vs c5')
#plt.scatter(data['c1'], data2['g2'], label='c1 vs g2') - crossing data sets

#xAxisData = np.array(data[c1])
#yAxisData = np.array(data[0])

#plt.plot(xAxisData, yAxisData, label='Col1 vs col2')
# Add a legend
# plt.legend()

# Show the plot
# plt.show()

