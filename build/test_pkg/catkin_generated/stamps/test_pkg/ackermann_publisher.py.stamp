import rospy
from ackermann_msgs.msg import AckermannDrive


def publish_ackermann():
    car_controller = AckermannDrive(0,0,20,1,0)
    pub = rospy.Publisher("/carla/my_car/ackermann_cmd", AckermannDrive, queue_size=10)
    pub.publish(car_controller)
    # rospy.spin()


def main():
    rospy.init_node("accermann_node_pub")
    publish_ackermann()
    rospy.spin()


if __name__ == '__main__':
    main()
