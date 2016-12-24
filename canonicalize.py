from __future__ import print_function
import pandas
import h5py
from rdkit import Chem

def canonicalize(smiles):
    return Chem.MolToSmiles(Chem.MolFromSmiles(smiles))

SMILES_COL_NAME = 'structure'

input_file = 'keras-molecules/data/smiles_zinc12_clean_drug_like.h5'
output_file = 'keras-molecules/data/canonical_smiles_zinc12_clean_drug_like_250k.h5'

data = pandas.read_hdf(input_file, 'table')
data = data.rename(columns={'SMILES':'structure'})
data = data.replace(
    ['CC(=O)Nc1ccc(cc1)S(=O)(=O)N=N=N',
     'COc1ccc(cc1)COC(=O)N=N=N',
     'CCCC[C@@H](C(=O)OC)NC(=O)C=N=N',
     'CCCC[C@H](C(=O)OC)NC(=O)C=N=N',
     'CC1=CC=N(=C(C#N)C#N)C=C1',
     'c1ccc(cc1)NC(=O)C(=N2=CC=CC=C2)C#N',
     'c1ccc(cc1)CC2=CC=N(=C(C#N)C#N)C=C2',
     'c1nc(nn1CCC#N)N=N=N',
     'c1ccc(cc1)C=N2=CC=CC=C2',
     'c1ccc2c(c1)c(=O)c(=N3=CC=CC=C3)c2=O',
     'CCOC(=O)C(=N1=CC=CC=C1)c2nc(=O)cc(s2)c3ccccc3',
     'c1csc2c1-c3cscc3N(=C2)=C(C#N)C#N'],
    ['CC(=O)NC1=CC=C(C=C1)S(=O)(=O)N=[N+]=N',
     'COC1=CC=C(C=C1)COC(=O)N=[N+]=N',
     'CCCC[C@@H](C(=O)OC)NC(=O)C=[N+]=N',
     'CCCC[C@H](C(=O)OC)NC(=O)C=[N+]=N',
     'CC1=CC=[N+](C=C1)C(C#N)C#N',
     'C1=CC=C(C=C1)NC(=O)C(C#N)[N+]2=CC=CC=C2',
     'C1=CC=C(C=C1)CC2=CC=[N+](C=C2)C(C#N)C#N',
     'C1=NC(=NN1CCC#N)N=[N+]=N',
     'C1=CC=C(C=C1)C[N+]2=CC=CC=C2',
     'C1CCC2C(C1)C(=O)C(C2=O)[N+]3=CC=CC=C3',
     'CCOC(=O)C(C1=NC(=O)C=C(S1)C2=CC=CC=C2)[N+]3=CC=CC=C3',
     'C1C2=C(C=CS2)C3=CSC=C3[N+]1=C(C#N)C#N']
)
ratio = float(250000)/len(data)
data = data.sample(frac = ratio)
data[SMILES_COL_NAME] = data[SMILES_COL_NAME].apply(canonicalize)
data.to_hdf(output_file,'table', format = 'table', data_columns = True)
print('Finished canonicalization')
