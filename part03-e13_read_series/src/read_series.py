#!/usr/bin/env python3
import pandas as pd

def read_series():
    data = []

    while True:
        line = input("Enter index and value (separated by whitespace), or press Enter to finish: ")
        
        if not line:
            break

        parts = line.split()

        if len(parts) != 2:
            raise ValueError("Malformed input. Each line should contain index and value separated by whitespace.")

        index, value = parts
        data.append((index, value))

    return pd.Series(dict(data), dtype=object)

def main():
    series = read_series()
    print("Resulting Series:")
    print(series)

if __name__ == "__main__":
    main()
