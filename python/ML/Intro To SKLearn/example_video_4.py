import pandas as pd
import os
import time
from datetime import datetime


path = "intraQuarter/intraQuarter/"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path +'_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    for each_dir in stock_list[1:]:
        # First element is the directory name we are walking
        each_file = os.listdir(each_dir)
        if len(each_file) > 0:
            for data_file in each_file:
                date_stamp = datetime.strptime(data_file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir + '/' + data_file
                source = open(full_file_path, 'r').read()

