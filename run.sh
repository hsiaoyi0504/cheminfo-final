cd keras-molecules
python download_dataset.py --dataset zinc12 --outfile data/smiles_zinc12_clean_drug_like.h5
cd ..
python canonicalize.py
cd keras-molecules
python preprocess.py data/canonical_smiles_zinc12_clean_drug_like_250k.h5 data/processed_zinc12_250k.h5
python train.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_600.h5 --epochs 225 --batch_size 600
python train.py data/processed_zinc12_250k.h5 data/model_zinc12_250k_batch_300.h5 --epochs 100 --batch_size 300
