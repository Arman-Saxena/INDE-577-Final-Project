# Random Forest

This repository contains an implementation of a Random Forest classifier applied to the Spotify Hit Prediction dataset.  
this project builds the full pipeline manually:

- Custom Decision Tree implementation (Gini impurity)
- Bootstrapped sampling (bagging)
- Random feature selection per split
- Majority-vote aggregation across trees
- Manual computation of feature importance

The goal of this project is to provide a clear, intuitive walk-through of **how Random Forests work internally**, without relying on external libraries for the modeling itself.

---

## What Is a Random Forest?

A **Random Forest** is an ensemble learning method that builds many decision trees on:

1. **Different bootstrap samples** of the training data  
2. **Different randomly selected subsets** of features  

Each tree "votes," and the forest’s final prediction is based on **majority vote** for classification.

Random Forests reduce the major weaknesses of single decision trees:

- Lower variance  
- Better generalization  
- More stable decision boundaries  
- Less sensitivity to noise  

---

## Methodology Overview

This project implements Random Forests using the following components:

### **1. Custom Decision Tree (Gini-Based)**
Each tree is built using:

- Gini impurity as the splitting criterion  
- Recursive binary splits  
- Random feature subsets (`max_features`)  
- Stopping conditions: max depth, min samples per leaf  

No scikit-learn tree code is used—this is a fully manual implementation.

---

### **2. Bootstrap Aggregation (Bagging)**

For each tree:

- Random sampling **with replacement** creates a bootstrap dataset  
- Each tree sees a slightly different distribution of examples  
- Trees become decorrelated, improving ensemble performance  

Mathematically, from `N` training samples, each tree draws `N` samples with replacement.

---

### **3. Random Feature Subsets**

At each split:

- A small subset of features is chosen (e.g., √d)  
- The tree chooses the best split **only within that subset**  

This adds randomness that prevents all trees from looking identical and dramatically reduces overfitting.

---

### **4. Majority Voting**

Each tree returns a predicted label (0 or 1).  
The forest prediction is:

\[
\hat{y} = 
\begin{cases}
1 & \text{if } \frac{1}{T}\sum_{t=1}^T y^{(t)} \ge 0.5 \\
0 & \text{otherwise}
\end{cases}
\]

This makes the model robust even if some trees are weak or noisy.

---

### **5. Feature Importance (Manual Computation)**

Feature importance is computed by summing each feature’s contribution to impurity reduction:

\[
\text{Importance}(f) = \sum_{splits} \Delta \text{Gini}(f)
\]

This reveals which attributes contribute most to predictive power.

## Algorithm Summary

### **Gini Impurity**
\[
G = 1 - \sum_{k=1}^K p_k^2
\]

### **Information Gain**
\[
IG = G_{parent} - \left( \frac{n_l}{n}G_l + \frac{n_r}{n}G_r \right)
\]

### **Random Forest Workflow**
1. Bootstrap sample  
2. Random feature subset  
3. Build decision tree  
4. Repeat for T trees  
5. Aggregate via majority vote  

---

## Evaluation Metrics

Although this README focuses on methodology rather than specific performance numbers, the project includes:

- Accuracy  
- Confusion Matrix  
- Feature Importances  
- Comparison across trees  

These tools help evaluate how ensemble methods improve stability and generalization over single decision trees.

---

## Why Random Forest for Spotify Data?

The Spotify dataset contains noisy, correlated features such as:

- Danceability  
- Energy  
- Loudness  
- Valence  
- Tempo  

Random Forests are well-suited because they:

- Handle non-linear relationships  
- Manage feature interactions naturally  
- Resist overfitting  
- Provide interpretable feature importance rankings  

---

## Conclusion

This project demonstrates how a Random Forest works internally—without scikit-learn—by reconstructing:

- Tree building  
- Bagging  
- Random feature selection  
- Majority voting  
- Importance scoring  

It serves both as a teaching tool and as a functional baseline model for binary classification.

Future extensions could include:

- Out-of-bag (OOB) error estimation  
- Random Forest regression  
- Hyperparameter tuning  
- Visualization of decision boundaries  

---
