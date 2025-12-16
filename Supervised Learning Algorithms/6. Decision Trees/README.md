# Decision Tree

This repository contains a full, from-first-principles implementation of a **Decision Tree Classifier**, designed to classify Spotify tracks as “hits” or “non-hits” based on audio features.  
Unlike linear models or perceptrons, decision trees learn a series of **hierarchical splitting rules** that partition the feature space into increasingly pure regions. This README focuses on the methodology behind decision trees, how they are constructed from scratch, and how they operate on real-world data.

---

## What Is a Decision Tree?

A decision tree is a **non-parametric supervised learning algorithm** used for classification and regression. It learns a flowchart-like structure of binary decisions:

- **Internal nodes**: test a feature value (e.g., *is loudness > –5.2?*)  
- **Branches**: represent the outcome of that test  
- **Leaf nodes**: assign a final class label  

This creates a model that is **interpretable**, **rule-based**, and able to capture **nonlinear relationships**.

---

## Methodology: How Decision Trees Are Built

This implementation builds a decision tree entirely from scratch, using the classic **CART (Classification and Regression Trees)** framework.

### **1. Impurity Measurement**

At each node, the algorithm measures how “mixed” the labels are.  
We implement **Gini Impurity**, defined as:

\[
G = 1 - \sum_{k=1}^{K} p_k^2
\]

Where \(p_k\) = proportion of samples belonging to class \(k\).

- Low Gini → purer node  
- High Gini → mixed labels  

---

### **2. Finding the Best Split**

For every feature and every possible threshold:

1. Split the dataset into left/right branches  
2. Compute the weighted impurity of the split  
3. Compute **Information Gain**:

\[
IG = G_{\text{parent}} - \left( \frac{n_L}{n}G_L + \frac{n_R}{n}G_R \right)
\]

4. Choose the split with **maximum information gain**

This allows the tree to discover nonlinear rules such as:

> “If valence ≤ 0.15 and acousticness ≤ –0.74 → classify as non-hit.”

---

### **3. Recursive Tree Construction**

The algorithm recursively:

- Evaluates all features  
- Selects the best split  
- Creates left and right child nodes  
- Stops when:  
  - The node is pure  
  - No split improves impurity  
  - The depth limit is reached  
  - Minimum sample requirements are violated  

The result is a **hierarchical partition of the Spotify feature space**, producing rules that are readable and interpretable.

---

## Application to Spotify Hit Classification

The model was trained on:

- **Dataset size:** 2,000 songs  
- **Features used:** 9 standardized audio attributes  
- **Positive class (hit):** popularity ≥ 70  
- **Positive class proportion:** 36.35%  

The tree learns dozens of splits involving features such as:

- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- valence  
- tempo  

Many leaves become highly specific, demonstrating the model’s expressive power but also its susceptibility to overfitting.

---

## My Example

A simplified excerpt of the learned tree:

[X7 ≤ 0.151] → valence
[X3 ≤ -0.523] → speechiness
Leaf → class 0
[X5 ≤ -0.162] → instrumentalness
...
[X2 ≤ -0.710] → loudness
[X8 ≤ 0.220] → tempo

This illustrates how decision trees generate **nested, hierarchical rules**.

---

## Strengths of Decision Trees

- **Interpretable**: produces clear, human-readable rules  
- **Nonlinear**: naturally models complex relationships  
- **No feature scaling required**  
- **Automatically captures feature interactions**  
- **Fast inference**  

---

## Limitations

- **Prone to overfitting**, especially without pruning  
- **Unstable** — small data changes may produce a different tree  
- **Greedy splitting may miss globally optimal trees**  
- **Features with many thresholds may dominate splits**  

These drawbacks are why ensemble methods such as **Random Forests** and **Gradient Boosting** often perform better in practice.

---

## Evaluation Outputs

This implementation provides:

- Final tree structure (text format)  
- Confusion matrix  
- Accuracy score  
- Decision boundaries (visualization)  
- Full recursive rule explanation  

These make it easy to understand how the model behaves and why it assigns a given class.

---

## Repository Contents

| File | Description |
|------|-------------|
| `Decision_Tree.ipynb` | Full explanation, from-scratch implementation, and analysis. |
| `decision_tree.py` | Core decision tree source code. |
| `utils.py` | Helper functions for impurity, splits, and accuracy. |
| `data/topsongs.csv` | Spotify dataset used in this project. |

---

## Conclusion

This project demonstrates:

- How decision trees work internally  
- How impurity, information gain, and recursive splits interact  
- How nonlinear rules emerge from audio features  
- How decision trees perform on real-world Spotify data  

The decision tree serves as an excellent interpretable model and a strong baseline before exploring ensemble methods.

---
