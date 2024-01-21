#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df1 = df["Population change from the previous year, %"]
    municipalities1 = len(df1)
    df2 = df[df["Population change from the previous year, %"] > 0]
    return (len(df2)/municipalities1)

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    df = df["Akaa":"Äänekoski"]
    dec = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {dec:.1f}%")


if __name__ == "__main__":
    main()