# Unsupervised-Learning-KMeans
Python implementation of K-Means clustering to determine the optimal number of clusters using Silhouette Coefficient on the housing dataset.
# K-Means Clustering using Silhouette Coefficient

This repository contains a Python implementation of the K-Means clustering algorithm to determine the optimal number of clusters (K) using the Silhouette Coefficient metric.

The project is completed as part of **Programming Assignment 4: Unsupervised Learning in Python** under the *Hands-on Approach to AI* program by **IIT Kharagpur AI4ICPS I-Hub Foundation**.

---

## 📌 Objective
- Implement K-Means clustering on a real-world dataset
- Evaluate different values of K using the Silhouette Coefficient
- Identify and output the best K value based on clustering performance

---

## 📂 Files in the Repository
- `template.py` – Python program for computing the best K
- `housing.csv` – Dataset used for clustering
- `README.md` – Project documentation

---

## ⚙️ Execution Instructions
Run the program from the command line by providing the range of K values:

```bash
python template.py <min_k> <max_k>
