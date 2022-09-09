import rospy
from carla_msgs.msg import CarlaWorldInfo


class WorldInfoSubscriber:
    opendrive_map = None

    def __init__(self):
        rospy.init_node('av_world_info_subscriber')
        rospy.Subscriber('/carla/world_info', CarlaWorldInfo, self.__callback)
        rospy.wait_for_message('/carla/world_info',CarlaWorldInfo)

    @classmethod
    def __callback(cls, data):
        cls.opendrive_map = data.opendrive
