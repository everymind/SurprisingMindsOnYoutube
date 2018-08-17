import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;
import os;

# print(os.getcwd())
# actualData = pd.read_csv("/Users/oibabalola/pupil_cvs_data.csv")

data = np.genfromtxt('FinalPupil.csv', delimiter=',', names=['c1', 'c2'])

x=data['c2']
y=data['c1']

print(x.size)
# Plot the data
plt.plot(x, y, label='c2 vs c1')
plt.suptitle('Change in Pupil Location with Time')
plt.xlabel('Time')
plt.ylabel('Pupil Centre')
#plt.scatter(data['c1'], data2['g2'], label='c1 vs g2') - crossing data sets

#xAxisData = np.array(data[c1])
#yAxisData = np.array(data[0])

#plt.plot(xAxisData, yAxisData, label='Col1 vs col2')
# Add a legend
#plt.legend()

# Show the plot
# plt.show()
