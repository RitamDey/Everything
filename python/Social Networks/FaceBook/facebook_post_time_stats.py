import json
from argparse import ArgumentParser
import dateutil.parser as date_parser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--file',
                        '-f',
                        required=True,
                        help="The JSON File"
                )
    return parser


parser = get_parser()
args = parser.parse_args()
with open(args.file) as f:
    posts = []
    for line in f:
        post = json.loads(line)
        created_time = date_parser.parse(post['created_time'])
        posts.append(created_time.strftime('%H:%M:%S'))
    ones = np.ones(len(posts))
    idx = pd.DatetimeIndex(posts)

    # The actual series (a series of 1s for the moment)
    my_series = pd.Series(ones, index=idx)

    # Resampling into 1-hour bucket
    per_hour = my_series.resample('1H').sum().fillna(0)

    # Plotting
    fig, ax = plt.subplots()
    ax.grid(True)
    ax.set_title("Post Frequency")
    width = 0.8
    ind = np.arange(len(per_hour))
    plt.bar(ind, per_hour)
    tick_pos = ind + width / 2
    labels = []
    for i in range(24):
        d = datetime.now().replace(hour=i, minute=0)
        labels.append(d.strftime('%H:%M'))
    plt.xticks(tick_pos, labels, rotation=90)
    plt.savefig('posts_by_hour.png')
