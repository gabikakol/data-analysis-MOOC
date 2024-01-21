#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    stats = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    stats2 = stats.groupby("Publisher")
    stats_sum = stats2.sum()["WoC"]
    stats_sorted = stats_sum.sort_values(ascending=False)
    best = stats_sorted.index[0]
    songs = stats[stats["Publisher"] == best]
    return songs

def main():
    best_record_company()
    

if __name__ == "__main__":
    main()