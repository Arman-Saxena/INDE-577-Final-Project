# Multilayer Perceptron 

This directory contains a full, from-first-principles implementation of a **Multilayer Perceptron (MLP)** trained on the Spotify Top Hits (2000–2019) dataset.  
Unlike the single-layer perceptron or logistic regression, the MLP introduces **nonlinearity** and **hidden layers**, enabling the model to learn richer patterns in musical audio features.

The notebook includes:

- A manually implemented neural network with:
  - custom forward pass  
  - custom backpropagation  
  - gradient-based optimization  
  - loss tracking and convergence visualization  
- Evaluation on a real-world dataset  
- Confusion matrix and accuracy reporting  
- Interpretation of model behavior  

---

## What Is a Multilayer Perceptron?

An MLP is a feed-forward neural network composed of:

- **Input layer** (audio features)
- **Hidden layers** (nonlinear transformations)
- **Output layer** (binary hit prediction)

Mathematically:

\[
h = f(W_1 x + b_1), \qquad 
\hat{y} = \sigma(W_2 h + b_2)
\]

Where:

- \( f(\cdot) \) is an activation function (ReLU in this project)  
- \( \sigma(\cdot) \) is the sigmoid output  
- \( W_1, W_2 \) and \( b_1, b_2 \) are learnable parameters  

This structure allows the network to capture **nonlinear** patterns that linear models cannot.

---

## Repository Contents

| File | Description |
|------|-------------|
| `MLP.ipynb` | Full training pipeline, visualizations, evaluation, and interpretation. |
| `spotiml/mlp.py` | Source code for the custom MLP class. |

---

## Algorithm Summary

### **Forward Pass**
1. Compute hidden layer output using ReLU  
2. Compute predicted probability via sigmoid  
3. Compute binary cross-entropy loss  

### **Backward Pass (Backpropagation)**
- Compute gradient of loss w.r.t. each parameter  
- Update weights with learning rate \( \alpha \)  
- Store loss history for visualization  

### **Loss Function**

\[
L = -[y\log(\hat{y}) + (1-y)\log(1-\hat{y})]
\]

---

## Evaluation

The model is evaluated using:

- **Accuracy**  
- **Confusion matrix**  
- **Loss curve**  
- **Classification performance**  

These metrics help compare the MLP to other supervised models such as Logistic Regression, Perceptron, and KNN.

---

## Results

- **Feature matrix:** (2000 × 9)  
- **Positive class proportion:** 0.3635  

### Training Loss (sampled)

- Iteration 0: **0.7766**  
- Iteration 1000: **0.6463**  
- Iteration 1800: **0.6427**  

### Final Test Accuracy

**0.6325**

### Confusion Matrix

[[243 12]
[135 10]]

The model consistently identifies non-hit tracks but struggles more with the minority positive class due to dataset imbalance.

---

## Interpretation

- The MLP learns a **nonlinear** mapping between musical features and popularity.  
- Accuracy surpasses linear models, suggesting deeper structure in the audio data.  
- Most false negatives arise from the imbalance in hit vs. non-hit tracks.  
- Performance could improve with:
  - More layers or hidden units  
  - Better weight initialization  
  - Regularization  
  - Class-balancing methods (e.g., oversampling, class weights)  
  - Additional metadata (genre, artist trends, year)  

---

## Limitations

- Sensitive to learning rate and training epochs  
- Requires careful tuning to avoid vanishing or exploding gradients  
- Limited by audio-only features — popularity is influenced by external social and cultural factors not captured in the dataset  

---

## Conclusion

This project demonstrates how to implement and train a multilayer perceptron from scratch, including:

- Forward and backward propagation  
- Optimization with gradient descent  
- Loss visualization  
- Performance evaluation  

It establishes a strong basis for future neural network extensions such as:

- Deeper architectures  
- Dropout + regularization  
- Hyperparameter search  
- Migration to PyTorch/TensorFlow for large-scale modeling  

---
