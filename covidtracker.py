# India Vs USA Covid deaths by month in 2020
# India Vs China Covid deaths by month in 2020

import json
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

def LineGraph(country,df,action):
   country_rows = df[df["Country/Region"] == country]
   country_rows["Date"] = pd.to_datetime(country_rows["Date"])
   country_rows["year_month"] = country_rows["Date"].dt.to_period("M")
   monthly_deaths_in = country_rows.groupby("year_month")[action].sum().reset_index()
   monthly_deaths_in["year_month"] = monthly_deaths_in["year_month"].dt.to_timestamp()
   return monthly_deaths_in 

df = pd.read_csv("full_grouped.csv")

df['Date'] = pd.to_datetime(df['Date'])

# print(monthly_deaths)
monthly_deaths_in = LineGraph("India",df,"Confirmed")
monthly_deaths_us = LineGraph("US",df,"Confirmed")
# us_rows = df[df["Country/Region"] == "US"]
# us_rows["Date"] = pd.to_datetime(us_rows["Date"])
# us_rows["year_month"] = us_rows["Date"].dt.to_period("M")
# monthly_deaths_us = us_rows.groupby("year_month")["Deaths"].sum().reset_index()
# monthly_deaths_us["year_month"] = monthly_deaths_us["year_month"].dt.to_timestamp()

plt.plot(monthly_deaths_in["year_month"], monthly_deaths_in['Confirmed'], label="India", color="orange")
plt.plot(monthly_deaths_us["year_month"], monthly_deaths_us['Confirmed'], label="USA", color="blue")
plt.xlabel("Months")
plt.ylabel("Confirmed")
plt.legend()
plt.show()
