import json
import os.path

import xmltodict

from src.map_parser_pkg.scripts.carla_world_info_subscriber import WorldInfoSubscriber
from src.map_parser_pkg.scripts.class_writer import ClassWriter
from src.map_parser_pkg.scripts.json_reader import JsonReader


def main():
    carla_world = WorldInfoSubscriber()
    opendrive_xml = carla_world.opendrive_map
    dict_map = xmltodict.parse(opendrive_xml)
    opendirve_json = json.dumps(dict_map)

    if not os.path.exists("../json_files"):
        os.mkdir("../json_files")
    json_file_path = "../json_files/opendrive.json"
    with open(json_file_path, 'w') as json_file:
        json_file.write(opendirve_json)

    json_reader = JsonReader(json_file_path)
    for class_constructs in json_reader.classes_constructs:
        ClassWriter(class_constructs, json_reader.classes)


if __name__ == '__main__':
    main()
