import rospy
from carla_msgs.msg import CarlaActorList
from geometry_msgs.msg import Pose, Point, Quaternion
from diagnostic_msgs.msg import KeyValue
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from std_msgs.msg import UInt32, Bool, String
from carla_msgs.srv import SpawnObject


class SpawnSensor:
    def __init__(self, attach_id, *args):
        self.spawn_object_client(attach_id, *args)

    @classmethod
    def spawn_object_client(cls, attach_id, *sensors):
        rospy.wait_for_service('/carla/spawn_object')
        try:
            spawn_object = rospy.ServiceProxy('/carla/spawn_object', SpawnObject)
            key_value = []
            point = Point(0, 0, 0)
            quaternion = Quaternion(0, 0, 0, 0)
            pose = Pose(point, quaternion)
            random_pos = False
            attach = attach_id

            for sensor in sensors:
                if sensor == 'camera':
                    point = Point(0, 0, 2.4)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.camera.rgb', 'rgb_camera_sensor', key_value, pose, attach,
                                            random_pos)
                elif sensor == 'lidar':
                    point = Point(0, 0, 2.4)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.lidar.ray_cast', 'lidar_sensor', key_value, pose, attach,
                                            random_pos)
                elif sensor == 'lidar_semantic':
                    point = Point(0, 0, 2.4)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.lidar.ray_cast_semantic', 'lidar_sensor', key_value, pose, attach,
                                            random_pos)

                elif sensor == 'odometer':
                    point = Point(0, 0, 2.4)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.pseudo.odom', 'odometer_sensor', key_value, pose, attach,
                                            random_pos)

                elif sensor == 'speedometer':
                    point = Point(0, 0, 2.4)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.pseudo.speedometer', 'speedometer_sensor', key_value, pose, attach,
                                            random_pos)

                elif sensor == 'control':
                    point = Point(0, 0, 0)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('actor.pseudo.control.', 'control', key_value, pose, attach,
                                            random_pos)
                elif sensor == 'radar':
                    point = Point(0, 0, 2.4)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.other.radar', 'radar_sensor', key_value, pose, attach,
                                            random_pos)
                elif sensor == 'gnss':
                    response = spawn_object('sensor.other.gnss', 'gnss_sensor', key_value, pose, attach, random_pos)
                elif sensor == 'imu':
                    response = spawn_object('sensor.other.imu', 'imu_sensor', key_value, pose, attach, random_pos)
        except rospy.ServiceException as e:
            return e


# if __name__ == '__main__':
#     rospy.init_node("AV_Drive")
#     spawn_vehicle = SpawnEgoVehicle(3, "right")
#     spawn_sensor = SpawnSensor(24, "camera", "imu", "lidar", "odometer", "speedometer")
