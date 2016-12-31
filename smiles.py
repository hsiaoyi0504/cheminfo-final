from rdkit import Chem
import csv

structures = []
solubility = []
f = open('solubility_all.csv', 'r')  
for row in csv.reader(f):  
    m = Chem.MolFromSmiles(row[0])
    if m is None:
    	continue
    s = Chem.MolToSmiles(m)
    structures.append(s)
    solubility.append(row[1])
f.close()


canonical = list(set(structures))
print len(canonical)
new_solubility = []
for item in canonical:
	new_solubility.append(solubility[structures.index(item)])
zipped = zip(canonical,new_solubility)


f = open('total.csv', 'wb')
for row in zipped:
    for column in row:
        f.write('%s;' % column)
    f.write('\n')
f.close()
