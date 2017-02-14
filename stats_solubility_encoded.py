import numpy as np
import matplotlib.pyplot as pp
data = []
with open('./data/solubility_encoded.txt') as f:
    for line in f:
        temp = line.rstrip('\n')
        temp = temp.split('\t')
        temp = [float(x) for x in temp]
        data.append(temp)
print len(data)
print len(data[0])
data = np.array(data)
pp.plot(np.var(data,axis=0))
pp.savefig('foo.png')
