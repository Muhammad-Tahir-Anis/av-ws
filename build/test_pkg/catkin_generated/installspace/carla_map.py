import json
import pandas as pd
from pandas import json_normalize
from types import SimpleNamespace


def main():
    with open('json_map') as map_data:
        carla_map = json.load(map_data, object_hook=lambda d: SimpleNamespace(**d))

    for data in carla_map.OpenDRIVE.road:
        print(data.type)

    # key_list_main: list = []
    # key_list: list = []
    # value = carla_map
    # list(value.keys())
    # # for key in value.keys():
    # # print(key)
    # # while value.keys():
    # print(value.keys())
    # for key in value.keys():
    #     print(key)
    #     key_list.append(key)
    #     # value = value[key]
    #     # print(value)
    # key_list_main.append(key_list)
    # print(key_list)
    # print(key_list_main)
    # value = value[value.keys()]
    # key_list = []
    # for key in carla_map.keys():
    #     key_list.append(key)
    # key_list_main.append(key_list)
    # print(value.keys())

    # print(key_list)


if __name__ == '__main__':
    main()
