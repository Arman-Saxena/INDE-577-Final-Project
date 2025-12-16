# **K-Means Clustering**

## **Overview**

This module implements **K-Means Clustering from scratch** and applies it to a standardized subset of the Spotify dataset. K-Means is an unsupervised learning algorithm that partitions observations into *k* groups, where each group is defined by a centroid representing the mean of its assigned data points. Unlike the supervised models in earlier modules, K-Means operates without labels, discovering natural structure within the audio-feature space.

This notebook focuses on:

- Understanding the geometry of clustering
- Using PCA for visualization
- Applying the **elbow method** to evaluate *k*
- Interpreting clusters within Spotify audio features

K-Means is one of the foundational techniques in unsupervised learning and serves as a bridge toward later clustering techniques such as Gaussian Mixture Models, DBSCAN, and spectral clustering.

---

## **Methodology**

### **1. Data Preparation**

All experiments use 9 numeric Spotify audio features:

- **danceability, energy, loudness, speechiness, acousticness**  
- **instrumentalness, liveness, valence, tempo**

Steps:

1. Select numerical columns  
2. Standardize using z-score scaling (required because K-Means is distance-based)  
3. Store the resulting matrix as the input feature space  

Standardization ensures that features with large ranges (e.g., loudness) do not dominate distance computations.

---

### **2. K-Means Algorithm (From Scratch)**

The algorithm implemented follows the classic iterative structure:

1. **Initialize centroids** randomly from the dataset  
2. **Assignment step**: assign each point to nearest centroid  
3. **Update step**: compute new centroids as cluster means  
4. Repeat until convergence or maximum iterations  

Distance metric: **Euclidean distance**

Convergence occurs when centroids stop changing significantly.

This implementation returns:

- Final centroid matrix  
- Cluster assignments  
- Inertia (sum of squared distances to centroids)  
- Cluster sizes  

---

### **3. Model Evaluation: Elbow Method**

Because K-Means has no intrinsic accuracy metric, we rely on **inertia** and the **elbow method**.

Procedure:

- Compute inertia for *k* = 1 to 10  
- Plot inertia vs. k  
- Identify the "elbow" where improvements begin to plateau  

For the Spotify dataset:

- Inertia drops sharply for small values of *k*  
- Clear elbow around **k = 7**  
- A **slight increase** in inertia at *k = 9**, confirming over-segmentation  

---

### **4. PCA Projection for Visualization**

Since the dataset is 9-dimensional, PCA is used for visualization.

PCA helps:

- Reveal cluster separation in 2D  
- Identify tight vs. dispersed clusters  
- Understand relationships between features and cluster structure  

PC1 captures the strongest musical axis (high energy/loudness vs. acousticness), making it well-suited for visual interpretation.


