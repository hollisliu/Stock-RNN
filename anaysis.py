import requests
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=2XZ08DFO2AYVOZHD')
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo').json()

data = r['Time Series (Daily)']

close_data = []
for key in data:
    close = data[key]['4. close']
    close_data.append(float(close))

close_data = close_data[4000:]
plt.plot(close_data)
print(close_data)
# derivatives
n = len(close_data)
fhat = np.fft.fft(close_data)
kappa = (2*np.pi/n)*np.arange(-n/2,n/2)
kappa = np.fft.fftshift(kappa)
dfhat = kappa * fhat * (1j)
dfFFT = np.real(np.fft.ifft(dfhat))

# integrate
inte = integrate.cumtrapz(y=dfFFT.real) + close_data[0]
plt.plot(inte)
print(inte)

# x = [close_data[0]]
# for val in dfFFT.real:
#     x.append(val + x[-1])
# plt.plot(x)


plt.show()





# DENOISE below
# # plt.show()
# # dt = 0.001
# # t = np.arange(0,1,dt)
# n = len(close_data)
# fhat = np.fft.fft(close_data, n)
# PSD = fhat * np.conj(fhat) / n
# freq = (1/(100*n)) * np.arange(n)
# # plt.plot(PSD.real)
# # plt.show()
#
# ind = PSD > 1000
# clean = PSD * ind
# fhat = ind * fhat
# res = np.fft.ifft(fhat)
# plt.plot(res.real)
# plt.show()

