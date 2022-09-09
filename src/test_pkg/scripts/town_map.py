import json
import keyword
import os


class TownMap:
    def __init__(self, json_file_path: str):

        with open("json_map.json") as map_file:
            value = json.load(map_file)
        self.iterate_json(value)
        # self.create_classes()

    # It is list of 2d lists first index of 2d list is class name and 2nd index
    # is a list of attribute of that class.
    classes_list = []

    @classmethod
    def iterate_json(cls, value: dict):
        """
        This iterator traverse json dictionary branch by branch.
        It will not go to another branch until current branch will be traversed completely
        :param value:
        :return:
        """
        keys_list = []
        if isinstance(value, dict):
            if value.keys():
                for key in value.keys():
                    # At this point we got keys of json.
                    keys_list.append(key)

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
        value_list = []
        if isinstance(value, list):
            for index in value:
                cls.extract_class(key, index)
        else:
            # if value type is list than add _list to that value like road_list
            for data in value:
                if isinstance(value[data], list):
                    value_list.append(data + "_list")
                else:
                    value_list.append(data)

            if not [key, value_list] in cls.classes_list:
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
                            cls.classes_list[index] = [list_index[0], list(set(list_index[1] + value_list))]
                    if is_key is False:
                        cls.classes_list.append([key, value_list])
                else:
                    cls.classes_list.append([key, value_list])
                # ----------- Special Block Ended------------
            # cls.classes_list.append([key, list(value)])

    @classmethod
    def create_classes(cls):
        classes = []
        for class_values in cls.classes_list:
            classes.append(class_values[0])
        for class_index in cls.classes_list:
            cls.write_class(class_name=class_index[0], class_attributes=class_index[1], classes=classes)

    @classmethod
    def write_class(cls, class_name: str, class_attributes: list, classes: list):
        """
        This method creates pythons file and class in that file
        :param class_name:
        :param class_attributes: list
        :param classes: list
        :return:
        """
        constructor_parameters = cls.normalize_attributes(class_attributes)

        # Creating folder town_map under current package for storing all classes related to town_map
        if not os.path.exists("../town_map"):
            os.mkdir("../town_map")
        with open("../town_map/%s.py" % class_name, "w") as python_file:

            imports = []
            attributes = []

            # Managing Imports
            list_import = f"from typing import List"
            for index in class_attributes:
                if index in classes:
                    imports.append(f"from src.test_pkg.town_map.{index} import {index.capitalize()}")
                    # Managing attribute who have _list as substring.
                if "_list" in index:
                    expected_class = index.replace("_list", "")
                    if expected_class in classes:
                        imports.append(f"from src.test_pkg.town_map.{expected_class} import {expected_class.capitalize()}")
                    if list_import not in imports:
                        imports.append(f"from typing import List")
            imports = "\n".join(imports)

            # Managing class attributes
            for index in class_attributes:
                attribute = f"\t\tself.{index} = {index}\n"
                if index in classes:
                    attribute = f"\t\tself.{index}: {index.capitalize()} = {index}"
                if "_list" in index:
                    expected_class = index.replace("_list", "")
                    if expected_class in classes:
                        attribute = f"\t\tself.{index}: List[{expected_class.capitalize()}] = list()"
                attributes.append(attribute)
            attributes = "\n".join(attributes)

            # Creating Template for class by adding imports, class name and class attributes
            if len(imports):
                class_temp = f"{imports}\n\n\nclass {class_name.capitalize()}:\n\t" \
                             f"def __init__(self, {constructor_parameters}):\n{attributes}"
            else:
                class_temp = f"class {class_name.capitalize()}:\n\t" \
                             f"def __init__(self, {constructor_parameters}):\n{attributes}"

            # Writing Class template to python file.
            python_file.write(class_temp)

    @classmethod
    def normalize_attributes(cls, class_attributes: list) -> str:
        """
        removing @ from attributes and then
        converting attributes which is keywords in python to non keyword by adding _ after attribute
        :param class_attributes:
        :return:
        """
        for attribute in class_attributes:
            # removing @ from attribute names
            index = class_attributes.index(attribute)
            if "@" in attribute:
                class_attributes[index] = attribute.replace("@", "")
                attribute = class_attributes[index]
            if keyword.iskeyword(attribute):
                class_attributes[index] = attribute + "_"
        # Converting list to string.
        constructor_parameters = ','.join(class_attributes)
        return constructor_parameters
