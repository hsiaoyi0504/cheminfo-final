from __future__ import print_function
from rdkit import Chem

data = []
line_count = 0
with open('./keras-molecules/data/interpolated.txt') as f:
#with open('./keras-molecules/data/interpolated2.txt') as f:
    for line in f:
        line_count += 1
        temp = line.rstrip('\n')
        temp = temp.split(' ')
        if temp[1] not in data:
            data.append(temp[1])
print(line_count)
print(len(data))
for i in data:
    print(i)
'''
clean_data = []
for i in range(len(data)):
    m = Chem.MolFromSmiles(data[i])
    if m is None:
        #print(data[i],'is invalid')
        continue
    else:
        clean_data.append(data[i])
for i in range(len(clean_data)):
    print('Before:',clean_data[i],'After',Chem.MolToSmiles(Chem.MolFromSmiles(clean_data[i])))
'''
