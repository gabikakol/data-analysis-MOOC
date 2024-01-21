#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split2():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    days = df["Päivämäärä"]
    days2 = days.str.split(expand=True)
    days2.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    weekdays = {
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
    weekdays2 = days2['Weekday']
    weekdays3 = weekdays2.map(weekdays)
    days2['Weekday'] = weekdays3
    months2 = days2['Month']
    months3 = months2.map(months)
    months3 = months3.map(int)
    days2['Month'] = months3
    hours = days2['Hour']
    hours = hours.map(lambda x: x[:2])
    hours = hours.map(int)
    days2['Hour'] = hours
    days3 = days2['Day']
    days3 = days3.map(int)
    days2['Day'] = days3
    years = days2['Year']
    years = years.map(int)
    days2['Year'] = years
    dates, df = days2, df
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    df.drop(["Päivämäärä"], axis=1, inplace=True)
    answer = pd.concat([dates, df], axis=1)
    return answer

def bicycle_timeseries():
    x = split2()
    x["Date"] = pd.to_datetime(x[["Year", "Month", "Day", "Hour"]])
    x.drop(columns=["Year", "Month", "Day", "Hour"], inplace=True)
    x.set_index("Date", inplace=True)
    return x


def commute():
    timeseries = bicycle_timeseries()
    x = timeseries["2017-08-01":"2017-08-31"]
    answer = x.groupby("Weekday").sum()
    return answer
    
def main():
    df = commute()
    df.plot()
    plt.show()


if __name__ == "__main__":
    main()