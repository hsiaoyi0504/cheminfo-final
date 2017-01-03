import sys 
import os
from itertools import islice
import h5py
import numpy as np
from sklearn.model_selection import train_test_split
sys.path.append(os.path.abspath("./keras-molecules"))
from  molecules.utils import load_dataset, one_hot_array, one_hot_index
import pandas as pd


data, charset = load_dataset('./keras-molecules/data/processed_zinc12_250k.h5', split = False)
charset = list(charset)
del data
smiles = []
solubility = []
with open('./data/total.csv') as f:
    for line in islice(f,1,None):
        temp = line.rstrip('\r\n')
        temp = temp.split(',')
        smiles.append(temp[0])
        solubility.append(float(temp[1]))

clean_smiles = []
clean_solubility = []
for i in range(len(smiles)):
    in_charset = True
    if len(smiles[i])>120:
        in_charset = False
    else:
        for char in smiles[i]:
            if char not in charset:
                in_charset = False
                break
    if in_charset:
        clean_smiles.append(smiles[i])
        clean_solubility.append(solubility[i])

h5f = h5py.File('./data/processed_solubility.h5', 'w')

data = pd.DataFrame({'structure':clean_smiles,'logS':clean_solubility})
keys = data['structure'].map(len)<121
data = data[keys]

dt = h5py.special_dtype(vlen=unicode)
h5f.create_dataset('structure',data=data['structure'],dtype=dt)
structures = data['structure'].map(lambda x: list(x.ljust(120)))

one_hot_encoded_fn = lambda row: map(lambda x: one_hot_array(x, len(charset)),one_hot_index(row, charset))

h5f.create_dataset('charset', data = charset)
def chunk_iterator(dataset, chunk_size=100):
    chunk_indices = np.array_split(np.arange(len(dataset)),len(dataset)/chunk_size)
    for chunk_ixs in chunk_indices:
        chunk = dataset[chunk_ixs]
        yield (chunk_ixs, chunk)
    raise StopIteration


def create_chunk_dataset(h5file, dataset_name, dataset, dataset_shape,chunk_size=100, apply_fn=None):
    new_data = h5file.create_dataset(dataset_name, dataset_shape,chunks=tuple([chunk_size]+list(dataset_shape[1:])))
    for (chunk_ixs, chunk) in chunk_iterator(dataset):
        if not apply_fn:
            new_data[chunk_ixs, ...] = chunk
        else:
            new_data[chunk_ixs, ...] = apply_fn(chunk)

test_idx = structures.index
create_chunk_dataset(h5f, 'data_test', test_idx,(len(test_idx), 120, len(charset)),apply_fn=lambda ch: np.array(map(one_hot_encoded_fn,structures[ch])))
h5f.create_dataset('solubility',data=data['logS'][test_idx])
h5f.close()

