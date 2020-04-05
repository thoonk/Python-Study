from matplotlib import pyplot as plt
import pandas as pd
import math

df=pd.read_csv("covid_19_data_southkorea.csv")

column_confirmed = df["Confirmed"].values.tolist()
column_deaths = df['Deaths'].values.tolist()
column_recovered = df['Recovered'].values.tolist()

sum_confirmed = sum(column_confirmed)
sum_deaths = sum(column_deaths)
sum_recovered = sum(column_recovered)

rate_deaths = round((sum_deaths/sum_confirmed) * 100, 1)
rate_recovered = round((sum_recovered/sum_confirmed) * 100, 1)

plt.pie([rate_deaths, rate_recovered, 100-(rate_deaths+rate_recovered)],
        startangle=180,
        counterclock=False,
        autopct='%1.1f%%',
        pctdistance=0.5,
        colors=['red', 'green', 'blue'])
labels = ["Deaths", "Recovered", "Remainder"]
plt.legend(labels)
plt.title("Corona_SouthKorea")
plt.axis("equal")
#plt.show()

plt.savefig('im/corona_pieCharts.png')
plt.gca().clear()











