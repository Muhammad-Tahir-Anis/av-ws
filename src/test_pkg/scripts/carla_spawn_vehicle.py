import rospy
from geometry_msgs.msg import Pose, Point, Quaternion
from diagnostic_msgs.msg import KeyValue
from carla_msgs.srv import SpawnObject
from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.map_parser_pkg.scripts.odr_map import OdrMap
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation


class SpawnEgoVehicle:
    ego_vehicle_id: int = 0

    def __init__(self, road_id: int, lane: str):
        spawning = self.spawn_object_client(road_id, lane)
        self.ego_vehicle_id = spawning.id

    @classmethod
    def spawn_object_client(cls, road_id, lane):
        rospy.wait_for_service('/carla/spawn_object')
        try:
            spawn_object = rospy.ServiceProxy('/carla/spawn_object', SpawnObject)
            role_name = KeyValue("role_name", "ego_vehicle")
            color = KeyValue("color", "255,255,255")
            key_value = [role_name, color]
            odr = OdrMap()
            print(road_id, lane)
            x, y, z, w = odr.spawn_at_road(road_id, lane)
            print(x, y)
            print(z, w)
            point = Point(x, y, 10)
            quaternion = Quaternion(0, 0, z, w)
            pose = Pose(point, quaternion)
            random_pos = False
            attach = 0
            response = spawn_object('vehicle.tesla.model3', 'vehicle.tesla.model3', key_value, pose, attach, random_pos)
            return response
        except rospy.ServiceException as e:
            return e


# def main():
#     rospy.init_node('spawn_vehicle_node')
#
#
# if __name__ == '__main__':
#     main()
