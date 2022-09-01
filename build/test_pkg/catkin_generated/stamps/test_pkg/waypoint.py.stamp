import rospy
from nav_msgs.msg import Path


def waypoint_callback(data):
    print(data)
    rospy.spin()


# def waypoint_client(): rospy.wait_for_service('/carla_waypoint_publisher/ego_vehicle/get_waypoint') try:
# waypoint_srv = rospy.ServiceProxy('/carla_waypoint_publisher/ego_vehicle/get_waypoint',GetWaypoint,
# waypoint_callback) response =  waypoint_srv()


def main():
    rospy.init_node('waypoint_node')
    subscriber = rospy.Subscriber('/carla/ego_vehicle/waypoints', Path, waypoint_callback)
    rospy.spin()


if __name__ == '__main__':
    main()
