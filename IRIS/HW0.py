
# coding: utf-8

# In[110]:

attributes = []
labels = []


# In[111]:

for line in open('/Users/GanHong/Desktop/iris.txt'):
    line = line.strip()
    if line != "":
        line = line.split(',')
        attributes.append(line[:-1])
        labels.append(line[-1])
n_samples = len(labels)
n_attributes = len(attributes[0])


# In[112]:

#indexing the label
map = {}
nn = []
for label in labels:
    if label not in nn:
        nn.append(label)
for i,label in enumerate(nn):
    map[label] = i
for i in range(n_samples):
    labels[i] = map[labels[i]]
print (map)


# In[113]:

import numpy
from matplotlib import pyplot as plt
import os


# In[114]:

colorList = ["r","b","g"]
cnt = 1
plt.figure(figsize=(8,6))
plt.subplots_adjust(hspace=.4)
for i in range(n_attributes-1):
    for j in range(i+1, n_attributes):
        xs = numpy.array([x[i] for x in attributes])
        ys = numpy.array([y[j] for y in attributes])
        colors = []
        for label in labels:
            colors.append(colorList[label])
        plt.subplot(2,3,cnt)
        plt.scatter(xs,ys,c=colors)
        cnt += 1
plt.savefig("res.png",dpi=200)
plt.show()


# In[ ]:



