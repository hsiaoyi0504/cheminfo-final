cd keras-molecules
python download_dataset.py --dataset zinc12 --outfile data/smiles_zinc12_clean_drug_like.h5
cd ..
python canonicalize.py
cd keras-molecules
python preprocess.py data/canonical_smiles_zinc12_clean_drug_like_250k.h5 data/processed_zinc12_250k.h5
python train.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_600.h5 --epochs 225 --batch_size 600
python train.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_300.h5 --epochs 100 --batch_size 300
python sample.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_300.h5 --target encoder >> data/encoded.txt
python sample.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_300.h5 --target encoder --save_h5 data/encoded.h5
cd ..
python clean_solubility_dataset.py
python csv_to_hdf5.py
cd keras_molecules
python sample.py ../data/processed_solubility.h5 data/model_zinc12_250k_batch_300.h5 --target encoder >> ../data/solubility_encoded.txt
python interpolate.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_300.h5 --source "CC=C(C(=CC)c1ccc(O)cc1)c1ccc(O)cc1" --dest "CN1C(=O)CCS(=O)(=O)C1c1ccc(Cl)cc1" >> data/interpolated.txt
cd ..
