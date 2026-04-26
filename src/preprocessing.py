from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data(dataset):
    x = dataset.iloc[:, :-1]
    y = dataset["median_house_value"]

    cols = x.columns 

    sc = StandardScaler()
    x = sc.fit_transform(x)

    x = pd.DataFrame(x, columns=cols)

    return x, y