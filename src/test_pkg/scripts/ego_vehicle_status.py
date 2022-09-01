import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from ego_vehicle_control import EgoController


def callback(data):
    print(data)
    EgoController(data.header, 0, 0, 0, 0, 1, 0, 0)
    # rospy.spin()


def ego_vehicle_status_subscriber():
    sub = rospy.Subscriber('/carla/ego_vehicle/vehicle_status', CarlaEgoVehicleStatus, callback)
    rospy.spin()


def main():
    rospy.init_node('av_ego_status')
    ego_vehicle_status_subscriber()


if __name__ == '__main__':
    main()
