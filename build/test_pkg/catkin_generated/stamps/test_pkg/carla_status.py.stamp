import rospy

from carla_waypoint_types.srv import GetActorWaypoint
from carla_msgs.msg import CarlaEgoVehicleInfo, CarlaStatus


# def actor_waypoint_client():
#     rospy.wait_for_service('/carla/')
#     try:
#         client_proxy = rospy.ServiceProxy('/carla/spawn_object', GetActorWaypoint)
#         return client_proxy
#     except rospy.ServiceException as e:
#         print("Exception Occurred : " + str(e))
#
#
# def ego_vehicle_info_callback(data):
#     # data = data.id
#     # print(data)
#     # rospy.logout(data)
#     rospy.loginfo(data.id)
#
#
# def subscribe_carla_ego_vehicle():
#     sub_ego_vehicle = rospy.Subscriber('/carla/ego_vehicle/vehicle_info', CarlaEgoVehicleInfo,
#                                        ego_vehicle_info_callback)
#     rospy.spin()


def carla_status_callback(data):
    print(data)
    rospy.spin()


def subscribe_carla_status():
    subscriber = rospy.Subscriber('carla/status', CarlaStatus, carla_status_callback)
    rospy.spin()


def main():
    rospy.init_node('test_node')
    # subscribe_carla_ego_vehicle()
    subscribe_carla_status()


if __name__ == '__main__':
    main()
