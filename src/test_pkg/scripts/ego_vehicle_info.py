import rospy
from carla_msgs.msg import CarlaEgoVehicleInfo
from ego_vehicle import EgoVehicle


def callback(data):
    ego_vehicle_info = EgoVehicle(data)
    print(data)


def ego_vehicle_info_subscriber():
    rospy.Subscriber('/carla/ego_vehicle/vehicle_info', CarlaEgoVehicleInfo, callback)
    rospy.spin()


def main():
    rospy.init_node('av_ego_info')
    ego_vehicle_info_subscriber()


if __name__ == '__main__':
    main()
