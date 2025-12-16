# Principal Component Analysis (PCA)

This repository contains a full, from-scratch implementation of **Principal Component Analysis (PCA)** applied to the Spotify audio feature dataset.  
The goal of this module is not classification or prediction, but **understanding structure**, **reducing dimensionality**, and **revealing the latent axes** that organize musical attributes.

PCA serves as a foundational tool in the unsupervised learning pipeline and is commonly used before clustering, visualization, and anomaly detection tasks.

---

## What Is PCA?

Principal Component Analysis is a linear transformation that:

- Centers the data  
- Computes the covariance matrix  
- Extracts eigenvalues and eigenvectors  
- Projects the data into an uncorrelated basis ordered by explained variance  

Mathematically:

\[
Z = XW
\]

Where:

- **\( X \)** — centered feature matrix  
- **\( W \)** — eigenvectors of covariance matrix (principal directions)  
- **\( Z \)** — transformed data in PCA space  

Each principal component:

- captures maximal remaining variance  
- is orthogonal to all previous components  
- represents a meaningful direction in the data's geometry  

---

## Why PCA?

PCA is used to:

- Reduce redundant or correlated features  
- Compress high-dimensional data  
- Improve computational efficiency  
- Visualize 9–50+ dimensional data in **2D or 3D**  
- Preprocess data for clustering (K-Means, DBSCAN, GMMs, etc.)  
- Understand the structure of musical features (energy, valence, tempo, etc.)

In the Spotify dataset, PCA helps uncover patterns such as:

- energy-driven variation across songs  
- rhythmic/mood axes  
- separation of speech-heavy vs. instrumental tracks  

---

## Methodology

### **1. Data Preparation**
- Extract nine core audio features (danceability, energy, loudness, etc.)  
- Standardize to zero mean and unit variance  
- Compute covariance matrix of standardized features  

### **2. Eigen-Decomposition**
From covariance matrix \( C \):

\[
C = V \Lambda V^\top
\]

Where:  
- \( \Lambda \) = eigenvalues (variance explained)  
- \( V \) = eigenvectors (principal axes)  

Eigenvalues rank components by importance; cumulative sums determine how many components capture most variance.

### **3. Projection**
Data is projected using:

\[
Z = X V_k
\]

Where \( V_k \) contains the top-\( k \) eigenvectors.

### **4. Interpretation**
PCA loadings explain how original features contribute to each component. Examples:

- **PC1:** Often dominated by energy + loudness  
- **PC2:** Often reflects rhythmic/mood structure (danceability, valence)  
- **PC3:** Often distinguishes speechiness vs. instrumentalness  

These axes give a compressed but meaningful representation of musical variation.

---

## Visualization Components Include:

- **Scree plot** (variance explained by each component)  
- **Cumulative variance chart**  
- **Loading matrix heatmaps**  
- **2D scatter of PC1 vs. PC2**  
- **3D PCA visualization for deeper structure**  

Each helps clarify how PCA reshapes feature space.

---

## Applications

PCA is used as:

### **Dimensionality Reduction**
Compress 9 features → 2–4 components while preserving ∼90% variance.

### **Preprocessing for Other Models**
- Clustering (K-Means, DBSCAN)  
- Anomaly detection  
- Regression pipelines  
- Recommendation systems  

### **Exploratory Analysis**
Visualizing genres, moods, or artist clusters in PCA space.

---

## Limitations

- PCA is fully **linear**, cannot capture nonlinear structure  
- Sensitive to scaling (features must be standardized)  
- Principal components can be hard to interpret  
- High-variance directions are not always the most predictive  
- Outliers may distort components  

---

## Conclusion

This implementation demonstrates PCA as a powerful unsupervised tool:

- reveals hidden structure in Spotify features  
- compresses data efficiently  
- enables interpretable 2D/3D visualization  
- enhances downstream machine learning workflows  

PCA forms a core part of the unsupervised module in this repository and sets the stage for clustering, mixture models, and advanced dimensionality reduction methods.
