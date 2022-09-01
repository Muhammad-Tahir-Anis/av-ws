import rospy
from geometry_msgs.msg import Pose, Point, Quaternion
from diagnostic_msgs.msg import KeyValue
from carla_msgs.srv import SpawnObject


def spawn_object_callback(data):
    print(data)
    rospy.spin()


def spawn_object_client():
    rospy.wait_for_service('/carla/spawn_object')
    try:
        spawn_object = rospy.ServiceProxy('/carla/spawn_object', SpawnObject)
        keyval_1 = KeyValue()
        key_value = []
        point = Point(-68, -28.0, 0.2)
        quaternion = Quaternion(1.0, 1.0, 0.2, -180)
        pose = Pose(point, quaternion)
        random_pos = False
        attach = 0
        response = spawn_object('controller.ai.walker', 'controller-sensor', key_value, pose, attach, random_pos)
        return response
    except rospy.ServiceException as e:
        return e


def main():
    rospy.init_node('spawn_controller_node')
    spawn = spawn_object_client()
    print(spawn)


if __name__ == '__main__':
    main()