import os.path
from typing import List


class ClassWriter:
    def __init__(self, class_constructs, classes):
        self.__class_name = class_constructs[0]
        self.__class_attributes = class_constructs[1]
        self.__classes = classes
        temp_class = self.__class_template(self.__class_name, self.__class_attributes, self.__classes)
        self.write_class(self.__class_name,temp_class)

    @classmethod
    def __class_template(cls, class_name: str, class_attributes: List[str], classes: List[str]):
        __constructor_parameters: str = ""
        __initialized_attributes: List[str] = list()
        __my_imports: List[str] = list()
        __constructor_parameters = "=None,".join(class_attributes) + "=None"
        __initialized_attributes = cls.__attribute_template(class_attributes, classes)
        __my_imports = cls.__imports_template(class_attributes,classes)
        __attributes = "\n\t\t".join(__initialized_attributes) + "\n"
        __imports = "\n".join(__my_imports) + "\n"
        __temp_class = f"{__imports}\n" \
                       f"class {class_name.capitalize()}:\n\t" \
                       f"def __init__(self,{__constructor_parameters}):\n\t\t" \
                       f"{__attributes}"
        return __temp_class

    @classmethod
    def __attribute_template(cls, class_attributes: List[str], classes: List[str]):
        __temp_attributes: list = list()
        for class_attribute in class_attributes:
            temp_attribute = f"self.{class_attribute} = {class_attribute}"
            if class_attribute in classes:
                temp_attribute = f"self.{class_attribute}: {class_attribute.capitalize()} = {class_attribute}"
            elif "_list" in class_attribute:
                expected_class = class_attribute.replace("_list", "")
                if expected_class in classes:
                    temp_attribute = f"self.{class_attribute}: List[{expected_class.capitalize()}] = list()"
            __temp_attributes.append(temp_attribute)
        return __temp_attributes

    @classmethod
    def __imports_template(cls, class_attributes: List[str], classes: List[str]):
        __temp_imports: list = list()
        list_import = f"from typing import List"
        for class_attribute in class_attributes:
            if class_attribute in classes:
                __temp_imports.append(
                    f"from src.map_parser_pkg.odr_map.{class_attribute.lower()} import {class_attribute.capitalize()}")
            if "_list" in class_attribute:
                expected_class = class_attribute.replace("_list", "")
                if expected_class in classes:
                    __temp_imports.append(
                        f"from src.map_parser_pkg.odr_map.{expected_class.lower()} import {expected_class.capitalize()}")
                if list_import not in __temp_imports:
                    __temp_imports.append(list_import)
        return __temp_imports

    @classmethod
    def write_class(cls, class_name, temp_class):
        if not os.path.exists("../odr_map"):
            os.mkdir("../odr_map")
        with open(f"../odr_map/{class_name.lower()}.py", "w") as python_file:
            python_file.write(temp_class)
