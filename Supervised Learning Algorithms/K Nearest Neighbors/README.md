# K-Nearest Neighbors (From Scratch)

This repository contains a complete from-scratch implementation of **K-Nearest Neighbors (KNN)** and applies it to the Spotify Top Songs (2000–2019) dataset to study how audio features relate to hit prediction.  
KNN is a simple but powerful baseline algorithm that relies entirely on local similarity rather than learned parameters.

---

## 🎧 What Is K-Nearest Neighbors?

KNN is a **non-parametric classification algorithm** that predicts labels by comparing a new input to the *K* closest points in the training set.

Steps:

1. Compute the distance between the query point and all training samples  
2. Select the *K* nearest neighbors  
3. Use majority vote to assign a class label  

KNN requires no training phase and is highly interpretable, making it a popular introductory machine learning algorithm.

---

## 🧠 Project Overview

This project implements KNN **entirely from first principles**, including:

- A custom Euclidean distance function  
- Manual neighbor sorting and selection  
- Majority voting for final prediction  
- A custom class with `.fit()`, `.predict()`, and `.score()` methods  
- Evaluation across multiple values of *K*  
- Application to real-world music data  

No scikit-learn KNN model is used—the implementation is fully manual.

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `KNN.ipynb` | Complete implementation, explanation, and evaluation. |
| `spotiml/knn.py` | Source code for the custom KNN classifier. |
| `topsongs.csv` | Spotify dataset used for experiments. |

---

## 🎼 Dataset Description

The dataset contains **2,000 tracks** released between 2000–2019, with features such as:

- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- tempo  

A binary target variable is created:

- **1 → hit** (popularity ≥ 70)  
- **0 → non-hit**  

Class distribution:

- **36.35% hits**  
- **63.65% non-hits**

Because of this imbalance, KNN tends to favor the majority class.

---

## 🛠️ Algorithm Summary

The notebook implements and analyzes KNN through the following:

### **Model Mechanics**
- Standardized numerical features  
- Euclidean distance for similarity  
- Manual ranking of neighbors  
- Majority vote among K nearest points  

### **Evaluation Approach**
- Run K from **1 to 15**  
- Compute accuracy at each K  
- Select optimal K based on maximum accuracy  
- Evaluate final model via confusion matrix  

---

## 📊 Results & Interpretation

### **K Performance Summary**
Accuracy ranged from **57% to 62.5%**, with the best model at:

- **Best K = 10**  
- **Final Test Accuracy = 0.6250**

### **Confusion Matrix**

[[226 29]
[121 24]]

### **Key Observations**

#### **1. Strong at Predicting Non-Hits**
- 226 non-hits correctly identified  
- Few false positives  
- Indicates that non-hit songs cluster well in feature space  

#### **2. Weak at Predicting Hits**
- Only 24 hits correctly classified  
- 121 hits misclassified  
- Suggests hit songs lack strong or consistent acoustic clustering  

#### **3. Audio Features Alone Do Not Predict Popularity**
Popularity depends heavily on:
- marketing  
- playlist placement  
- artist visibility  

These factors cannot be captured by audio features alone.

#### **4. KNN’s Structural Limitations Show Clearly**
KNN struggles with:
- imbalanced classes  
- overlapping high-dimensional data  
- the need for feature weighting (which KNN does not learn)  

---

## ⭐ Why These Results Matter

This module highlights:

- The behavior of distance-based classifiers on real musical data  
- The difficulty of predicting popularity from acoustic features alone  
- How baseline models set the stage for deeper, more flexible methods  
- The value in evaluating both strengths and weaknesses of simple algorithms  

The KNN results serve as a benchmark for more advanced models in this project.

---

## 📈 Conclusion

The KNN module demonstrates:

- Manual construction of a classic ML algorithm  
- Hyperparameter tuning across multiple values of K  
- Application to real Spotify audio features  
- Interpretation of classifier strengths and limitations  

While simple, KNN provides meaningful intuition and a baseline for comparison across the broader repository.

---

Created by **Arman Saxena**  
Feel free to open an issue or reach out with questions or suggestions.

