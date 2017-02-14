from rdkit.Chem import AllChem
from rdkit.Chem import Draw

size = 10 #how many molecules in a row
ms = [
        'CC=C(C(=CC)c1ccc(O)cc1)c1ccc(O)cc1',
        'CC(=O)CC1CC(=O)N(C)C1c1ccc(Cl)cc1',
        'CN1C(=O)CCS(=O)(=O)C1c1ccc(Cl)cc1'
        ]
mol = []
for m in ms: 
	tmp = AllChem.MolFromSmiles(m)	
	if m is None:
		continue
	else:
		mol.append(tmp)
img=Draw.MolsToGridImage(mol,molsPerRow=size,subImgSize=(200,200))
img.save('cdk2_molgrid.o.png')
