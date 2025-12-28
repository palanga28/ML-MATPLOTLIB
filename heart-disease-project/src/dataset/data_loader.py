import pandas as pd
import os

def load_data():
    data_path = os.path.join("datasets", "raw_data", "heart.csv")

    columns = [
        "age", "sex", "cp", "trestbps", "chol",
        "fbs", "restecg", "thalach", "exang",
        "oldpeak", "slope", "ca", "thal", "target"
    ]

    df = pd.read_csv(
        data_path,
        header=None,
        names=columns,
        na_values="?"
    )

    return df


if __name__ == "__main__":
    df = load_data()

    print("Aperçu des données :")
    print(df.head())

    print("\nInfos générales :")
    print(df.info())

    print("\nValeurs manquantes :")
    print(df.isnull().sum())
