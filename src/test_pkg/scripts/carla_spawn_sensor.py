import rospy
from geometry_msgs.msg import Pose, Point, Quaternion
from diagnostic_msgs.msg import KeyValue
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
                    point = Point(0, 0, 0)
                    quaternion = Quaternion(0, 0, 0, 0)
                    pose = Pose(point, quaternion)
                    response = spawn_object('sensor.camera.rgb', 'rgb_camera-sensor', key_value, pose, attach, random_pos)
                elif sensor == 'gnss':
                    response = spawn_object('sensor.other.gnss', 'gnss_sensor', key_value, pose, attach, random_pos)
                elif sensor == 'imu':
                    response = spawn_object('sensor.other.imu', 'imu_sensor', key_value, pose, attach, random_pos)
        except rospy.ServiceException as e:
            return e
