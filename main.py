import type2_skimmer_datagen as type2skimmer
import sys
import random


if __name__ == '__main__':
    arg_list = sys.argv[1:]
    if ("type1" in arg_list):
        print('type1 called')
    if ("type2" in arg_list):
        type2skimmer.run()
