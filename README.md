# **INDE 577 — Data Science & Machine Learning (Rice University)**  
This repository contains my full collection of machine learning projects completed for **CMOR 438/INDE 577: Data Science & Machine Learning**. Every algorithm—supervised and unsupervised—is implemented **using NumPy**,. The goal is to build conceptual understanding, mathematical intuition, and full control over model behavior.

The repo includes clear Jupyter notebooks, method-focused READMEs, and visualizations across the entire ML pipeline.

---

## **Contents**

### **Supervised Learning**
- **Linear Regression** (normal equation + gradient descent)  
- **Logistic Regression**  
- **Perceptron & Multilayer Perceptron (MLP)**  
- **Neural Networks** (regression + classification)  
- **K-Nearest Neighbors**  
- **Decision Trees**  
- **Random Forests**  

### **Unsupervised Learning**
- **Principal Component Analysis (PCA)**  
- **K-Means Clustering**  
- **Hierarchical Clustering**  
- **DBSCAN**  

Each algorithm includes:
- Mathematical formulation  
- Clean, modular from-scratch implementation  
- Training/validation loops  
- Visual explanations and interpretations  
- Comparisons across methods on the **topsongs.csv** dataset when applicable  

---

## **Primary Dataset**
Most projects use the **topsongs.csv** dataset, which contains standardized numerical audio features (danceability, energy, tempo, etc.). This consistent dataset allows direct comparison of how different models interpret the same feature space.

Additional toy datasets or random data are used where conceptually helpful.

---

## **Tools & Environment**
- **Python 3**  
- **NumPy, Pandas, Matplotlib**  
- **Jupyter Notebook**  

---

## **Purpose of the Repository**
This project demonstrates:
- How core ML algorithms operate internally  
- How optimization, loss functions, and gradients shape training  
- How unsupervised methods reveal structure without labels  
- How to rigorously evaluate models without black-box libraries 
