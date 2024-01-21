#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t', index_col=0)
    sub = df.iloc[0:10, [1,2]]
    return pd.DataFrame(sub)

def main():
    subsetting_by_positions()

if __name__ == "__main__":
    main()