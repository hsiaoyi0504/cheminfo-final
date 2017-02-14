from __future__ import print_function
from rdkit import Chem
before = [
        'CC=C(C1=CC=C(C=C1)O)C(=CC)C2=CC=C(C=C2)O',
        'CN1C(C2=CC=C(Cl)C=C2)S(=O)(=O)CCC1=O',
        'C[C@](N)(CC1=CC=C(O)C=C1)C(O)=O',
        'CCN1CCCC1CNC(=O)C1=CC(=C(N)C=C1OC)S(=O)(=O)CC'
        ]

for i in range(len(before)):
    m = Chem.MolFromSmiles(before[i])
    if m is None:
       print('Before:',before[i],' is not a valid SMILES')
       continue
    after = Chem.MolToSmiles(m)
    print('Before:',before[i],'After:',after)
