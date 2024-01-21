#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score

def plant_classification():
    ds = load_iris()
    X, y = ds.data, ds.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
    gaussian = naive_bayes.GaussianNB()
    gaussian.fit(X_train, y_train)
    y_fitted = gaussian.predict(X_test)
    outcome = accuracy_score(y_test, y_fitted)
    return outcome

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
