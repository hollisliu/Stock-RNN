import requests
import pandas as pd
from datetime import datetime
from datetime import timezone
import numpy as np

today = str(int(datetime(2021, 2, 24, hour=0, minute=0, second=0, tzinfo=timezone.utc).timestamp()))
#GJ 000596
#HQ 002697
#url = 'http://quotes.money.163.com/klinederc/service/chddata.html?code=1000596&start=20101105&end=20210219&fields=TCLOSE;VOTURNOVER'
url = 'https://query1.finance.yahoo.com/v7/finance/download/000596.SZ?period1=1266710400&period2='+today+'&interval=1d&events=history&includeAdjustedClose=true'

data = pd.read_csv(url)
data = data.drop(['Date','Close'], axis=1)
tomorrow = np.roll(data['Adj Close'].values,-1)
data.insert(5, "tomorrow", tomorrow, True)
data.drop(data.tail(1).index,inplace=True)

# data = data.set_axis(['date', '5. adjusted close', '6. volume'], axis=1)
# data = data.set_index('date')
# data['5. adjusted close'] = data['5. adjusted close'].astype(float)
# data['6. volume'] = data['6. volume'].astype(float)
# data = data.iloc[::-1]
#data.to_pickle("./ml/GJD_full.pkl")
data.to_csv("../ml/GJD.csv",index=False)