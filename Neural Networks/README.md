# **Neural Networks Module**

## **Overview**
This module implements **feedforward neural networks from scratch using NumPy**, applying them to the `topsongs.csv` dataset for both regression (predicting continuous audio features) and classification (predicting binary song attributes). The goal is to demonstrate how neural networks learn nonlinear relationships through layered transformations, without relying on high-level libraries like scikit-learn or PyTorch.

---

## **Core Concepts**

### **1. Network Architecture**
A neural network is built from:
- **Input layer** — receives standardized numeric audio features  
- **Hidden layers** — apply nonlinear transformations (ReLU or Sigmoid)  
- **Output layer**  
  - Regression: linear neuron  
  - Classification: sigmoid neuron  

Weights are initialized using variance scaling (He/Xavier-style), and biases are initialized randomly.

---

### **2. Forward Propagation**
Each layer performs:

\[
z = W a + b, \quad a = f(z)
\]

Nonlinear activations allow the network to model complex relationships beyond linear transformations.

- **ReLU** for hidden layers (stable gradients, efficient training)  
- **Sigmoid** for binary classification outputs  

---

### **3. Backpropagation**
Gradients are derived manually:
- Uses the chain rule through all layers  
- Computes ∂Loss/∂Weights and ∂Loss/∂Biases  
- Updates parameters via **Stochastic Gradient Descent (SGD)**  

Loss functions:
- **Mean Squared Error (MSE)** for regression  
- **Binary Cross-Entropy (BCE)** for classification  

This module emphasizes understanding *how* gradients flow rather than relying on automatic differentiation.

---

### **4. Training Framework**
Each network trains using:
- Per-sample SGD updates  
- Epoch-level tracking of:
  - Training loss or accuracy  
  - Validation loss or accuracy  
- Monitoring of overfitting via curve comparison  

The methodology illustrates how neural networks iteratively minimize error and refine internal representations of the data.

---

### **5. Evaluation**
After training, the models are evaluated using:

**Regression**
- MSE  
- Predicted vs. actual scatterplots  

**Classification**
- Accuracy  
- Confusion matrix  
- ROC curve  

Visualizations provide insight into model performance, error patterns, and decision thresholds.

---

## **Dataset**
All experiments use the **topsongs.csv** dataset, which contains normalized audio descriptors such as energy, valence, danceability, liveness, and tempo.

Neural networks are a strong fit for this dataset because:
- Musical feature relationships are often nonlinear  
- Targets may be continuous or binary  
- Proper feature scaling improves convergence and stability  

---

## **Learning Goals**
This module demonstrates:
- How neural networks are constructed mathematically  
- How activation functions and loss functions shape learning  
- How backpropagation operates without external ML libraries  
- When neural networks outperform simpler models—and when they may not  

