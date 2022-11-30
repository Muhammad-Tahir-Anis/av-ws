import rospy
from sensor_msgs.msg import NavSatFix
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from src.test_pkg.scripts.object_detection.detect_obstacle import ObjectLocation


class GnssData:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.location = ObjectLocation()
        rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, self.callback)
        rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)
        # rospy.spin()

    def callback(self, data: NavSatFix):
        gnss_const = 0.000009
        self.y = data.latitude / gnss_const
        self.x = data.longitude / gnss_const
        # print(self.x, self.y)


def main():
    rospy.init_node("av_gnss_subscriber")
    gnss_data = GnssData()
    print(gnss_data.get_gnss_data)


if __name__ == "__main__":
    main()
