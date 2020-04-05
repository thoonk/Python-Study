from matplotlib import pyplot as plt
import pandas as pd

df=pd.read_csv("covid_19_data_southkorea.csv")

column_date = df['ObservationDate'].values.tolist()
column_confirmed = df["Confirmed"].values.tolist()

plt.bar(column_date, column_confirmed, color='blue')
plt.ylim(0, 10500)


plt.xlabel("Date")
plt.ylabel("Confirmed")
plt.title("Corona_South Korea(Confirmed)")


plt.xticks(column_date[: :5], column_date[: :5], rotation=45)

plt.show()

plt.savefig('im/corona_barCharts.png')
plt.gca().clear()
