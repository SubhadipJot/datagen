from datetime import date, datetime, timedelta
from pprint import pprint
import pandas as pd
import random
from randmac import RandMac
import string
import math
import csv

devices = []


def datetime_range(start, end, delta):
    current = start
    if not isinstance(delta, timedelta):
        delta = timedelta(**delta)
    while current < end:
        yield current
        current += delta


def getTimeList(period):
    start = datetime(2020, 1, 1)
    end = datetime(2020, 1, 3)
    date_list = []
    new_date_list = []
    # this unlocks the following interface:
    for dt in datetime_range(start, end, {'hours': period}):
        date_list.append(dt)
    for date in date_list:
        new_date_list = new_date_list + pd.date_range(start=date,
                                                      end=(date + timedelta(minutes=random.choice(range(5, 30)))), freq='S').tolist()
    return new_date_list


def get_random_event_id(stringLength=9):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0))


def confidenceFactor(distance):
    return list(map(lambda x: round((100 - ((x / 235) * 100))), distance))


def get_random_alphaNumeric_string(stringLength=13):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


for i in range(3):
    device_details = {}
    time_span = [i.to_pydatetime() for i in (getTimeList(
        int((i+1) * 2)) if (i < 2) else getTimeList(1))]
    xPos = float(0 + random.uniform(10.0, 25.5))
    yPos = float(0 + random.uniform(10.0, 35.5))
    device_details['deviceType'] = 'skimmer'
    device_details['timeSpanAlive'] = [str(i) for i in time_span]
    device_details['recordUid'] = [
        'event-' + str(get_random_event_id()) for x in time_span]
    device_details['recordTimeStamp'] = [
        (x.timestamp() * 1000) for x in time_span]
    device_details['macAddress'] = str(
        RandMac("00:00:00:00:00:00", True)).strip("'")
    device_details['deviceId'] = 'device-' + get_random_alphaNumeric_string()
    device_details['xPos'] = [xPos for _ in time_span]
    device_details['yPos'] = [yPos for _ in time_span]
    device_details['distance'] = [
        distance(0, 0, xPos, yPos) for _ in time_span]
    device_details['confidenceFactor'] = confidenceFactor(
        device_details['distance'])
    device_details['doesPair'] = 'False'
    device_details['pairingMacAddress'] = 'N/A'
    device_details['pairingMacAddressSessionDuration'] = 'N/A'
    devices.append(device_details)


with open(f'./latest_data/monthly_data/test-3' + '.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["recordUid", "recordTimeStamp", "verboseTime",
                     "macAddress", "deviceId", "deviceType", "doesPair", "pairingMacAddress", "pairingMacAddressSessionDuration", "xPos", "yPos", "distance", "confidenceFactor"])
    for device in devices:
        for index in range(len(device['recordUid'])):
            writer.writerow([device['recordUid'][index],
                             device['recordTimeStamp'][index],
                             device['timeSpanAlive'][index],
                             device['macAddress'],
                             device['deviceId'],
                             device['deviceType'],
                             device["doesPair"],
                             device['pairingMacAddress'],
                             device['pairingMacAddressSessionDuration'],
                             device['xPos'][index],
                             device['yPos'][index],
                             device['distance'][index],
                             device['confidenceFactor'][index]])


pprint(devices)
