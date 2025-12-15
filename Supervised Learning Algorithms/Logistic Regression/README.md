# Logistic Regression

This repository contains a full, from-first-principles implementation of **Logistic Regression**, including:

- Manual gradient descent  
- Manually computed sigmoid + binary cross-entropy loss  
- A custom Python class built to mirror scikit-learn’s API style  
- Visualizations of the optimization process  
- Application to a real dataset for binary classification  

The project also includes comparisons to standard tools (e.g., scikit-learn) to validate correctness and performance.

---

## What Is Logistic Regression?

Logistic Regression is a foundational **binary classification** algorithm used across statistics, machine learning, and data science.  
Unlike linear regression, which predicts continuous values, logistic regression predicts a **probability** between 0 and 1:

\[
\hat{y} = \sigma(w^\top x + b)
\]

Where:

- **x** — feature vector  
- **w** — learned weights  
- **b** — bias term  
- \(\sigma(z) = \frac{1}{1 + e^{-z}}\) — the sigmoid function  

The predicted probability is then thresholded (typically at 0.5) to produce a binary class label.

---

## Project Overview

This project implements Logistic Regression in two modes:

### **1. Manual Implementation (Core Contribution of This Repo)**  
- Manually coded forward pass  
- Hand-derived gradients for cross-entropy loss  
- Batch gradient descent  
- Custom stopping criteria (`eta` tolerance, max iterations)  
- Weight tracking + loss tracking  
- Prediction via sigmoid + probabilistic label sampling  

This version exposes the internal mechanics of logistic regression and optimization.

### **2. Comparison with scikit-learn**
Used to benchmark performance and confirm correctness.

---

## Repository Contents

| File | Description |
|------|-------------|
| `Logistic_Regression.ipynb` | Full explanation, implementation, and evaluation. |
| `spotiml/logistic_reg.py` | Source file for the custom logistic regression class. |
| `data/` | Optional datasets used for testing. |

---

## Algorithm Summary

### **Model**
\[
\text{logit}(p) = w^\top x + b
\]

\[
p = \sigma(w^\top x + b)
\]

### **Binary Cross-Entropy Loss**
\[
L = - \left[ y \log(p) + (1 - y)\log(1 - p) \right]
\]

### **Gradient Descent Update**
\[
w \leftarrow w - \gamma \cdot \nabla L
\]

The notebook visualizes:

- Loss curves  
- Weight updates  
- Convergence stability  

---

## Evaluation Metrics

- **Accuracy**  
- **Precision, Recall, F1 Score**  
- **Confusion Matrix**  
- **Loss over iterations**

Visualization libraries (matplotlib, seaborn) help analyze model performance.

---

## Example Application

The model is demonstrated using the **top songs**:

- Converted into a binary classification problem  
- Features standardized  
- Train/test evaluation  
- Achieved near-perfect accuracy, validating the implementation  

---

## Coefficient Interpretation

Each learned weight represents how a **one-unit increase** in a feature affects the **log-odds** of predicting the positive class.

- Positive weight → increases likelihood of class 1  
- Negative weight → decreases likelihood  
- Larger magnitude → stronger effect  

---

## Limitations of Logistic Regression

- Assumes a **linear** decision boundary  
- Cannot model nonlinear patterns without feature engineering  
- Sensitive to imbalance and multicollinearity  
- Requires feature scaling for stable gradient descent  
- May converge slowly without proper tuning  

---

## Conclusion

This project demonstrates logistic regression from the ground up, covering:

- Manual training using gradient descent  
- Loss computation and optimization  
- Model interpretation  
- Performance visualization  

This forms a strong foundation for extensions like:

- Multiclass logistic regression  
- Regularization (L1, L2)  
- Mini-batch or stochastic gradient descent  
- Neural network building blocks  

---
