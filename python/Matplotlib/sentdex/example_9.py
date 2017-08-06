""" Example of basic customization and rotating labels in Matplotlib """
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def bytespdate2num(format, encoding='utf-8'):
    strcoverter = mdates.strpdate2num(format)

    def bytescoverter(b):
        s = b.decode(encoding)
        return strcoverter(s)

    return bytescoverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + \
        stock + '/chartdata;type=quote;range=10y/csv'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(split_line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(
        stock_data,
        delimiter=',',
        unpack=True,
        # converters is a tuple where the first element
        # is the position of element and the last is the callback
        converters=(0, bytespdate2num('%Y%m%d'))
    )

    ax1.plot_date(date, closep)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Random Graphs from Internet')
    plt.legend()
    plt.show()


graph_data('TSLA')
