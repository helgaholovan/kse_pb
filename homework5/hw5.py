import requests
import pandas


response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 50.4501,
    'lng': 30.5234,
    'params': ','.join(['windSpeed', 'airTemperature']),
  },
  headers={
    'Authorization': '4716190c-4c49-11f0-89da-0242ac130006-4716198e-4c49-11f0-89da-0242ac130006'
  }
)
json_data = response.json()

import pandas as pd
import datetime

def format(tim):
    dt = datetime.datetime.fromisoformat(tim.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%d %H:%M")
df = pd.DataFrame(json_data['hours'])
df["time"] = df["time"].apply(format)

df["windSpeed"] = df["windSpeed"].apply(lambda x: x["noaa"])
df["airTemperature"] = df["airTemperature"].apply(lambda x: x["noaa"])

MaxTemp = max(df["airTemperature"])
MinTemp = min(df["airTemperature"])
AvTemp = sum(df["airTemperature"])/len(df["airTemperature"])
AvWind = sum(df["windSpeed"])/len(df["windSpeed"])
MaxWind = max(df["windSpeed"])
ss = AvWind-MaxTemp

display(df)
print(f" Максимальна температура - {MaxTemp}, мінімальна - {MinTemp}, середня - {AvTemp}. Якесь завдання з вітром - {ss}")