import requests
import pandas as pd


#data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo').json()
data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=2XZ08DFO2AYVOZHD').json()

df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df['5. adjusted close'] = df['5. adjusted close'].astype(float)
df['6. volume'] = df['6. volume'].astype(float)
df = df.iloc[::-1]
df.to_pickle("./daily/AAPL_full.pkl")