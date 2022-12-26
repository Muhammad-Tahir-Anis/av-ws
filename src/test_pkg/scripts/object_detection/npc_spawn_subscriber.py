import rospy
from std_msgs.msg import String
from src.test_pkg.scripts.object_detection.non_player_character_spawner import Npc_1
from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.path_planning.Shortest_path_with_lanes import lane_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path
from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class NpcSubscriber:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.sub = rospy.Subscriber("talker", String, self.callback)

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.x = data.data
        self.y = data.data

    @property
    def get_gnss_data(self):
        return self.x, self.y


def main():
    npc1 = Npc_1(17, "right")
    print("stopped")
    # try:
    #     rospy.spin()
    # except rospy.ROSInterruptException:
    #     print("process interrupted shutting down")


if __name__ == "__main__":
    main()
