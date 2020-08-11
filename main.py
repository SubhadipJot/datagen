import type1_skimmer_datagen as type1skimmer
import type2_skimmer_datagen as type2skimmer
import type3_skimmer_datagen as type3skimmer
import mobile_devices_datagen as mobile_devices
import sys
import random


if __name__ == '__main__':
    arg_list = sys.argv[1:]
    if ("type1" in arg_list):
        type1skimmer.run()
    if ("type2" in arg_list):
        type2skimmer.run()
    if ("type3" in arg_list):
        type3skimmer.run()
    if ("mobile" in arg_list):
        mobile_devices.run()
