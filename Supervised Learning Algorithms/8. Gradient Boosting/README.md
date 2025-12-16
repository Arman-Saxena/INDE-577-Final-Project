# Gradient Descent

This directory contains a complete, from-first-principles implementation of **Gradient Descent**, applied to a binary classification task using the Spotify dataset.

The focus of this module is not on achieving state-of-the-art accuracy, but on demonstrating **how optimization works underneath nearly every machine learning algorithm**.

---

## What Is Gradient Descent?

Gradient Descent is one of the most fundamental optimization algorithms in machine learning.  
It provides a general procedure for minimizing any differentiable loss function by updating model parameters in the direction that **reduces the loss most quickly**.

For a parameter vector \( \theta \), learning rate \( \gamma \), and loss function \( L(\theta) \):

\[
\theta_{t+1} = \theta_t - \gamma \nabla L(\theta_t)
\]

This simple rule forms the backbone of:

- Linear & Logistic Regression  
- Neural Networks  
- SVMs  
- Deep Learning optimization algorithms (Adam, RMSProp, Momentum, etc.)

In this project, Gradient Descent is implemented using raw NumPy operations.

---

## Project Overview

This module implements:

### **1. Manual Gradient Descent Engine**
- Full-batch updates  
- Explicit computation of gradients  
- Sigmoid activation + Binary Cross-Entropy loss  
- Custom convergence tolerance  
- Training loop with loss tracking  

### **2. Binary Classifier Using Logistic Regression Structure**
Gradient Descent optimizes:

\[
L = - \left( y\log \hat{y} + (1-y)\log (1-\hat{y}) \right)
\]

Where:

\[
\hat{y} = \sigma(w^\top x + b)
\]

### **3. Evaluation & Diagnostics**
- Accuracy  
- Confusion Matrix  
- Loss curve inspection  
- Discussion of convergence behavior  

This project demonstrates the *mechanics* behind model training rather than relying on automated toolkits.

---

## Algorithm Summary

### **Gradient Descent Update Rule**

\[
w \leftarrow w - \gamma \cdot \frac{\partial L}{\partial w}
\]

\[
b \leftarrow b - \gamma \cdot \frac{\partial L}{\partial b}
\]

### **Key Hyperparameters**
- **Learning Rate (\(\gamma\))**  
  Controls step size; too small → slow convergence, too large → divergence.
  
- **Max Iterations**  
  Upper limit on training.

- **Tolerance (\(\eta\))**  
  Stops training when loss movement becomes negligible.

---

## Example Interpretation

Using the Spotify dataset (2000 samples, 9 features), the Gradient Descent classifier showed:

- **Stable convergence** after ~200 epochs  
- Loss plateau around **0.6843**  
- **Accuracy ≈ 0.57**  
- Confusion Matrix:

|              | Pred 0 | Pred 1 |
|--------------|--------|--------|
| **True 0**   | 114    | 86     |
| **True 1**   | 86     | 114    |

These results reflect the **limitations of linear decision boundaries** on complex musical metadata—but the primary goal of demonstrating optimization dynamics is fully met.

---

## Why Gradient Descent Matters

Even with modest predictive performance, Gradient Descent is the foundation of:

- Deep Learning  
- Transformer architectures  
- Word embeddings  
- Image recognition  
- Reinforcement learning  

Understanding it is essential for understanding how modern ML models learn.

---

## Limitations of Basic Gradient Descent

- Sensitive to learning rate choice  
- Can get stuck in plateaus or saddle points  
- Converges slowly on poorly scaled data  
- Doesn't adapt learning rate (unlike Adam/RMSProp)  

These limitations make it an excellent *teaching tool*, because they reveal how optimization actually behaves.

---

## Conclusion

This project provides:

- A complete Gradient Descent implementation from scratch  
- A transparent demonstration of parameter updates  
- Insight into convergence via loss tracking  

It serves as a foundation for more advanced optimizers such as Momentum, Nesterov, RMSProp, and Adam.

---

