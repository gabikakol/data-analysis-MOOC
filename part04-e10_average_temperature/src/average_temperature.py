#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    jul = df[df.m == 7]
    temp_jul = jul["Air temperature (degC)"]
    average = temp_jul.mean()
    return average

def main():
    result = average_temperature()
    print(f"Average temperature in July: {result:.1f}")

if __name__ == "__main__":
    main()