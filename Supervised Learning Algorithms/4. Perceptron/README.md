# 🧠 Perceptron (From Scratch)

This directory contains a complete, from-first-principles implementation of the **Perceptron algorithm**, one of the earliest and most influential models in machine learning.  
The perceptron acts as a *single-layer linear classifier* and forms the conceptual foundation for modern neural networks.

In this project, the perceptron is applied to the **Spotify Top Hits (2000–2019)** dataset to classify whether a track is a “hit” or “non-hit” based on its acoustic and musical features.

---

## 📌 What Is the Perceptron?

The perceptron models a simplified version of a biological neuron.  
Given an input vector \( x \), it computes:

\[
z = w^\top x + b
\]

Then applies a **unit step activation**:

\[
\hat{y} =
\begin{cases}
1, & z \ge 0 \\
0, & z < 0
\end{cases}
\]

Learning occurs through updates whenever a misclassification happens:

\[
w \leftarrow w + \eta (y - \hat{y}) x
\]
\[
b \leftarrow b + \eta (y - \hat{y})
\]

This makes the perceptron simple and interpretable, but only effective for **linearly separable** data.

---

## 🎧 Project Goal

We train a perceptron to classify whether a Spotify track is a *hit*:

- **hit = 1** if popularity ≥ 70  
- **hit = 0** otherwise  

Features include:

- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- tempo  

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `Perceptron.ipynb` | Full notebook: preprocessing, perceptron implementation, evaluation |
| `spotiml/perceptron.py` | Custom perceptron implementation from scratch |
| `spotiml/utils.py` | Accuracy and confusion matrix helpers |
| `topsongs.csv` | Dataset used for all supervised learning tasks |

---

## 🔧 Implementation Overview

The perceptron is implemented manually with:

- Custom weight initialization  
- Manual activation (step function)  
- Per-sample weight updates  
- No scikit-learn perceptron model used  
- Accuracy and confusion matrix evaluation  
- Interpretation of learned weights  

This implementation exposes the core mechanics of linear classification.

---

## 📊 Results Summary

After training, the perceptron achieved:

- **Accuracy:** 0.5700  

### Confusion Matrix

|               | Pred 0 | Pred 1 |
|---------------|--------|--------|
| **True 0**    | 167    | 88     |
| **True 1**    | 84     | 61     |

### Interpretation

- Performs much better on the majority “non-hit” class (0).  
- Struggles with identifying hits due to:
  - Nonlinear patterns in musical features  
  - Weak linear separability  
  - Class imbalance  

---

## 📉 Learned Weights

danceability : -0.0078
energy : -0.0244
loudness : 0.0041
speechiness : -0.0250
acousticness : 0.0303
instrumentalness : -0.0115
liveness : 0.0141
valence : -0.0009
tempo : -0.0096
bias : -0.0100

### Weight Interpretation

- All weights have **small magnitudes**, indicating very weak linear signals.  
- Slightly positive weights: acousticness, liveness → small push toward “hit.”  
- Negative weights: energy, speechiness → small push toward “non-hit.”  
- Confirms **lack of linear separability** in Spotify audio features.

---

## ⚠️ Limitations of the Perceptron

The perceptron struggles when:

- Data is **not linearly separable**  
- Features interact **nonlinearly**  
- Classes are imbalanced  
- Noise disrupts linear boundaries  

As a result, more flexible models (Logistic Regression, Neural Networks, Random Forests) generally outperform the perceptron on real-world datasets.

---

## ✅ Conclusion

This Perceptron project demonstrates:

- How early neural models learn through weight updates  
- Why some datasets are unsuitable for linear classifiers  
- How audio features relate (weakly) to track popularity  
- The importance of matching model complexity to data complexity  

Despite modest accuracy, the perceptron remains a crucial stepping stone for understanding modern deep learning.

---
