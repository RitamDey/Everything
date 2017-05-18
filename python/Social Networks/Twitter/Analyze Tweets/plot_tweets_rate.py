from sys import argv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from numpy import ones
from make_client import make_client


def main():
    try:
        file_name = argv[1]
    except IndexError:
        file_name = "tweets.json"

    all_dates = []
    client = make_client()
    for line in client.user_timeline("republic", count=10):
        tweet = line._json
        all_dates.append(tweet.get('created_at'))

    idx = pd.DatetimeIndex(all_dates)
    ones_array = ones(len(all_dates))

    # the actual series (at series of 1s for the moment)
    my_series = pd.Series(ones_array, index=idx)

    # Resampling / bucketing into 1-minute buckets
    per_minute = my_series.resample('1Min').sum().fillna(0)

    # Plotting the series
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.set_title("Tweet Frequencies")

    hours = mdates.MinuteLocator(interval=20)
    hours.MAXTICKS = 52643
    date_formatter = mdates.DateFormatter("%H:%M")

    datemin = datetime(2015, 10, 31, 15, 0)
    datemax = datetime(2017, 10, 31, 18, 0)

    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(date_formatter)

    ax.set_xlim(datemin, datemax)
    max_freq = per_minute.max()
    ax.set_ylim(0, max_freq)
    ax.plot(per_minute.index, per_minute)

    plt.savefig('tweets_rate.png')


if __name__ == '__main__':
    main()
