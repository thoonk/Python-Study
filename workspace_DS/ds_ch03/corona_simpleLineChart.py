from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv("covid_19_data_southkorea.csv")

column_date = df['ObservationDate'].values.tolist()
column_recovered = df['Recovered'].values.tolist()

plt.plot(column_date, column_recovered, color='green', marker='x', linestyle='--')

plt.xlabel("Date")
plt.ylabel("Recovered")
plt.title("Corona_South Korea(Recovered)")

plt.xticks(column_date[: :5], column_date[: :5], rotation=45)

plt.show()

plt.savefig('im/corona_simpleLineChart.png')
plt.gca().clear()
