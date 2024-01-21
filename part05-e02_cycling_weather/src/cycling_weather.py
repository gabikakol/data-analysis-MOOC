#!/usr/bin/env python3

import pandas as pd

def split_date():
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
    return (days2, df)

def split_date_continues():
    dates, df = split_date()
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    df.drop(["Päivämäärä"], axis=1, inplace=True)
    result = pd.concat([dates, df], axis=1)
    return result

def cycling_weather():
    cycling_set = split_date_continues()
    weather_set = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    merged_set = pd.merge(cycling_set, weather_set, 
        left_on=['Year', 'Month', 'Day'], right_on=["Year", "m", "d"])
    merged_set.drop(["m", "d", "Time", "Time zone"], axis=1, inplace=True)
    return merged_set

def main():
    cycling_weather()

if __name__ == "__main__":
    main()