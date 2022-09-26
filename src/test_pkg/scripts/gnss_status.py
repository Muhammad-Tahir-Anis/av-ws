import rospy
from sensor_msgs.msg import NavSatFix


class GnssData:
    x = 0
    y = 0

    def __init__(self):
        rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, self.callback)
        rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)

    @classmethod
    def callback(cls, data: NavSatFix):
        gnss_const = 0.000009
        cls.y = data.latitude / gnss_const
        cls.x = data.longitude / gnss_const
        # print(cls.x, cls.y)


# def main():
#     rospy.init_node("av_gnss_subscriber")
#     rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, callback)
#     rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)
#
#
# if __name__ == "__main__":
#     main()
