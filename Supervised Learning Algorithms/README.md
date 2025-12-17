# **Supervised Learning Module**

## **Overview**
Supervised learning uses **labeled data** to learn a mapping from inputs to outputs. Unlike unsupervised learning, these algorithms are trained to *predict* a target variable—either a class label (classification) or a continuous value (regression).  

This module implements a full suite of supervised algorithms **from scratch** and applies them to the **topsongs.csv** dataset to understand how different models learn patterns in musical attributes and predict a selected target.

---

## **Algorithms Implemented**

### **1. Logistic Regression**
**Type:** Classification  
**Purpose:** Predict binary outcomes (e.g., hit vs. non-hit).  
**Method:**  
- Sigmoid activation  
- Gradient descent optimization  
- Cross-entropy loss

---

### **2. K-Nearest Neighbors (KNN)**
**Type:** Instance-Based Method  
**Purpose:** Classify a track based on the labels of its nearest neighbors.  
**Method:**  
- Euclidean distance  
- Majority voting  
- No explicit training phase  

---

### **3. Linear Regression**
**Type:** Regression  
**Purpose:** Model linear relationships between song features and a continuous target (e.g., popularity).  
**Method:**  
- Closed-form solution (Normal Equation)  
- Gradient-based optimization  
- Error measured via MSE  

---

### **4. Perceptron**
**Type:** Linear Binary Classifier  
**Purpose:** Learn a separating hyperplane for two classes.  
**Method:**  
- Iterative weight updates  
- Sign activation  
- Suitable for linearly separable data  

---

### **5. Multilayer Perceptron (MLP)**
**Type:** Neural Network Classifier  
**Purpose:** Capture nonlinear relationships between Spotify features and the target label.  
**Method:**  
- Hidden layer with nonlinear activation  
- Backpropagation implemented manually  
- Gradient descent optimization  

---

### **6. Decision Tree**
**Type:** Classification / Regression  
**Purpose:** Learn hierarchical rules based on feature splits.  
**Method:**  
- Recursive partitioning  
- Gini impurity / entropy  
- Tree traversal for prediction  

---

### **7. Random Forest**
**Type:** Ensemble Learning  
**Purpose:** Improve tree performance through bootstrap aggregation.  
**Method:**  
- Multiple decision trees  
- Random feature subsets  
- Majority vote (classification)  

---

### **8. Gradient Descent Framework**
**Type:** Optimization Method  
**Purpose:** Provide a unified training mechanism for linear and logistic models.  
**Method:**  
- Iterative parameter updates  
- Learning-rate tuning  
- Loss monitoring  

---
