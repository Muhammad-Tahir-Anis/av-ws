import json
import keyword
from typing import List

from src.map_parser_pkg.scripts.class_writer import ClassWriter


class JsonReader:
    objects: list = list()
    classes_constructs: list = list()
    object_constructs: list = list()
    classes: list = list()

    def __init__(self, json_file_path):
        self.__json_file_path = json_file_path
        with open(self.__json_file_path) as self.__json_file:
            self.__json_data = json.load(self.__json_file)
            self.__read_json(self.__json_data)
            self.__normalize_class_attributes(self.classes_constructs)
            # self.__normalize_class_attributes(self.object_constructs)

    @classmethod
    def __read_json(cls, json_data):
        __keys = list()
        __value = None
        if isinstance(json_data, dict):
            if json_data.keys():
                for key in json_data.keys():
                    __keys.append(key)
                    if not isinstance(json_data[key], (str, type(None))):
                        __value = json_data[key]
                        cls.__extract_class(key, __value)
                        cls.__extract_object(key, __value)
                    cls.__read_json(__value)
            else:
                pass
        elif isinstance(json_data, list):
            for data in json_data:
                cls.__read_json(data)
        elif isinstance(json_data, (str, type(None))):
            pass

    @classmethod
    def __extract_class(cls, key, value):
        __attributes = list()
        __is_key_exists = False
        if isinstance(value, list):
            for index in value:
                cls.__extract_class(key, index)
        elif isinstance(value, (dict, str, type(None))):
            for keys in value:
                attribute = value[keys]
                if isinstance(attribute, list):
                    __attributes.append(f"{keys}_list")
                else:
                    __attributes.append(keys)
            if len(cls.classes_constructs):
                for class_constructs in cls.classes_constructs:
                    if class_constructs[0] is key:
                        __is_key_exists = True
                        index = cls.classes_constructs.index([key, class_constructs[1]])
                        cls.classes_constructs[index] = [key, __attributes]
                        cls.classes.append(key)
                if __is_key_exists is False:
                    cls.classes_constructs.append([key,__attributes])
                    cls.classes.append(key)
            else:
                cls.classes_constructs.append([key, __attributes])
                cls.classes.append(key)

    @classmethod
    def __extract_object(cls, key, value):
        parameter: list = list()
        __parameters: list = list()
        if isinstance(value, list):
            for index in value:
                cls.__extract_object(key, index)
        elif isinstance(value, dict):
            for keys in value:
                if isinstance(value[keys],list):
                    parameter = [f"{keys}_list", f"{keys}s"]
                elif isinstance(value[keys],dict):
                    for data in value[keys]:
                        parameter = [keys,data]
                    print(parameter)
                elif isinstance(value[keys],(str,type(None))):
                    parameter = [keys,value[keys]]
                __parameters.append(parameter)
            cls.object_constructs.append([key,__parameters])

    @classmethod
    def __normalize_class_attributes(cls, classes_constructs):
        if isinstance(classes_constructs,list):
            for index in classes_constructs:
                cls.__normalize_class_attributes(index)
        else:
            cls.__normalize(classes_constructs)
        # for class_constructs in classes_constructs:
        #     # removing @ from attribute names
        #     for class_construct in class_constructs:
        #         if isinstance(class_construct,list):
        #             for attribute in class_construct:
        #                 index = class_construct.index(attribute)
        #                 class_construct[index] = cls.__normalize(attribute)
        #         else:
        #             index = class_constructs.index(class_construct)
        #             class_constructs[index] = cls.__normalize(class_construct)
        cls.classes_constructs = classes_constructs

    @classmethod
    def __normalize(cls,word):
        if "@" in word:
            word = word.replace("@", "")
        if "{" in word:
            word = word.replace("{","")
        if "}" in word:
            word = word.replace("}", "")
        if keyword.iskeyword(word):
            word = word + "_"
        return word
