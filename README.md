# Regression Error Analysis

This project focuses on understanding how machine learning models make errors instead of only checking accuracy.

The main goal is to study:
- How models behave on training vs test data
- What residual errors look like
- When a model is underfitting

We are not trying to improve accuracy here.
We are trying to understand model behavior.


## Project Goal

To analyze how regression models behave using:
- Same dataset (California Housing Dataset)
- Same features
- Same train/test split

And observe key ML concepts:
- Bias vs Variance
- Underfitting vs Overfitting
- Error patterns in predictions


## Dataset

- California Housing Dataset
- Target variable: `median_house_value`
- Categorical column removed
- Missing values dropped
- Features scaled using StandardScaler


## Models Used

- Linear
- Ridge
- Lasso


## What This Project Does

- Train models on training data
- Predict on training and test data
- Calculate residual errors
- Plot residual graphs
- Compare Train vs Test RMSE

## Results Summary

- Linear Regression → High error, underfitting
- Ridge Regression → Same behavior
- Lasso Regression → Same behavior

## Conclusion

All models show similar behavior:

- High RMSE
- No major difference between train and test
- Clear underfitting pattern

This proves that simple linear models cannot fully capture complex relationships in this dataset.

--- 

## Project Structure

```
regression-error-analysis/
├── data/
│   └── housing.csv
├── src/
│   ├── load_data.py
│   ├── main.py
│   ├── preprocessing.py
│   └── train.py
├── result/
│   └── metrics.txt
├── requirements.txt
└── README.md
```


---
   ```bash
   git clone https://github.com/Sabirhusseinbalal/regression-error-analysis.git
   ```
---

## Machine Learning (Basics)
---
- [***simple-regression-lab***](https://github.com/sabirhusseinbalal/simple-regression-lab)
- [***house-price-prediction-ml***](https://github.com/sabirhusseinbalal/house-price-prediction-ml)
- [***same-data-different-models***](https://github.com/sabirhusseinbalal/same-data-different-models)
- 👉 regression-error-analysis
  
**Watch Full YouTube Playlist:**
[[Machine Learning (Beginner → Advanced)](https://youtube.com/playlist?list=PLBslpEV463BcknHrcoF_OJDyutuE1DneY&si=7PfeO4OSQCqh1wEI)]





