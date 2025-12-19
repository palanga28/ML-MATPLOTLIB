import pandas as pd

dossier = pd.read_csv("Maldie_du_coeur/datasets/raw_data/heart_disease.csv", header=None)
print(dossier.head())
print(dossier.describe())
print(dossier.shape)