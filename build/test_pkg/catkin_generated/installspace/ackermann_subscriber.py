import rospy
from carla_msgs.msg import CarlaEgoVehicleControl



def tf_callback(data):
    print(data)
    rospy.spin()


def tf_subscribe():
    sub = rospy.Subscriber("/statistics", TopicStatistics, tf_callback)
    rospy.spin()


def main():
    rospy.init_node("tf_subscriber_node")
    tf_subscribe()


if __name__ == '__main__':
    main()
