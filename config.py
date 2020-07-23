import random

START_DATE = "2020/7/7"
END_DATE = "2020/7/8"

MOBILE_DEVICE_COUNT = 300
SKIMMER_DISTANCE_RANGE = 3  # units in metres, from Access Point

#########################
# TYPE 1 skimmer config #
#########################

TYPE1_SKIMMER_COUNT = 3
# distance in metres, can range between 3 - 300
TYPE1_SKIMMER_DISTANCE_RANGE = random.sample(
    range(3, 300), TYPE1_SKIMMER_COUNT)
# set user defined distance
TYPE1_SKIMMER_HAS_USER_DEFINED_DISTANCE = True
# units in hours, available for 24 hours
TYPE1_SKIMMER_SESSION_DURATION = 24
# session count must be 1 as it's avaialble 24*7
TYPE1_SKIMMER_SESSION_COUNT = 1
# if pairs with another device for data transfer, must be false for type-1 skimmers, but can be toggled for testing. Session count will be set to 1,
# irrespective of the value set here if TYPE1_SKIMMER_SESSION_DURATION value is 24
TYPE1_SKIMMER_DOES_PAIR = False
# if TYPE1_SKIMMER_DOES_PAIR is True set duration, else set 0
TYPE1_SKIMMER_PAIRING_MACADDRESS_SESSION_DURATION = 0

#########################
# TYPE 1 skimmer config #
#########################


#########################
# TYPE 2 skimmer config #
#########################
TYPE2_SKIMMER_COUNT = 3
# distance in metres, can range between 3 - 300
TYPE2_SKIMMER_DISTANCE_RANGE = 3
# units in hours, available intermittently
TYPE2_SKIMMER_SESSION_DURATION = 22
# session count must be 1 as it's avaialble 24*7
TYPE2_SKIMMER_SESSION_COUNT = 1
# if pairs with another device for data transfer, must be false for type-1 skimmers, but can be toggled for testing. Session count will be set to 1,
# irrespective of the value set here if TYPE2_SKIMMER_SESSION_DURATION value is 24
TYPE2_SKIMMER_DOES_PAIR = False
# if TYPE2_SKIMMER_DOES_PAIR is True set duration, else set 0
TYPE2_SKIMMER_PAIRING_MACADDRESS_SESSION_DURATION = 0
#########################
# TYPE 1 skimmer config #
#########################
