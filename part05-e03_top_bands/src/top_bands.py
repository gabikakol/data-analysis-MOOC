#!/usr/bin/env python3

import pandas as pd

def top_bands():
    stats = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    bands = pd.read_csv('src/bands.tsv', sep='\t')
    stats["Artist"] = stats["Artist"].str.title()
    bands["Band"] = bands["Band"].str.title()
    list1 = pd.merge(bands, stats, left_on='Band', right_on='Artist')
    return list1

def main():
    top_bands()

if __name__ == "__main__":
    main()