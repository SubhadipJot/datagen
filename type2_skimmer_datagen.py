from datetime import date, datetime, timedelta
from pprint import pprint
import pandas as pd
import random
from randmac import RandMac
import helper_functions.helper as helper
import string
import math
import csv

devices = []


# def datetime_range(start, end, delta):
#     current = start
#     if not isinstance(delta, timedelta):
#         delta = timedelta(**delta)
#     while current < end:
#         yield current
#         current += delta


# def getTimeList(period):
#     index_to_pop = set()
#     start = datetime(2020, 1, 1)
#     end = datetime(2020, 1, 3)
#     date_list = []
#     new_date_list = []
#     for dt in datetime_range(start, end, {'hours': period}):
#         date_list.append(dt)
#     for date in date_list:
#         new_date_list = new_date_list + pd.date_range(start=date,
#                                                       end=(date + timedelta(minutes=random.choice(range(5, 30)))), freq='S').tolist()
#     for i in range(int(len(new_date_list)/0.8)):
#         index_to_pop.add(random.randrange(len(new_date_list)))
#     timestamps_to_remove = [new_date_list[index] for index in index_to_pop]
#     final_time_list = [
#         timestamp for timestamp in new_date_list if timestamp not in timestamps_to_remove]
#     return final_time_list


def generate():

    print("generating type 2 skimmers")

    for i in range(3):
        device_details = {}
        time_span = [i.to_pydatetime() for i in (helper.getTimeList(
            int((i + 1) * 2)) if (i < 2) else helper.getTimeList(1))]
        xPos = float(0 + random.uniform(10.0, 25.5))
        yPos = float(0 + random.uniform(10.0, 35.5))
        device_details['deviceType'] = 'skimmer'
        device_details['timeSpanAlive'] = [str(i) for i in time_span]
        device_details['recordUid'] = [
            'event-' + str(helper.get_random_event_id()) for x in time_span]
        device_details['recordTimeStamp'] = [
            (x.timestamp() * 1000) for x in time_span]
        device_details['macAddress'] = str(
            RandMac("00:00:00:00:00:00", True)).strip("'")
        device_details['deviceId'] = 'device-' + \
            helper.get_random_alphaNumeric_string()
        device_details['xPos'] = [xPos for _ in time_span]
        device_details['yPos'] = [yPos for _ in time_span]
        device_details['distance'] = [
            helper.distance(0, 0, xPos, yPos) for _ in time_span]
        device_details['confidenceFactor'] = helper.confidenceFactor(
            device_details['distance'])
        device_details['doesPair'] = 'False'
        device_details['pairingMacAddress'] = 'N/A'
        device_details['pairingMacAddressSessionDuration'] = 'N/A'
        devices.append(device_details)

    with open(f'./latest_data/{datetime.now()}-type2' + '.csv', 'w',) as csvfile:
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

    print("type 2 skimmer generation successful")


def run():
    generate()
