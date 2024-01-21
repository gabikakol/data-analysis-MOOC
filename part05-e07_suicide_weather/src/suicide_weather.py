#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',', index_col="country")
    df.drop(["year", "sex", "age"], axis=1, inplace=True)
    df["mean"] = df["suicides_no"] / df["population"]
    df_grouped = df.groupby("country")
    df_mean = df_grouped["mean"].mean()
    return df_mean
    
def suicide_weather():
    deaths = suicide_fractions()
    weather = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col="Country")[0]
    weather = weather.iloc[:, 0].str.replace("\u2212", "-").astype(float)
    df_weather = pd.merge(weather, deaths, left_index=True, right_index=True)
    ratio = df_weather.corr(method='spearman').iloc[0, 1]
    (death_rows, temp_rows, common_rows) = (x.shape[0] for x in [deaths, weather, df_weather])
    return death_rows, temp_rows, common_rows, ratio

def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")

if __name__ == "__main__":
    main()