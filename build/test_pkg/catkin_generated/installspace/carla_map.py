import json

from typing import List

class_list_check: List[str] = []
class_list = []

attribute_list = []


def main():
    with open('json_map.json') as map_data:
        # carla_map = json.load(map_data, object_hook=lambda d: SimpleNamespace(**d))
        carla_map = json.load(map_data)
        json_iterator(carla_map)
        for classes in class_list_check:
            print(classes)
        for attribute in attribute_list:
            print(attribute)


def attributes(value):
    print(value)
    print(list(value))
    if not str(list(value)) in attribute_list:
        attribute_list.append(str(list(value)))


def class_creator(name, value):
    """
    This function creates list of possible classes which is essential to make TOW-MAP model class for creating map
    object for future use
     :param value:
     :param name: :return:
    """
    if not str(name) in class_list_check:
        class_list_check.append(str(name))
        attributes(value)

        # class_list.append(type(name, (), attribute_list))
        # with open("%s.py"%name, "w") as python_file:
        #     class_temp = "class {name}:\n\def __init__(self,{attributes})"


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
                # print(key)  # At this point we got keys of json.

                # This if condition checks that the key should not have the value of type string or none to make
                # relevant classes
                if not isinstance(value[key], (str, type(None))):
                    class_creator(key, value)
                json_iterator(value[key])
    elif isinstance(value, list):
        for index in value:
            json_iterator(index)
    else:
        pass
        # print(value)


if __name__ == '__main__':
    main()
