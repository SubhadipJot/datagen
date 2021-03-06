from datetime import date, datetime, timedelta
import pandas as pd
import os
import glob
import config
import string
import random
import math
import config


def get_random_event_id(stringLength=9):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def get_random_alphaNumeric_string(stringLength=13):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0))


def mobile_device_distance(x1, y1, x2, y2):
    distance_list = []
    for i in range(len(x2)):
        distance_list.append(
            round(math.sqrt(math.pow(x2[i] - x1, 2) + math.pow(y2[i] - y1, 2) * 1.0)))
    return distance_list


def confidenceFactor(distance):
    return list(map(lambda x: round((100 - ((x / 235) * 100))), distance))


def mobile_device_epoch(time_span):
    epoch_list = []
    for t in time_span:
        dt = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
        epoch_list.append(int(dt.timestamp() * 1000))
    return epoch_list


def datetime_range(start, end, delta):
    current = start
    if not isinstance(delta, timedelta):
        delta = timedelta(**delta)
    while current < end:
        yield current
        current += delta


def getTimeList(period):
    index_to_pop = set()
    start = config.START_DATE
    end = config.END_DATE
    date_list = []
    new_date_list = []
    for dt in datetime_range(start, end, {'hours': period}):
        date_list.append(dt)
    for date in date_list:
        new_date_list = new_date_list + pd.date_range(start=date,
                                                      end=(date + timedelta(minutes=random.choice(range(5, 30)))), freq='S').tolist()
    for i in range(int(len(new_date_list)/0.8)):
        index_to_pop.add(random.randrange(len(new_date_list)))
    timestamps_to_remove = [new_date_list[index] for index in index_to_pop]
    final_time_list = [
        timestamp for timestamp in new_date_list if timestamp not in timestamps_to_remove]
    return final_time_list


def generate_final_csv():
    os.chdir("./latest_data")
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.to_csv("final_data.csv", index=False, encoding='utf-8-sig')
    # df = pd.read_csv("combined_csv.csv", low_memory=False)
    # df.sort_values(by='verboseTime')
    # df.to_csv("final_data_2.csv", index=False, encoding='utf-8-sig')
