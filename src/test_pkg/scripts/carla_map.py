import json

from typing import List

class_list_check: List[str] = []
class_list = []


def main():
    with open('json_map.json') as map_data:
        # carla_map = json.load(map_data, object_hook=lambda d: SimpleNamespace(**d))
        carla_map = json.load(map_data)
        json_iterator(carla_map)
        for classes in class_list:
            print(classes)


def class_creator(name):
    """
    This function creates list of possible classes which is essential to make TOW-MAP model class for creating map
    object for future use
     :param name: :return:
    """
    if not str(name) in class_list_check:
        class_list_check.append(str(name))
        class_list.append(type(name, (), {}))


def json_iterator(value):
    """
    This iterator traverse json dictionary branch by branch.
    It will not go to another branch until current branch will be traversed completely
    :param value: json dict
    :return:
    """
    keys_list = []
    if isinstance(value, dict):
        if value.keys():
            for key in value.keys():
                keys_list.append(key)
                print(key)  # At this point we got keys of json.

                # This if condition checks that the key should not have the value of type string or none to make
                # relevant classes
                if not isinstance(value[key], (str, type(None))):
                    class_creator(key)
                json_iterator(value[key])
    elif isinstance(value, list):
        for index in value:
            json_iterator(index)
    else:
        print(value)


if __name__ == '__main__':
    main()
