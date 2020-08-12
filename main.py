import type1_skimmer_datagen as type1skimmer
import type2_skimmer_datagen as type2skimmer
import type3_skimmer_datagen as type3skimmer
import mobile_devices_datagen as mobile_devices
import helper_functions.helper as helper
import sys
import random


if __name__ == '__main__':
    arg_list = sys.argv[1:]
    if ("1" in arg_list):
        type1skimmer.run()
    if ("2" in arg_list):
        type2skimmer.run()
    if ("3" in arg_list):
        type3skimmer.run()
    if ("0" in arg_list):
        mobile_devices.run()
    if ("all" in arg_list):
        type1skimmer.run()
        type2skimmer.run()
        type3skimmer.run()
        mobile_devices.run()
    if("gen" in arg_list):
        helper.generate_final_csv()
