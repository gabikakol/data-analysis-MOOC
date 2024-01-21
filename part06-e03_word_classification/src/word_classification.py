#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

a = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet = set(a)

def load_finnish():
    url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load = False
    if load:
        with urllib.request.urlopen(url) as x:
            lines = []
            for line in x:
                lines.append(line.decode('utf-8'))
        data = "".join(lines)
    else:
        with open(filename, "rb") as x:
            data = x.read()
    xml_tree = etree.XML(data)
    y = xml_tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, y))

def load_english():
    with open("src/words", encoding="utf-8") as x:
        lines = map(lambda s: s.rstrip(), x.readlines())
    return lines

def get_features(wordlist):
    v = CountVectorizer(token_pattern=r"(?u)\w|-", analyzer='char', vocabulary=alphabet)
    y = v.transform(wordlist).toarray()
    result = np.hstack((y[:, 1:], y[:, 0].reshape(-1, 1)))
    return result

def contains_valid_chars(s):
    for i in s:
        if i not in a:
            return False
    return True

def get_features_and_labels():
    eng = list(load_english())
    lowercase_eng = [x.lower() for x in eng if x[0].islower()]
    valid_eng = [x for x in lowercase_eng if contains_valid_chars(x)]
    fin = load_finnish()
    lowercase_fin = [x.lower() for x in fin]
    valid_fin = [x for x in lowercase_fin if contains_valid_chars(x)]
    eng1 = get_features(valid_eng)
    eng2 = np.ones((len(valid_eng), 1))
    fin1 = get_features(valid_fin)
    fin2 = np.zeros((len(valid_fin), 1))
    x1 = np.concatenate((fin1, eng1))
    x2 = np.concatenate((fin2, eng2))
    return x1, x2


def word_classification():
    x, y = get_features_and_labels()
    model = MultinomialNB()
    v = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    outcome = cross_val_score(model, x, np.ravel(y), cv=v)
    return outcome


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()