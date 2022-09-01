import rospy

from carla_msgs.srv import SpawnObject
from carla_msgs.msg import CarlaEgoVehicleInfo,CarlaLaneInvasionEvent


# def spawn_object_client():
#     rospy.wait_for_service('/carla/spawn_object')
#     try:
#         client_proxy = rospy.ServiceProxy('/carla/spawn_object', SpawnObject)
#         return client_proxy
#     except rospy.ServiceException as e:
#         print("Exception Occurred : " + str(e))


def ego_vehicle_info_callback(data):
    # print(data)
    # rospy.logout(data)
    rospy.loginfo(data)


def subscribe_carla_ego_vehicle():
    sub_ego_vehicle = rospy.Subscriber('/carla/ego_vehicle/lane_invasion', CarlaLaneInvasionEvent, ego_vehicle_info_callback)
    rospy.spin()


def main():
    rospy.init_node('test_node')
    subscribe_carla_ego_vehicle()


if __name__ == '__main__':
    main()
