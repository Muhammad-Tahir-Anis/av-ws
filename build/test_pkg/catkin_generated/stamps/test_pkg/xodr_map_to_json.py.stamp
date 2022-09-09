import xmltodict

import rospy

import json
from carla_msgs.msg import CarlaWorldInfo


def world_info_callback(data):
    print(data.map_name)

    with open("xodr_map.xml", "w") as xodr_file:
        xodr_file.write(data.opendrive)

    with open("xodr_map.xml") as xml_file:
        dict_map = xmltodict.parse(xml_file.read())
        json_map = json.dumps(dict_map)

        with open("json_map.json", "w") as json_file:
            json_file.write(json_map)

    print(data.opendrive)
    rospy.spin()


def world_info_subscriber():
    subscriber = rospy.Subscriber('carla/world_info', CarlaWorldInfo, world_info_callback)
    rospy.spin()


def main():
    rospy.init_node('world_info_node')
    world_info_subscriber()


if __name__ == '__main__':
    main()
