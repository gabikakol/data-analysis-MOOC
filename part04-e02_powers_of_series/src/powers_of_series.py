#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    result_df = pd.DataFrame(index=s.index)    
    for i in range(1, k + 1):
        result_df[i] = s.pow(i)
    return result_df

def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    result = powers_of_series(s, 3)
    print(result)

if __name__ == "__main__":
    main()
