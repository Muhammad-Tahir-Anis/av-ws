import rospy
from sensor_msgs.msg import NavSatFix


class GnssData:
    def __init__(self):
        self.x = 0
        self.y = 0
        rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, self.callback)
        rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)

    def callback(self, data: NavSatFix):
        gnss_const = 0.000009
        self.y = data.latitude / gnss_const
        self.x = data.longitude / gnss_const
        # print(cls.x, cls.y)

    @property
    def get_gnss_data(self):
        return self.x, self.y
