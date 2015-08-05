import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

days, messages = np.loadtxt("ankit_count.csv", unpack=True,
        converters={ 0: mdates.strpdate2num('%d/%m/%Y')})
days2, messages2 = np.loadtxt("ayush_count.csv", unpack=True,
        converters={ 0: mdates.strpdate2num('%d/%m/%Y')})

plt.xlabel('Date')
plt.ylabel('Message Count')
plt.plot_date(x=days, y=messages,color='m',label='Me',linestyle=':')
plt.plot_date(x=days2, y=messages2,color='c',label='Friend',linestyle='-.')
plt.legend()
plt.show()