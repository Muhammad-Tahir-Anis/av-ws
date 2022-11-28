import rospy
from geometry_msgs.msg import Pose, Point, Quaternion
from diagnostic_msgs.msg import KeyValue
from std_msgs.msg import UInt32, Bool, String
from carla_msgs.srv import SpawnObject


class SpawnSensor:
    def __init__(self, attach_id):
        self.spawn_object_client(attach_id)

    @classmethod
    def spawn_object_client(cls, attach_id):
        rospy.wait_for_service('/carla/spawn_object')
        try:
            spawn_object = rospy.ServiceProxy('/carla/spawn_object', SpawnObject)
            keyval_1 = KeyValue()
            key_value = []
            # point = Point(0.5, 0, 1.3)  # point at back view mirror in car to spawn camera over their
            point = Point(0, 0, 0)
            quaternion = Quaternion(0, 0, 0, 0)
            pose = Pose(point, quaternion)
            random_pos = False
            attach = attach_id
            # response = spawn_object('sensor.camera.rgb', 'rgb_camera-sensor', key_value, pose, attach, random_pos)
            response = spawn_object('sensor.other.gnss', 'gnss_sensor', key_value, pose, attach, random_pos)
            response = spawn_object('sensor.other.imu', 'imu_sensor', key_value, pose, attach, random_pos)
            return response
        except rospy.ServiceException as e:
            return e


# def main():
#     rospy.init_node('spawn_sensor_node')
#
#
# if __name__ == '__main__':
#     main()
