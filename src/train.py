from sklearn.linear_model import LinearRegression, Ridge, Lasso


def train_models(x_train, y_train):

    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.1)
    }

   
    for name, model in models.items():
        model.fit(x_train, y_train)

    return models