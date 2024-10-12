# India Vs USA Covid deaths by month in 2020
# India Vs China Covid deaths by month in 2020

import json
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("full_grouped.csv")

df['Date'] = pd.to_datetime(df['Date'])
india_rows = df[df["Country/Region"] == "India"]
# deaths_india = india_rows.groupby("Date")["Deaths"].sum()
india_rows["Date"] = pd.to_datetime(india_rows["Date"])

india_rows["year_month"] = india_rows["Date"].dt.to_period("M")
monthly_deaths_in = india_rows.groupby("year_month")['Deaths'].sum().reset_index()
monthly_deaths_in["year_month"] = monthly_deaths_in["year_month"].dt.to_timestamp()
# print(monthly_deaths)

us_rows = df[df["Country/Region"] == "US"]
us_rows["Date"] = pd.to_datetime(us_rows["Date"])
us_rows["year_month"] = us_rows["Date"].dt.to_period("M")
monthly_deaths_us = us_rows.groupby("year_month")["Deaths"].sum().reset_index()
monthly_deaths_us["year_month"] = monthly_deaths_us["year_month"].dt.to_timestamp()

plt.plot(monthly_deaths_in["year_month"], monthly_deaths_in['Deaths'], label="India", color="orange")
plt.plot(monthly_deaths_us["year_month"], monthly_deaths_us['Deaths'], label="USA", color="blue")
plt.xlabel("Months")
plt.ylabel("Deaths")
plt.legend()
plt.show()
# def Get_Deaths(year,country,df):
#     {
# 
# }