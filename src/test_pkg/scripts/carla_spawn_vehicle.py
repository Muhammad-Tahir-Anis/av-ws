import rospy
from geometry_msgs.msg import Pose, Point, Quaternion
from diagnostic_msgs.msg import KeyValue
from carla_msgs.srv import SpawnObject
from src.map_parser_pkg.scripts.odr_map_obj import opendrive


def spawn_object_callback(data):
    print(data)
    rospy.spin()


def spawn_object_client():
    rospy.wait_for_service('/carla/spawn_object')
    try:
        spawn_object = rospy.ServiceProxy('/carla/spawn_object', SpawnObject)
        role_name = KeyValue("role_name", "ego_vehicle")
        color = KeyValue("color", "255,255,255")
        key_value = [role_name, color]
        carla_map = opendrive
        x = float(carla_map.road_list[0].planview.geometry_list[0].x)
        print(x)
        y = float(carla_map.road_list[0].planview.geometry_list[0].y)
        print(y)
        heading = float(carla_map.road_list[0].planview.geometry_list[0].hdg)
        point = Point(x, y-12, 10)
        quaternion = Quaternion(0, 0, 1, 1)
        pose = Pose(point, quaternion)
        random_pos = False
        attach = 0
        response = spawn_object('vehicle.tesla.model3', 'vehicle.tesla.model3', key_value, pose, attach, random_pos)
        return response
    except rospy.ServiceException as e:
        return e


def main():
    rospy.init_node('spawn_vehicle_node')
    spawn = spawn_object_client()
    print(spawn)


if __name__ == '__main__':
    main()
