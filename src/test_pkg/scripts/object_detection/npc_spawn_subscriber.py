import rospy
from std_msgs.msg import String
from src.test_pkg.scripts.object_detection.non_player_character_spawner import Npc_1


class NpcSubscriber:

    def __init__(self):
        pass


def main():
    npc1 = Npc_1(10, 'right')
    print("stopped")
    # try:
    #     rospy.spin()
    # except rospy.ROSInterruptException:
    #     print("process interrupted shutting down")


if __name__ == "__main__":
    main()
