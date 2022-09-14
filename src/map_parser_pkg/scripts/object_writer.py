from src.map_parser_pkg.scripts.json_reader import JsonReader
from src.map_parser_pkg.scripts.object_creator import ObjectCreator


class ObjectWriter:
    __imports: list = list()
    __objects: list = list()

    def __init__(self, objects_constructs, classes):
        self.objects_constructs = objects_constructs
        for object_constructs in objects_constructs:
            object_creator = ObjectCreator(object_constructs, classes)
            self.gather_objects(object_creator.class_import, object_creator.class_object)
        self.write_object()

    @classmethod
    def gather_objects(cls, class_import, class_object):
        if class_import not in cls.__imports:
            cls.__imports.insert(0, class_import)
        cls.__objects.append(class_object)

    @classmethod
    def write_object(cls):
        imports = "\n".join(cls.__imports)
        objects = "\n".join(cls.__objects)
        combine = f"{imports}\n{objects}"
        with open("odr_map_obj.py", "w") as python_file:
            python_file.write(combine)


def main():
    json_reader = JsonReader("/home/maanz-ai/PycharmProjects/av-ws/src/test_pkg/scripts/json_map.json")
    ObjectWriter(json_reader.objects_constructs, json_reader.classes)


if __name__ == '__main__':
    main()
