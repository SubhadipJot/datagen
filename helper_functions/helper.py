from datetime import date, datetime, timedelta
import pandas as pd
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


def confidenceFactor(distance):
    return list(map(lambda x: round((100 - ((x / 235) * 100))), distance))


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
