# **Unsupervised Learning Module**

## **Overview**
Unsupervised learning analyzes **unlabeled data** to uncover structure, patterns, and relationships. It is used for clustering, dimensionality reduction, anomaly detection, and exploratory analysis. Unlike supervised learning, these methods do not predict outcomes—they reveal how the data organizes itself.

This module implements four core unsupervised algorithms **from scratch** and applies them to the **topsongs.csv** dataset to compare how different techniques interpret the same musical feature space.

---

## **Algorithms Implemented**

### **1. Principal Component Analysis (PCA)**
**Type:** Dimensionality Reduction  
**Purpose:** Compress high-dimensional audio features into orthogonal components that capture the most variance.  
**Method:**  
- Standardize features  
- Compute covariance matrix  
- Extract eigenvalues/eigenvectors  
- Project data onto principal components  
Used for visualization and preprocessing before clustering.

---

### **2. K-Means Clustering**
**Type:** Partitioning Clustering  
**Purpose:** Group tracks into *k* clusters based on similarity in feature space.  
**Method:**  
- Initialize centroids  
- Assign → update steps  
- Minimize within-cluster variance  
Used to identify song groupings and genre-like structure in numeric audio features.

---

### **3. Hierarchical Clustering**
**Type:** Agglomerative Clustering  
**Purpose:** Build a tree of song clusters using pairwise distances.  
**Method:**  
- Compute linkage matrix (single linkage)  
- Visualize with dendrogram  
- Optional cluster extraction via tree cutting  
Useful for multi-level structure and understanding how clusters merge.

---

### **4. DBSCAN**
**Type:** Density-Based Clustering  
**Purpose:** Detect dense song clusters and label sparse points as noise.  
**Method:**  
- Use `eps` + `min_samples` to define neighborhoods  
- Identify core vs. border vs. noise points  
- Clusters form where density exceeds threshold  
Captures irregular shapes and identifies outliers in musical feature space.

---
