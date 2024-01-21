#!/usr/bin/env python3

import scipy
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    ds = load_iris()
    X, y = ds.data, ds.target
    print(X)
    means = KMeans(3, random_state=0)
    means.fit(X)
    permutation = find_permutation(3, y, means.labels_)
    labels2 = [ permutation[label] for label in means.labels_]
    outcome = accuracy_score(y, labels2)
    return outcome

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
