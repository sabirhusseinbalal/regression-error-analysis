import numpy as np
import pandas as pd
from load_data import load_data
from preprocessing import preprocess_data
from train import train_models
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    dataset = load_data()

    x, y = preprocess_data(dataset)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42
    )

    models = train_models(x_train, y_train)

    for name, model in models.items():

        # Predictions
        y_train_pred = model.predict(x_train)
        y_test_pred = model.predict(x_test)

        train_residuals = y_train - y_train_pred
        test_residuals = y_test - y_test_pred

        plt.figure(figsize=(5,4))
        sns.scatterplot(x=y_test_pred, y=test_residuals)
        plt.axhline(0, color='red')
        plt.xlabel("Predicted Values")
        plt.ylabel("Residuals (Error)")
        plt.title(f"Residual Plot ({name})")
        plt.show()

        train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

        print(f"{name}")
        print(f"Train RMSE: {train_rmse}")
        print(f"Test RMSE: {test_rmse}")
        print("-"*10)




if __name__ == "__main__":
    main()