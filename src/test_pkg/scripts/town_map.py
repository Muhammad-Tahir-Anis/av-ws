import json
import pandas as pd

classes_list = []


def get_classes(key, value):
    if isinstance(value, list):
        for index in value:
            get_classes(key, index)
    else:
        if not [key, list(value)] in classes_list:
            classes_list.append([key, list(value)])


def class_extractor(key, value):
    """
    This function creates list of possible classes which is essential to make MAP model class for creating map
    object for future use
     :param value:
     :param key:
     :return:
    """
    get_classes(key, value)


def class_creator(class_name: str, class_attributes: list):
    # print(class_name, class_attributes)
    # for attribute in class_attributes:
    #     # print(attribute)
    attributes = ','.join(class_attributes)
    attributes = attributes.replace("@", "")
    print(attributes)
    # class_temp = "class {name}:\n\tdef __init__(self,{attributes}):\n\tpass\n\n".format(name=class_name,
    #                                                                                     attributes=attributes)
    with open("town_map/%s.py" % class_name, "a") as python_file:
        for x in python_file:
            print(x)
    #     python_file.write(class_temp)


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
                    class_extractor(key, value[key])
                json_iterator(value[key])
    elif isinstance(value, list):
        for index in value:
            json_iterator(index)
    else:
        pass
        # print(value)


def main():
    # accessing json map data from json file
    with open('json_map.json') as map_data:
        carla_map = json.load(map_data)
        # passing json
        json_iterator(carla_map)
        # displaying classes extracted from json. It is list of 2d lists first index of 2d list is class name and 2nd
        # index is a list of attribute of that class.
        for map_class in classes_list:
            class_creator(class_name=map_class[0], class_attributes=map_class[1])


if __name__ == '__main__':
    main()
