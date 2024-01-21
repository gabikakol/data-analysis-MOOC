#!/usr/bin/env python3

from gzip import open
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

def spam_detection(random_state=0, fraction=1.0):
    ham_list = None
    spam_list = None
    ham_file = 'src/ham.txt.gz'
    spam_file = 'src/spam.txt.gz'
    with open(ham_file) as ham_data:
        ham_list = ham_data.readlines()
        num_lines = int(fraction * len(ham_list))
        ham_list = ham_list[:num_lines]
    with open(spam_file) as spam_data:
        spam_list = spam_data.readlines()
        num_lines = int(fraction * len(spam_list))
        spam_list = spam_list[:num_lines]    
    vector_counter = CountVectorizer()  
    X_rows = ham_list + spam_list  
    X = vector_counter.fit_transform(X_rows).toarray()
    y = np.zeros(len(X_rows))
    y[len(ham_list):] = 1
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    y_fitted = nb.predict(X_test)
    outcome = accuracy_score(y_test, y_fitted)
    misclassified = np.sum(y_test != y_fitted)
    return (outcome, len(X_test), misclassified)

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()