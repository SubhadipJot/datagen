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
    devices = []
    start_date = config.START_DATE
    end_date = config.END_DATE
    times = []
    while start_date < end_date:
        delta = timedelta(seconds=int(random.uniform(2, 5)))
        times.append(start_date)
        start_date += delta
    times.append(end_date)

    for _ in range(config.TYPE1_SKIMMER_COUNT):
        device_details = {}
        time_span = [i for i in times]
        xPos = float(0 + random.uniform(10.0, 25.5))
        yPos = float(0 + random.uniform(10.0, 35.5))
        device_details['deviceType'] = '1'
        # device_details['sessionDurationInHours'] = session_duration
        # device_details['sessionDurationInSeconds'] = session_duration * 60 * 60
        device_details['timeSpanAlive'] = [str(i) for i in time_span]
        device_details['recordUid'] = [
            'event-' + str(helper.get_random_event_id()) for x in time_span]
        device_details['recordTimeStamp'] = [
            (x.timestamp()*1000) for x in time_span]
        device_details['macAddress'] = str(
            RandMac("00:00:00:00:00:00", True)).strip("'")
        device_details['deviceId'] = 'device-' + \
            helper.get_random_alphaNumeric_string()
        device_details['xPos'] = [
            (xPos)+random.uniform(0.0, 2.0) for _ in time_span]
        device_details['yPos'] = [
            (yPos)+random.uniform(0.0, 2.0) for _ in time_span]
        device_details['distance'] = helper.mobile_device_distance(
            0, 0, device_details['xPos'], device_details['yPos'])
        device_details['confidenceFactor'] = helper.confidenceFactor(
            device_details['distance'])
        # device_details['sessions'] = session_count
        device_details['doesPair'] = False
        device_details['pairingMacAddress'] = 'N/A'
        device_details['pairingMacAddressSessionDuration'] = 'N/A'
        devices.append(device_details)

    with open(f'./latest_data/latest-type1' + '.csv', 'w', newline='') as csvfile:
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
    print('type1 skimmer generation successful')


def run():
    generate()
