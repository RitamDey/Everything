""" Example of using data from Internet in Matplotlib """
import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + \
        stock + '/chartdata;type=quote;range=10y/csv'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Random Graphs from Internet')
    plt.legend()
    plt.show()


graph_data('TSLA')
