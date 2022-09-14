class ObjectCreator:
    class_object: str
    class_import: str

    def __init__(self, object_constructors: list, classes: list):
        self.__object_constructors = object_constructors
        self.__classes = classes
        self.__object_template(self.__object_constructors, self.__classes)

    @classmethod
    def __object_template(cls, object_constructors, classes):
        __object_temp = ""
        if len(object_constructors) == 3:
            object_name = object_constructors[0]
            class_name = object_constructors[1]
            cls.__imports_template(class_name, classes)
            class_parameters = cls.__parameters_template(object_constructors[2], classes)
            class_parameters = ",".join(class_parameters)
            __object_temp = f"{object_name.lower()} = {class_name.capitalize()}({class_parameters})"
        elif len(object_constructors) == 2:
            object_name = object_constructors[0]
            object_value = object_constructors[1]
            object_value = f"[{','.join(object_value).lower()}]"
            __object_temp = f"{object_name.lower()} = {object_value}"
        cls.class_object = __object_temp

    @classmethod
    def __parameters_template(cls, class_parameters, classes):
        if isinstance(class_parameters, list):
            for parameter in class_parameters:
                index = class_parameters.index(parameter)
                if f"'" not in parameter[1]:
                    parameter[1] = parameter[1].lower()
                parameter[0] = parameter[0].lower()
                class_parameters[index] = "=".join(parameter)
        return class_parameters

    @classmethod
    def __imports_template(cls, class_name, classes):
        if class_name in classes:
            __import_temp = f"from src.map_parser_pkg.odr_map.{class_name.lower()} import {class_name.capitalize()}"
            cls.class_import = __import_temp
