#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    a1 = df["Päivämäärä"]
    frame1 = a1.str.split(expand=True)
    frame1.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    days = {
        'ma': 'Mon',
        'ti': 'Tue',
        'ke': 'Wed',
        'to': 'Thu',
        'pe': 'Fri',
        'la': 'Sat',
        'su': 'Sun'
    }
    months = {
        'tammi': 1,
        'helmi': 2,
        'maalis': 3,
        'huhti': 4,
        'touko': 5,
        'kesä': 6,
        'heinä': 7,
        'elo': 8,
        'syys': 9,
        'loka': 10,
        'marras': 11,
        'joulu': 12
    }
    days_frame = frame1['Weekday']
    days_frame2 = days_frame.map(days)
    frame1['Weekday'] = days_frame2
    month_frame = frame1['Month']
    month_frame2 = month_frame.map(months)
    month_frame2 = month_frame2.map(int)
    frame1['Month'] = month_frame2
    hourf1 = frame1['Hour']
    hf2 = hourf1.map(lambda x: x[:2])
    hf2 = hf2.map(int)
    frame1['Hour'] = hf2
    df1 = frame1['Day']
    df1 = df1.map(int)
    frame1['Day'] = df1
    yf1 = frame1['Year']
    yf1 = yf1.map(int)
    frame1['Year'] = yf1
    print(frame1)
    return frame1

def main():
    split_date()
       
if __name__ == "__main__":
    main()