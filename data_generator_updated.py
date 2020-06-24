import json
import csv
import math
import time
import random
from datetime import datetime, timedelta
from randmac import RandMac
import string
from pprint import pprint

# recordUid: this is ID per row, random unique value should be fine

# recordTimestamp: Unix timestamps in milli seconds

# deviceLocationUpdate.device.deviceId: unique device ID representing every device

# deviceLocationUpdate.visitId: forget this for now

# deviceLocationUpdate.lastSeen: forget this for now

# deviceLocationUpdate.mapId: forget this for now

# deviceLocationUpdate.xPos: assumed x coordinate of the device position from AP device

# deviceLocationUpdate.yPos: assumed y coordinate of the device position from AP device

# deviceLocationUpdate.confidenceFactor: Confidence factor ranging between 0-100. Assuming this is representing the signal strength of the device. Close the device distance wise should have high value


def data_generator(ap_x_origin, ap_y_origin):
    ap_xPos = ap_x_origin
    ap_yPos = ap_y_origin
    response_list = list()
    devices = list()
    last_updated_time_for_mobile_devices = datetime.now()
    # UNIQUE_IDS = (random.sample(range(10000, 999999), 90000))

    for i in range(4):  # adding skimmer devices
        device_details = {}
        device_details['macAddress'] = str(
            RandMac("00:00:00:00:00:00", True)).strip("'")
        device_details['deviceId'] = 'device-' + \
            get_random_alphaNumeric_string()
        device_details['device_type'] = 'skimmer'
        device_details['xPos'] = 21.61853 + random.uniform(10.0, 25.5)
        device_details['yPos'] = 13.60946 + random.uniform(15.0, 35.5)
        devices.append(device_details)

    for i in range(60):  # adding mobile devices
        device_details = {}
        device_details['macAddress'] = str(
            RandMac("00:00:00:00:00:00", True)).strip("'")
        device_details['deviceId'] = 'device-' + \
            get_random_alphaNumeric_string()
        device_details['device_type'] = 'mobile'
        devices.append(device_details)

    for device in devices:
        if (device['device_type'] == 'skimmer'):
            for i in range(10800):
                data = {}
                device_location = {}
                current_datetime = datetime.now()
                incremented_datetime = str(
                    current_datetime + timedelta(seconds=i))
                datatime_object = datetime.strptime(
                    incremented_datetime, '%Y-%m-%d %H:%M:%S.%f')
                data['recordUid'] = 'event-' + \
                    str(round(random.uniform(10000, 999999)))
                data['recordTimeStamp'] = int(
                    datatime_object.timestamp() * 1000)
                data['verboseTime'] = incremented_datetime
                device_location['macAddress'] = device['macAddress']
                device_location['deviceId'] = device['deviceId']
                device_location['xPos'] = device['xPos']
                device_location['yPos'] = device['yPos']
                device_location['distance'] = round(
                    distance(ap_xPos, ap_yPos, device_location['xPos'], device_location['yPos']))
                device_location['confidenceFactor'] = 'to be set'
                device_location['deviceType'] = device['device_type']
                data['deviceLocationUpdate'] = device_location
                response_list.append(data)
        else:
            for i in range(random.choice([600, 900, 1200, 1500, 1800, 2100, 2400])):
                data = {}
                device_location = {}
                current_datetime = last_updated_time_for_mobile_devices
                incremented_datetime = str(
                    current_datetime + timedelta(seconds=i))
                datatime_object = datetime.strptime(
                    incremented_datetime, '%Y-%m-%d %H:%M:%S.%f')
                data['recordUid'] = 'event-' + \
                    str(round(random.uniform(10000, 999999)))
                data['recordTimeStamp'] = int(
                    datatime_object.timestamp() * 1000)
                last_updated_time_for_mobile_devices = datatime_object
                data['verboseTime'] = incremented_datetime
                device_location['macAddress'] = device['macAddress']
                device_location['deviceId'] = device['deviceId']
                device_location['xPos'] = random.uniform(2.99, 175.99)
                device_location['yPos'] = random.uniform(2.99, 155.99)
                device_location['distance'] = round(distance(
                    ap_xPos, ap_yPos, device_location['xPos'], device_location['yPos']))
                device_location['confidenceFactor'] = 'to be set'
                device_location['deviceType'] = device['device_type']
                data['deviceLocationUpdate'] = device_location
                current_datetime = incremented_datetime
                response_list.append(data)

    # for index, unique_id in enumerate(UNIQUE_IDS):
    #     data = {}
    #     device_location = {}
    #     current_datetime = datetime.now()
    #     incremented_datetime = str(current_datetime +
    #                                timedelta(seconds=index))
    #     datatime_object = datetime.strptime(
    #         incremented_datetime, '%Y-%m-%d %H:%M:%S.%f')
    #     data['recordUid'] = 'event-' + str(unique_id)
    #     data['recordTimeStamp'] = int(datatime_object.timestamp() * 1000)
    #     data['verboseTime'] = incremented_datetime
    #     device = random.choice(devices)
    #     if (device['device_type'] == 'skimmer'):
    #         device_location['macAddress'] = device['macAddress']
    #         device_location['deviceId'] = device['deviceId']
    #         device_location['xPos'] = device['xPos']
    #         device_location['yPos'] = device['yPos']
    #         device_location['distance'] = round(distance(
    #             ap_xPos, ap_yPos, device_location['xPos'], device_location['yPos']))
    #         device_location['deviceType'] = device['device_type']
    #         data['deviceLocationUpdate'] = device_location
    #     else:
    #         device_location['macAddress'] = device['macAddress']
    #         device_location['deviceId'] = device['deviceId']
    #         device_location['xPos'] = random.uniform(2.99, 175.99)
    #         device_location['yPos'] = random.uniform(2.99, 155.99)
    #         device_location['distance'] = round(distance(
    #             ap_xPos, ap_yPos, device_location['xPos'], device_location['yPos']))
    #         device_location['deviceType'] = device['device_type']
    #         data['deviceLocationUpdate'] = device_location
    #     response_list.append(data)

    with open('data - ' + str(datetime.now()) + '.csv', 'w',) as csvfile:  # generating csv
        writer = csv.writer(csvfile)
        writer.writerow(["recordUid", "recordTimeStamp", "verboseTime",
                         "macAddress", "deviceId", "deviceType", "xPos", "yPos", "distance", "confidenceFactor"])
        for x in response_list:
            writer.writerow([x['recordUid'], x['recordTimeStamp'], x['verboseTime'], x['deviceLocationUpdate']['macAddress'], x['deviceLocationUpdate']['deviceId'], x['deviceLocationUpdate']['deviceType'],
                             x['deviceLocationUpdate']['xPos'], x['deviceLocationUpdate']['yPos'], x['deviceLocationUpdate']['distance'], x['deviceLocationUpdate']['confidenceFactor']])

    # pprint(response_list)
    print('csv written')


def get_random_alphaNumeric_string(stringLength=13):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)


data_generator(0, 0)  # this is a dummy lat long
