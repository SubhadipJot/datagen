import json
import csv
import math
import time
import random
import chalk
import pandas as pd
import multiprocessing
import concurrent.futures
from datetime import datetime, timedelta, date
from dateutil.parser import parse
from randmac import RandMac
import string
import config
from pprint import pprint

date_list = pd.date_range(start=config.START_DATE,
                          end=config.END_DATE, freq='S').tolist()

date_start_index = random.choice(random.sample(range(0, len(date_list)), 1))
date_end_index = random.choice(random.sample(
    range(date_start_index, len(date_list)), 1))

start_date = date_list[date_start_index]
end_date = date_list[date_end_index]

new_date_range = pd.date_range(
    start=start_date, end=end_date, freq='S').tolist()

devices = list()


# default 1 skimmer will be generated if no value is passed
def generate_skimmers_type1(skimmer_count,
                            # range is set randomly in config.py between 3 - 300 metres
                            skimmer_distance_range,
                            # if true this will override the distance function and assign random values between 3 - 300 metres, xPos and yPos not be calculated
                            # if false distance will be calculated based on the xPos and yPos
                            skimmer_has_user_defined_distance,
                            session_duration,
                            session_count,
                            skimmer_does_pair,
                            skimmer_pairing_macaddress_session_duration):
    if (session_duration == 24):
        print(chalk.green('Generating Type-1 Skimmers!'))
        for _ in range(skimmer_count):
            device_details = {}
            time_span = [i.to_pydatetime() for i in date_list]
            xPos = float(0 + random.uniform(10.0, 25.5))
            yPos = float(0 + random.uniform(10.0, 35.5))
            device_details['deviceType'] = 'skimmer'
            device_details['sessionDurationInHours'] = session_duration
            device_details['sessionDurationInSeconds'] = session_duration * 60 * 60
            device_details['timeSpanAlive'] = [str(i) for i in time_span]
            device_details['recordUid'] = [
                'event-' + str(get_random_event_id()) for x in time_span]
            device_details['recordTimeStamp'] = [
                (x.timestamp()*1000) for x in time_span]
            date_start_index = random.choice(
                random.sample(range(0, len(date_list)), 1))
            date_end_index = random.choice(random.sample(
                range(date_start_index, len(date_list)), 1))
            device_details['macAddress'] = str(
                RandMac("00:00:00:00:00:00", True)).strip("'")
            device_details['deviceId'] = 'device-' + \
                get_random_alphaNumeric_string()
            device_details['xPos'] = [xPos for _ in date_list]
            device_details['yPos'] = [yPos for _ in date_list]
            if skimmer_has_user_defined_distance:
                device_details['distance'] = [
                    skimmer_distance_range[_] for x in date_list]
            else:
                device_details['distance'] = [
                    distance(0, 0, xPos, yPos) for _ in date_list]
            device_details['confidenceFactor'] = confidenceFactor(
                device_details['distance'])
            device_details['sessions'] = session_count
            device_details['doesPair'] = skimmer_does_pair
            if skimmer_does_pair:
                device_details['pairingMacAddress'] = str(
                    RandMac("00:00:00:00:00:00", True)).strip("'")
                device_details['pairingMacAddressSessionDuration'] = skimmer_pairing_macaddress_session_duration
            else:
                device_details['pairingMacAddress'] = 'N/A'
                device_details['pairingMacAddressSessionDuration'] = 'N/A'
            devices.append(device_details)
        # pprint(devices)
    else:
        print(chalk.red(
            'TYPE-1 skimmer generation terminated! Please set TYPE1_SKIMMER_SESSION_DURATION to 24 in the config file '))


# def generate_data():
#     print('-----------------')
#     for device in devices:
#         device['distance'] = distance(0, 0, device['xPos'], device['yPos'])
#         device['confidenceFactor'] =

def get_random_event_id(stringLength=9):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def get_random_alphaNumeric_string(stringLength=13):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0))


def confidenceFactor(distance):
    return list(map(lambda x: round((100 - ((x/235) * 100))), distance))


def generate_csv():
    # generating csv
    print(chalk.green('CSV Generation in process'))
    with open(f'./latest_data/data-{datetime.now()} - final_data' + '.csv', 'w',) as csvfile:
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


if (__name__ == '__main__'):
    green = chalk.Chalk('green')
    bold_green = green + chalk.utils.FontFormat('bold')

    start_time = time.perf_counter()
    print(bold_green(f'Operation started -- Please Wait'))
    generate_skimmers_type1(config.TYPE1_SKIMMER_COUNT,
                            config.TYPE1_SKIMMER_DISTANCE_RANGE,
                            config.TYPE1_SKIMMER_HAS_USER_DEFINED_DISTANCE,
                            config.TYPE1_SKIMMER_SESSION_DURATION,
                            config.TYPE1_SKIMMER_SESSION_COUNT,
                            config.TYPE1_SKIMMER_DOES_PAIR,
                            config.TYPE1_SKIMMER_PAIRING_MACADDRESS_SESSION_DURATION)
    # generate_data()
    generate_csv()
    end_time = time.perf_counter()
    print(bold_green(
        f'Opeartion finished in {end_time - start_time} seconds'))
