from src.map_parser_pkg.scripts.json_reader import JsonReader

#
# class ObjectWriter:
#     def __init__(self, class_constructs, classes):
#         self.__class_name = class_constructs[0]
#         self.__class_parameters = class_constructs[1]
#         self.__classes = classes
#         self.__object_template(self.__class_name, self.__class_parameters, )
#
#     @classmethod
#     def __object_template(cls, class_name: str, class_parameters: list, parameter_values: list):


def main():
    json_reader = JsonReader("/home/maanz-ai/PycharmProjects/av-ws/src/test_pkg/scripts/json_map.json")
    # object_writer = ObjectWriter(json_reader.classes_constructs, json_reader.classes)
    for objects in json_reader.object_constructs:
        print(objects)


if __name__ == '__main__':
    main()
