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

devices = []


def daterange(start_date, end_date, delta):
    delta = timedelta(hours=delta)
    while start_date < end_date:
        yield start_date
        start_date += delta
    return delta


def getTimeList(delta):
    datetimelist = []
    for i in daterange(config.START_DATE, config.END_DATE, delta):
        datetimelist = datetimelist + (pd.date_range(
            start=i, periods=int(random.uniform(10, 90)), freq='S').tolist())
    return datetimelist


def generate_pairing_mobile_device(mobile_macaddress, ap_macadress, times):
    delta = random.uniform(2, 10)
    times = times
    device_details = {}
    time_span = [i for i in times]
    xPos = float(0 + random.uniform(11.5, 25.5))
    yPos = float(0 + random.uniform(11.5, 35.5))
    device_details['deviceType'] = '0'
    device_details['timeSpanAlive'] = [str(i) for i in time_span]
    device_details['recordUid'] = [
        'event-' + str(helper.get_random_event_id()) for x in time_span]
    device_details['recordTimeStamp'] = [
        (x.timestamp()*1000) for x in time_span]
    device_details['macAddress'] = mobile_macaddress
    device_details['deviceId'] = 'device-' + \
        helper.get_random_alphaNumeric_string()
    device_details['xPos'] = [(xPos)+random.uniform(0.0, 80.0)
                              for _ in time_span]
    device_details['yPos'] = [
        (yPos)+random.uniform(0.0, 80.0) for _ in time_span]
    device_details['distance'] = helper.mobile_device_distance(
        0, 0, device_details['xPos'], device_details['yPos'])
    device_details['confidenceFactor'] = helper.confidenceFactor(
        device_details['distance'])
    # device_details['sessions'] = session_count
    device_details['doesPair'] = True
    device_details['pairingMacAddress'] = ap_macadress
    device_details['pairingMacAddressSessionDuration'] = 'N/A'
    devices.append(device_details)


def generate():
    for _ in range(3):
        delta = random.uniform(2, 10)
        times = getTimeList(delta)
        device_details = {}
        time_span = [i for i in times]
        xPos = float(0 + random.uniform(10.0, 25.5))
        yPos = float(0 + random.uniform(10.0, 35.5))
        device_details['deviceType'] = '3'
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
        device_details['doesPair'] = True
        device_details['pairingMacAddress'] = str(
            RandMac("00:00:00:00:00:00", True)).strip("'")
        device_details['pairingMacAddressSessionDuration'] = 'N/A'
        devices.append(device_details)
        generate_pairing_mobile_device(
            device_details['pairingMacAddress'], device_details['macAddress'], times)

    with open(f'./latest_data/latest-type3' + '.csv', 'w', newline='') as csvfile:
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
    print('type3 skimmer generation successful')


def run():
    generate()
