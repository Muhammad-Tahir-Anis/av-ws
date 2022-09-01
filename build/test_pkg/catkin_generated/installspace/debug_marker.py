import rospy

from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker


def marker_array_publisher():
    marker = Marker()

    marker.ns = "my_namespace"
    marker.id = 0
    marker.type = 2
    marker.action = 0
    marker.pose.position.x = 1
    marker.pose.position.y = 1
    marker.pose.position.z = 1
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 1
    marker.scale.y = 0.1
    marker.scale.z = 0.1
    marker.color.a = 1.0
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    MarkerArray(marker)
    pub = rospy.Publisher('/carla/debug_marker',MarkerArray,queue_size=10)
    pub.publish(MarkerArray())
    rospy.spin()


def main():
    rospy.init_node('marker_array_node_c')
    marker_array_publisher()
    # rospy.spin()


if __name__ == '__main__':
    main()
