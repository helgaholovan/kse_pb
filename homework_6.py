import requests
import pandas as pd


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

df = pd.DataFrame(data['Weekly Time Series'])
df = pd.DataFrame.from_dict(data['Weekly Time Series'], orient='index')

df['MA20'] = df['4. close'].rolling(window=10).mean()
df['MA50'] = df['4. close'].rolling(window=50).mean()


df[['MA20', 'MA50']].plot(figsize=(10, 6))

df['Signal'] = "Hold"
for i in range(len(df)):
    prev_ma20 = df['MA20'].iloc[i-1]
    prev_ma50 = df['MA50'].iloc[i-1]
    curr_ma20 = df['MA20'].iloc[i]
    curr_ma50 = df['MA50'].iloc[i]
    if prev_ma20 < prev_ma50 and curr_ma20 > curr_ma50:
       df.loc[df.index[i], 'Signal'] = "Buy"
    elif prev_ma20 > prev_ma50 and curr_ma20 < curr_ma50:
       df.loc[df.index[i], 'Signal'] = "Sell"
Budget = {"Income":0, "Amount":0, "Costs":0}
for i in range(len(df)):
  signal = df['Signal'].iloc[i]
  price_sell = float(df['4. close'].iloc[i])
  price_buy = float(df['1. open'].iloc[i])
  if signal == "Buy":
    Budget['Costs'] += price_buy
    Budget['Amount'] += 1
  elif signal == "Sell" and Budget['Amount'] !=0:
    Budget['Income'] += price_sell
    Budget['Amount'] -= 1
Budget['Income'] = "%.2f" % Budget['Income']
Budget['Costs'] = "%.2f" % Budget['Costs']
Profit = "%.2f" % (float(Budget['Income']) - float(Budget['Costs']))
print(f"Наразі ми маємо {Budget['Amount']} акцій, ми витратили {Budget['Costs']} та отримали {Budget['Income']}. Наш прибуток/втрати - ({Profit})")