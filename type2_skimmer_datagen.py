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

    with open(f'./latest_data/latest-type2' + '.csv', 'w', newline='') as csvfile:
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
