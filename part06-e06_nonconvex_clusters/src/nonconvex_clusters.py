#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def nonconvex_clusters():
    data = pd.read_csv('src/data.tsv', sep='\t')
    x = data.loc[:, ['X1', 'X2']]
    lab = data.iloc[:, -1]
    lab_len = len(set(lab))
    list1 = []
    for i in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=i)
        model.fit(x)
        outln = 0
        clusters = len(set(model.labels_))
        if -1 in model.labels_:
            clusters -= 1
            outln = list(model.labels_).count(-1)
        perm = find_permutation(clusters, lab, model.labels_)
        new_lab = pd.DataFrame([perm[i] for i in model.labels_]).iloc[:, 0]
        non_out = model.labels_ == -1
        if lab_len != clusters:
            result = None
        else:
            result = accuracy_score(lab[~non_out], new_lab[~non_out])
        list1.append([i, result, clusters, outln])
    data = pd.DataFrame(list1, columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype=float)
    return data

def find_permutation(n_clusters, real_labels, labels):
    perm = []
    for i in range(n_clusters):
        x = labels == i
        new_label = scipy.stats.mode(real_labels[x])[0][0]
        perm.append(new_label)
    return perm

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()