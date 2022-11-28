import rospy
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from ackermann_msgs.msg import AckermannDrive


class AVackermann:

    def __init__(self):
        rospy.wait_for_message('/carla/ego_vehicle/ackermann_cmd', AckermannDrive)
        print("OK")
        print("OK")
        pup = rospy.Publisher('/carla/ego_vehicle/ackermann_cmd', AckermannDrive, queue_size=10)
        pup.publish(0, 0, 10, 0, 0)
        rospy.Subscriber('/carla/ego_vehicle/ackermann_cmd', AckermannDrive, callback=callback)
        rospy.wait_for_message('/carla/ego_vehicle/ackermann_cmd',AckermannDrive)
        print("OK")
        # rospy.spin()


def callback(data):
    # print(data)
    pass


def main():
    rospy.init_node('av_ackermann')
    print("OK")
    spawn_vehicle = SpawnEgoVehicle(3, "right")
    # AVackermann()


if __name__ == "__main__":
    main()
