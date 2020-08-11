from datetime import date, datetime, timedelta
from pprint import pprint
import config
import pandas as pd
import random
from randmac import RandMac
import helper_functions.helper as helper
import string
import math
import csv


def generate():
    print('mobile device generation started')
    devices = []
    start_date = config.START_DATE
    end_date = config.END_DATE
    times = []
    while start_date < end_date:
        delta = timedelta(seconds=int(random.uniform(2, 15)))
        times.append(start_date)
        start_date += delta
    times.append(end_date)

    for i in range(300):  # adding mobile devices
        device_details = {}
        time_span_list = []
        device_details['macAddress'] = str(
            RandMac("00:00:00:00:00:00", True)).strip("'")
        device_details['deviceId'] = 'device-' + \
            helper.get_random_alphaNumeric_string()
        device_details['deviceType'] = 'mobile'
        device_details['repeatCount'] = random.choice([1, 2, 3, 4, 5, 6])
        for _ in range(device_details['repeatCount']):
            start_time = random.choice(times)
            time_delta = random.choice(
                random.sample(range(600, 1800), 1))
            time_span = [str(i) for i in pd.date_range(
                start=start_time, periods=time_delta, freq='S').tolist()]
            time_span_list = time_span_list + time_span
        device_details['timeSpanAlive'] = sorted(time_span_list)
        device_details['startTime'] = device_details['timeSpanAlive'][0]
        device_details['endTime'] = device_details['timeSpanAlive'][-1]
        device_details['recordUid'] = ['event-' +
                                       str(helper.get_random_event_id()) for x in device_details['timeSpanAlive']]
        device_details['recordTimeStamp'] = helper.mobile_device_epoch(
            device_details['timeSpanAlive'])
        device_details['xPos'] = [random.uniform(
            2.99, 175.99) for _ in device_details['timeSpanAlive']]
        device_details['yPos'] = [random.uniform(
            2.99, 175.99) for _ in device_details['timeSpanAlive']]
        device_details['distance'] = helper.mobile_device_distance(
            0, 0, device_details['xPos'], device_details['yPos'])
        device_details['confidenceFactor'] = helper.confidenceFactor(
            device_details['distance'])
        device_details["doesPair"] = False
        device_details['pairingMacAddress'] = "N/A"
        device_details['pairingMacAddressSessionDuration'] = "N/A"
        devices.append(device_details)

    with open(f'./latest_data/mobile-devices' + '.csv', 'w', newline='') as csvfile:
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
    print('mobile device generation successful')


def run():
    generate()
