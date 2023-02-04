import rospy
from sensor_msgs.msg import NavSatFix
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.object_detection.detect_obstacle import DetectObstacle

from std_msgs.msg import String


class Npc_1:
    def __init__(self, road_id: int, lane: str):
        self.x = 0
        self.y = 0
        self.location = DetectObstacle()
        spawning = self.talker(road_id, lane)

    def callback(self, data: NavSatFix):
        gnss_const = 0.000009
        self.y = data.latitude / gnss_const
        self.x = data.longitude / gnss_const
        self.location.get_Obstacle_location(self.x, self.y)

    @property
    def get_gnss_data(self):
        return self.x, self.y

    def talker(self, road_id, lane):

        # pub = rospy.Publisher('npc_topic', String, queue_size=10)
        # rospy.init_node('publisher_node', anonymous=True)
        rospy.init_node('publisher_node')

        rate = rospy.Rate(1)
        spawn_vehicle = SpawnEgoVehicle(int(road_id), str(lane), "npc")
        spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id, "gnss")

        rospy.Subscriber('/carla/npc/gnss_sensor', NavSatFix, self.callback)
        rospy.wait_for_message("/carla/npc/gnss_sensor", NavSatFix)
        pub = rospy.Publisher('npc_topic', String, queue_size=10)

        # while not rospy.is_shutdown():
        for i in range(4):
            npc_id = str(spawn_vehicle.ego_vehicle_id)
            msg = self.x, self.y
            # print("x :" + self.x, "y :" + self.y)
            # print(self.get_gnss_data)?
            # print(msg)
            pub.publish(msg)
            rate.sleep()
        # self.location.get_Obstacle_location(self.x, self.y)

            # self.location.get_Obstacle_location(x, y)



