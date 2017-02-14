import h5py
h5f = h5py.File('./keras-molecules/data/encoded.h5', 'r')
for name in h5f:
    print name
print h5f['latent_vectors']
