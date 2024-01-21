#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    df1 = df.loc[:, 'X1':'X5']
    df2 = df.loc[:, 'Y']
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(df1,df2)
    scr = model.score(df1, df2)
    array = [scr]
    for column in df.columns:
        a = df.loc[:, column]
        a = a.values.reshape(-1,1)
        model.fit(a,df2)
        scr2 = model.score(a, df2)
        array.append(scr2)
    return array    
    
def main():
    coefficient = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {coefficient[0]}")
    print(f"R2-score with feature(s) X1: {coefficient[1]}")
    print(f"R2-score with feature(s) X2: {coefficient[2]}")
    print(f"R2-score with feature(s) X3: {coefficient[3]}")
    print(f"R2-score with feature(s) X4: {coefficient[4]}")
    print(f"R2-score with feature(s) X5: {coefficient[5]}")


if __name__ == "__main__":
    main()
