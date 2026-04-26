import pandas as pd

def load_data():
    dataset = pd.read_csv("data/housing.csv")

    dataset = dataset.drop(columns="ocean_proximity")
    dataset = dataset.dropna()
    

    return dataset


if __name__ == "__main__":
    dataset = load_data()
    print(dataset.head())
    print(dataset.isnull().sum())