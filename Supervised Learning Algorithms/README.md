# [Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning)

---


Supervised learning is a category of machine learning where models are trained using labeled examples—pairs of input feature vectors and known outputs. The algorithm learns a mapping from inputs to outputs by repeatedly following the predict then compare then update cycle:
1. The model uses a feature vector to generate a prediction.
2. The prediction is compared to the true label to compute a loss.
3. The loss is used to update the model parameters, improving future predictions.

Supervised learning tasks are generally divided into two categories:

## Classification
Classification algorithms assign inputs to discrete categories.
In this project, classification is used to determine whether a track is a “hit” based on its audio features from Spotify. Using the dataset’s popularity column, a binary label is defined:
hit = 1  if popularity ≥ 70  
hit = 0  otherwise
This allows us to test how different algorithms interpret musical attributes—such as danceability, energy, valence, tempo, and loudness—to determine whether a song achieved high popularity.

## Regression
Regression models predict continuous outputs and are useful when the target variable is numeric.
Although the primary supervised task in this repository is classification, regression techniques are included for completeness and conceptual understanding. These methods help illustrate how linear models capture relationships between input variables (e.g., acousticness, loudness) and continuous outcomes (e.g., raw popularity score).

## How Supervised Learning Works
Preparing data for supervised learning typically involves the following steps:

Make all data numeric and machine-readable.
For Spotify data, this includes encoding values like explicit or genre, scaling continuous features such as tempo or loudness, and ensuring no missing values remain.

Shuffle the dataset to reduce the risk of bias introduced by sorted or grouped data (e.g., songs ordered by year).

Partition the data into training and testing sets.
Common splits include:

90% training/validation, 10% testing

or 81% training, 9% validation, 10% testing

Separate feature vectors from labels.
In this project, features include the full set of acoustic and musical attributes from Spotify.

Insert a column of ones for bias terms when implementing algorithms from scratch (e.g., Perceptron, Logistic Regression, Linear Regression).

Once the data is prepared, each algorithm is trained on the labeled dataset and then evaluated on unseen test examples. This allows us to compare model performance and understand which approaches are most effective for predicting song popularity.

## Algorithms Implemented
The following supervised learning algorithms are included in this repository. Each one is applied to the Spotify Top Hits (2000–2019) dataset to evaluate its predictive capabilities:

1. K-Nearest Neighbors (KNN)

A non-parametric method that classifies inputs by examining the labels of nearby songs in feature space. KNN often highlights local relationships in acoustic features (e.g., energetic songs cluster with other energetic songs).

2. Linear Regression

A foundational regression method used here for instructional purposes. It models the relationship between Spotify audio features and continuous popularity score.

3. Logistic Regression

A widely used binary classification algorithm. In this project, it predicts whether a track is a “hit” using a sigmoid function to map audio features to probabilities.

4. Perceptron

A linear binary classifier inspired by neural computation. It learns a decision boundary separating hit vs. non-hit songs.

5. Multilayer Perceptron (Neural Network)

A simple fully connected neural network that models nonlinear relationships between audio features. Useful for learning complex interactions—e.g., how tempo, loudness, and energy combine to influence popularity.

6. Decision Trees

A rule-based model that splits the data according to feature thresholds. Decision trees can reveal interpretable patterns, such as:

“If danceability > 0.8 and valence > 0.5, then the track is likely a hit.”

7. Random Forests

An ensemble of decision trees that reduces overfitting and improves accuracy by aggregating predictions from multiple trees. This is often one of the strongest classic ML models for tabular datasets like Spotify’s.

8. Gradient Boosting / Ensemble Methods

Boosting methods sequentially improve weak learners by focusing on misclassified examples. They often outperform single models and provide a more robust predictor of Spotify popularity.

## Dataset Used
All supervised learning experiments use the Spotify Top Hits 2000–2019 dataset, which contains:

1. 18 audio and musical features

2. metadata such as artist, year, genre, and explicit flag

3. a popularity score from 0–100

This consistent dataset allows meaningful comparisons across algorithms under identical conditions.

## Error Analysis
Once each algorithm is trained, error analysis is conducted to assess its performance.

For Classification Tasks (Hit Prediction):

Confusion Matrix

Accuracy

Precision

Recall

F1 Score

ROC Curve & AUC Score

These metrics indicate how well each model identifies high-popularity tracks based on audio features.

For Regression Tasks (Predicting Continuous Popularity):

Mean Squared Error (MSE)

Mean Absolute Error (MAE)

R² Score

Together, these metrics help us understand:

Which models generalize best

How audio features influence popularity

Which transformations or preprocessing steps improve predictions

How linear and nonlinear models differ in their interpretation of music data



