import json
import keyword
from typing import List

from src.map_parser_pkg.scripts.class_writer import ClassWriter


class JsonReader:
    objects: list = list()
    classes_constructs: list = list()
    objects_constructs: list = list()
    classes: list = list()
    json_list: list = list()

    def __init__(self, json_file_path):
        self.__json_file_path = json_file_path
        with open(self.__json_file_path) as self.__json_file:
            self.__json_data = json.load(self.__json_file)
            self.__read_json(self.__json_data)
            for key, value in self.json_list:
                self.__extract_class(key=key,value=value)
                # self.__extract_object(key=key,value=value)
            self.__normalize_constructs(self.classes_constructs)
            self.__normalize_constructs(self.objects_constructs)

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
                        cls.json_list.append([key,__value])
                        # cls.__extract_class(key, __value)
                        cls.__extract_object(key, __value)
                    cls.__read_json(__value)
        elif isinstance(json_data, list):
            for data in json_data:
                cls.__read_json(data)

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
                        cls.classes_constructs[index] = [class_constructs[0],
                                                         list(set(class_constructs[1] + __attributes))]
                        cls.classes.append(key)
                if __is_key_exists is False:
                    cls.classes_constructs.append([key, __attributes])
                    cls.classes.append(key)
            else:
                cls.classes_constructs.append([key, __attributes])
                cls.classes.append(key)

    @classmethod
    def __extract_object(cls, key, value, index=None):
        parameter: list = list()
        __parameters: list = list()
        if isinstance(value, list):
            list_parameter: list = list()
            for index in value:
                list_parameter.append(f"{key}{value.index(index)}")
            cls.objects_constructs.insert(0, [f"{key}s", list_parameter])
            for data in value:
                cls.__extract_object(key, data, index=value.index(data))
                cls.__read_json(data)
        elif isinstance(value, dict):
            for keys in value:
                if isinstance(value[keys], list):
                    parameter = [f"{keys}_list", f"{keys}s"]
                elif isinstance(value[keys], dict):
                    # for data in value[keys]:
                    parameter = [keys, keys]
                elif isinstance(value[keys], str):
                    parameter = [keys, f"'{value[keys]}'"]
                elif isinstance(value[keys], type(None)):
                    parameter = [keys, "''"]
                __parameters.append(parameter)
            if index is None:
                cls.objects_constructs.insert(0, [key, key, __parameters])
            else:
                cls.objects_constructs.insert(0, [f"{key}{index}", key, __parameters])

    @classmethod
    def __normalize_constructs(cls, objects_constructs):
        if isinstance(objects_constructs, list):
            for constructs in objects_constructs:
                if isinstance(constructs, list):
                    cls.__normalize_constructs(constructs)
                elif isinstance(constructs, str):
                    index = objects_constructs.index(constructs)
                    objects_constructs[index] = cls.__normalize(constructs)

    @classmethod
    def __normalize(cls, word):
        if "@" in word:
            word = word.replace("@", "")
        if "{" in word:
            word = word.replace("{", "")
        if "}" in word:
            word = word.replace("}", "")
        if keyword.iskeyword(word):
            word = word + "_"
        return word
