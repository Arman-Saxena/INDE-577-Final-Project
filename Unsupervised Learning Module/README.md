# **DBSCAN — Density-Based Clustering**

## **Overview**
DBSCAN is an unsupervised clustering algorithm that discovers groups of high-density points while marking low-density points as noise. Unlike K-Means, it **does not require choosing the number of clusters** and can find **arbitrarily shaped** clusters, making it useful for spatial data, anomaly detection, and irregular datasets.

---

## **1. Core Concepts**

DBSCAN is controlled by two parameters:

- **ε (eps):** Maximum distance between two points to be considered neighbors  
- **min_samples:** Minimum number of nearby points required to form a dense region  

Definitions:
- **Core point:** Satisfies min_samples within ε  
- **Border point:** Near a core point but not dense enough  
- **Noise point:** Not reachable from any core  

Clusters form by connecting core points through density reachability.

---

## **2. Methodology**

### **Step 1 — Preprocessing**
- Remove identifier columns  
- Standardize features (critical for distance-based algorithms)  
- Optional: use **PCA** to reduce dimensionality for visualization  

### **Step 2 — Choosing ε**
Use a **k-distance graph**:
1. Compute each point’s k-th nearest neighbor distance  
2. Sort the distances  
3. Plot the curve  
4. Select ε at the “elbow” where the slope changes sharply  

This identifies a threshold separating dense vs. sparse regions.

### **Step 3 — Run DBSCAN**

### **Step 4 — Visualization**
Project data into 2D using PCA and:
1. Color points by cluster
2. Mark noise as -1
3. Optionally compute cluster centroids manually

### **Step 5 - Evaluation**
Because DBSCAN doesn’t optimize a fixed objective:
1. Count clusters and noise points
2. Compute silhouette score (excluding noise)
3. Inspect cluster shape and density
Comparison with K-Means can highlight DBSCAN’s ability to detect irregular structures.

---

## **3. Strengths**

1. No need to predefine number of clusters
2. Finds arbitrarily shaped clusters
3. Naturally detects outliers
4. Useful in geospatial, customer segmentation, and anomaly detection tasks

---

## **4. Limitations**

1. Sensitive to ε and feature scaling
2. Struggles when clusters have varying densities
3. High-dimensional data can degrade performance

---

## **5. Conclusions**

This DBSCAN implementation demonstrates:
1. Proper preprocessing for density-based clustering
2. Systematic ε selection via k-distance graph
3. Cluster discovery without assuming structure
4. PCA visualization and density interpretation
DBSCAN offers a flexible alternative to centroid-based methods, especially when clusters are non-spherical or when noise detection is important.

---


