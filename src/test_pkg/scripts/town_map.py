import json
import keyword
import os
import pandas as pd


class TownMap:
    def __init__(self):
        print("Town map initialized")

    # It is list of 2d lists first index of 2d list is class name and 2nd index
    # is a list of attribute of that class.
    classes_list = []

    @classmethod
    def extract_class(cls, key, value):
        """
        This method gets names and attributes of class from key and value coming from json data and store into a list.
        This function creates list of possible classes which is essential to make MAP model class for creating map
        object for future use
         :param value:
         :param key:
         :return:
        """
        if isinstance(value, list):
            for index in value:
                cls.extract_class(key, index)
        else:
            if not [key, list(value)] in cls.classes_list:
                # ----------- Special Block Started------------
                # This special block is restricting duplication of Keys with different values.
                # if multiple same keys have different values than it merges them into one
                # if you want to make them separate just comment special block
                # and uncomment the line just after the end of special block
                if len(cls.classes_list):
                    is_key: bool = False
                    for list_index in cls.classes_list:
                        if list_index[0] is key:
                            is_key = True
                            index = cls.classes_list.index([key, list_index[1]])
                            cls.classes_list[index] = [list_index[0], list(set(list_index[1] + list(value)))]
                    if is_key is False:
                        cls.classes_list.append([key, list(value)])
                else:
                    cls.classes_list.append([key, list(value)])
                    # ----------- Special Block Ended------------
                # cls.classes_list.append([key, list(value)])

    @classmethod
    def create_class(cls, class_name: str, class_attributes: list, classes: list):
        # converting attributes which is keywords in python to non keyword by adding _ after attribute
        for attribute in class_attributes:
            # removing @ from attribute names
            if "@" in attribute:
                index = class_attributes.index(attribute)
                class_attributes[index] = attribute.replace("@", "")
            if keyword.iskeyword(attribute):
                index = class_attributes.index(attribute)
                class_attributes[index] = attribute + "_"
        # Converting list to string.
        attributes = ','.join(class_attributes)
        print(attributes)

        if not os.path.exists("../town_map"):
            os.mkdir("../town_map")
        with open("../town_map/%s.py" % class_name, "a") as python_file:

            imports = []

            for index in class_attributes:
                if index in classes:
                    imports.append(f"from src.test_pkg.town_map.{index} import {index.capitalize()}\n")
            imports = "\n".join(imports)
            if len(imports):
                class_temp = f"{imports}\nclass {class_name.capitalize()}:\n\tdef __init__(self, {attributes}):\n"
            else:
                class_temp = f"\nclass {class_name.capitalize()}:\n\tdef __init__(self, {attributes}):\n"
            python_file.write(class_temp)

            for index in class_attributes:
                attributes_temp = f"\t\tself.{index} = {index}\n"
                if index in classes:
                    attributes_temp = f"\t\tself.{index}: {index.capitalize()} = {index}\n"
                python_file.write(attributes_temp)

    @classmethod
    def iterate_json(cls, value):
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
                        cls.extract_class(key, value[key])
                    cls.iterate_json(value[key])
        elif isinstance(value, list):
            for index in value:
                cls.iterate_json(index)
        else:
            pass
            # print(value)


def main():
    # accessing json map data from json file
    with open('json_map.json') as map_data:
        carla_map = json.load(map_data)
        my_map = TownMap()
        my_map.iterate_json(carla_map)

        classes = []
        for class_values in my_map.classes_list:
            classes.append(class_values[0])
        for class_index in my_map.classes_list:
            print(class_index)
            my_map.create_class(class_name=class_index[0], class_attributes=class_index[1], classes=classes)


if __name__ == '__main__':
    main()
