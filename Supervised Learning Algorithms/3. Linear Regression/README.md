# Linear Regression

This module implements **Linear Regression from first principles**, including:

- Manual derivation of the prediction function  
- Closed-form solution using the **Normal Equation**  
- A full **Gradient Descent** implementation  
- Data preprocessing, feature scaling, and visualization  
- Evaluation of regression performance using standard metrics  
- Interpretation of learned coefficients  

The project uses a real-world dataset of **top songs** to explore how acoustic features relate to song popularity.

---

## What Is Linear Regression?

Linear Regression models the relationship between a set of input features and a continuous output variable using the function:

\[
\hat{y} = w^\top x + b
\]

Where:  
- **x** — feature vector  
- **w** — learned weights  
- **b** — bias  
- **ŷ** — predicted value  

The goal is to find parameters \( w, b \) that minimize the **Mean Squared Error (MSE)** between predictions and true values.

Linear Regression is simple and interpretable, but its performance declines when relationships are nonlinear or data is noisy.

---

## Project Overview

This project implements Linear Regression in two complementary ways:

### **1. Gradient Descent (Manual Implementation)**  
- Random weight initialization  
- Manual gradient computation  
- Iterative optimization  
- Loss curve visualization  
- Fully vectorized NumPy operations  

### **2. Normal Equation (Closed-Form Solution)**  

\[
\theta = (X^\top X)^{-1} X^\top y
\]

This method solves for optimal weights analytically and provides a benchmark for verifying gradient descent results.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `Linear_Regression.ipynb` | Full explanation, implementation, and evaluation. |
| `spotiml/linear_regression.py` | Custom Linear Regression class (GD + closed form). |
| `data/topsongs.csv` | Dataset used for training and evaluation. |

---

## Dataset Description

The project uses a dataset of **2,000 songs**, each containing:

- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- tempo  
- popularity (target)

Key summary statistics:

- **Mean popularity:** 59.87  
- **Std dev:** 21.34  
- **Only semi-strong correlation:** *energy ↔ loudness*  

Because audio features do not strongly correlate with popularity, linear regression faces structural limitations.

---

## Algorithm Summary

### **Prediction Function**
\[
\hat{y} = X w
\]

### **Gradient Descent Update Rule**
\[
w \leftarrow w - \alpha \cdot \frac{2}{n} X^\top(\hat{y} - y)
\]

### **Mean Squared Error (MSE)**

\[
MSE = \frac{1}{n} \sum_{i=1}^{n}(\hat{y}_i - y_i)^2
\]

---

## Evaluation Metrics

This model is evaluated using:

- **Mean Squared Error (MSE)**  
- **Mean Absolute Error (MAE)**  
- **R² Score**  
- Side-by-side predicted vs actual scatter plots  
- Coefficient analysis  

---

## Results Summary

Using the top songs dataset:

| Metric | Value |
|--------|--------|
| **MSE** | 475.047 |
| **MAE** | 14.964 |
| **R² Score** | 0.008 |

### Interpretation

- The model explains **less than 1% of the variance** in popularity.
- Predictions collapse toward the dataset mean.
- Linear regression is not suitable for predicting song popularity because the target variable is highly noisy and nonlinear.

---

## Learned Weights (Insights)

The learned coefficients reveal:

| Feature | Weight | Interpretation |
|---------|--------|----------------|
| **loudness** | +1.277 | Louder tracks slightly trend more popular. |
| **energy** | −1.131 | Negative due to multicollinearity with loudness. |
| **instrumentalness** | −0.702 | Instrumental songs predicted to be less popular. |
| **acousticness** | +0.458 | Mild positive association. |
| **tempo** | +0.434 | Higher tempo slightly increases predicted popularity. |

While some directional trends make intuitive sense, correlations are too weak for effective prediction.

---

## Limitations of Linear Regression

- Assumes strictly **linear** relationships  
- Cannot model feature interactions or nonlinear patterns  
- Highly sensitive to **multicollinearity** (e.g., energy vs. loudness)  
- Regression collapses toward mean when variance is high  
- Performs poorly when target behavior emerges from social/market dynamics  

---

## Why Popularity Isn’t Linearly Predictable

Song popularity is influenced by:

- Virality and cultural trends  
- Playlist placements (Spotify algorithm)  
- Label investment and marketing  
- Artist fame and social context  
- Release timing and external events  

These external drivers dominate acoustic features.

---

## Conclusion

This Linear Regression implementation:

- Demonstrates gradient descent from first principles  
- Implements the mathematically optimal closed-form solution  
- Provides full visualization and error evaluation  
- Highlights the limitations of linear models in complex cultural prediction tasks  

Though performance is low, the model serves as a **baseline** for comparing more advanced nonlinear algorithms such as decision trees, neural networks, and ensemble methods.

---
