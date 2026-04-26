# Regression Error Analysis

## Project Overview
This project focuses on understanding how machine learning models make errors instead of only checking accuracy.

The main goal is to study:
- How models behave on training vs test data
- What residual errors look like
- When a model is underfitting

We are not trying to improve accuracy here.
We are trying to understand model behavior.

---

## Dataset
- Dataset: California Housing Dataset
- Target: median_house_value
- Categorical column removed
- Missing values dropped
- Features scaled using StandardScaler

---

## Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression

---

## Key Concept: Residual

Residual = Actual Value - Predicted Value

It shows how wrong the model is.

---

## What This Project Does

- Train models on training data
- Predict on train and test data
- Calculate residual errors
- Plot residual graphs
- Compare Train vs Test RMSE

---

## Residual Plot

- X-axis: Predicted values
- Y-axis: Residual (error)

### Good model:
- Random scatter of points

### Our result:
- Pattern observed in errors
- Indicates model limitation

---

## Results Summary

- Linear Regression → High error, underfitting
- Ridge Regression → Same behavior
- Lasso Regression → Same behavior

---

## Key Learnings

- Error is not just a number, it has patterns
- Residual plots help understand model problems
- Train vs Test comparison helps detect underfitting
- Linear models struggle with complex data

---

## Conclusion

All models show similar behavior:
- High RMSE
- No major difference between train and test
- Clear underfitting pattern

This proves that simple linear models cannot fully capture complex relationships in this dataset.

---

## Next Step

Feature Engineering (Repo 5)
We will try to improve model performance by transforming features.