#!/usr/bin/env python3

import pandas as pd

def main():
    file_path = "src/municipal.tsv"
    df = pd.read_csv(file_path, sep='\t')
    print(f"Shape: {df.shape[0]},{df.shape[1]}")
    print("Columns:")
    for col in df.columns:
        print(col)

if __name__ == "__main__":
    main()
