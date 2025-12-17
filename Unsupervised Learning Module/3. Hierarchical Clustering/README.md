# **Hierarchical Clustering (Spotify Audio Features Dataset)**  
### *Unsupervised Learning Methodology & Implementation Guide*

---

## **Overview**

Hierarchical clustering is an unsupervised learning method that builds a hierarchy of clusters without requiring labels or a predefined number of groups. Unlike K-Means, which partitions data into *k* clusters using centroid optimization, hierarchical methods construct a **tree structure (dendrogram)** that reveals relationships among points at multiple scales.

In this notebook, we implement **agglomerative hierarchical clustering**—merging the closest clusters step-by-step—and use SciPy only for efficient distance computation and dendrogram visualization. This approach allows us to examine the algorithmic process in detail while applying it to the Spotify audio features dataset.

---

## **What Hierarchical Clustering Does**

Hierarchical clustering follows this iterative process:

1. **Start with each point as its own cluster**
2. **Compute pairwise distances** between all clusters
3. **Merge the two closest clusters**
4. **Record the merge** in a linkage matrix *(cluster A, cluster B, distance, combined size)*
5. **Repeat until only one cluster remains**

This produces a **linkage matrix**, which encodes the entire clustering hierarchy and supports dendrogram plotting.

### **Why This Is Useful**
- Reveals cluster structure at all distance thresholds  
- Naturally identifies outliers  
- Does not require choosing *k* in advance  
- Allows visual interpretation through a dendrogram  

Hierarchical methods are ideal for exploratory analysis and for datasets where the number or shape of clusters is unknown.

---

## **Preprocessing & PCA**

Before clustering:

- **Standardization** ensures all features contribute equally to distance calculations.
- **PCA** is used *only for visualization*, not for clustering.  
  - It compresses the dataset into 2 principal components.  
  - It enables clear scatterplots of cluster structure.  

This combination supports meaningful interpretation without altering the underlying clustering computation.

---

## **Algorithmic Implementation**

### **1. Standardizing the Data**
All numeric Spotify audio features (danceability, energy, loudness, valence, tempo, etc.) are scaled to zero mean and unit variance.  

This prevents any single feature from dominating Euclidean distance.

---

### **2. Computing the Linkage Matrix**

This ensures equal contribution to Euclidean distance.

Reasons for using SciPy rather than a full from-scratch implementation:

Correct cluster bookkeeping

Avoids invalid merges

Much faster on datasets with ~2000 samples

Integrates seamlessly with dendrogram visualization tools

### **3. Dendogram**

How to interpret the dendrogram:

Height of merges → distance between clusters

Large vertical gaps → natural cluster boundaries

Late merges → potential outliers

Branch density → compact vs. diffuse clusters

### **4. Extracting k Clusters**

To cut the dendrogram into the desired number of clusters:

from scipy.cluster.hierarchy import fcluster
labels = fcluster(Z, t=4, criterion='maxclust')

This produces 4 clusters based on the hierarchical structure.

