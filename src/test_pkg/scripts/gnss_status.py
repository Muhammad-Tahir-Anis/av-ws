import rospy
from sensor_msgs.msg import NavSatFix


def callback(data: NavSatFix):
    gnss_const = 0.000009
    y = data.latitude / gnss_const
    x = data.longitude / gnss_const
    print(y,x)



def main():
    rospy.init_node("av_gnss_subscriber")
    rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, callback)
    rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)


if __name__ == "__main__":
    main()
