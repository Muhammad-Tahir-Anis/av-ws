import rospy
from carla_msgs.msg import CarlaEgoVehicleControl


class EgoController:
    def __init__(self, header, throttle, steer, brake, hand_break, reverse, gear, manual_gear_shift):
        self.header = header
        self.throttle = throttle
        self.steer = steer
        self.brake = brake
        self.hand_break = hand_break
        self.reverse = reverse
        self.gear = gear
        self.manual_gear_shift = manual_gear_shift
        ego_vehicle_control_publisher(self.header, self.throttle, self.steer, self.brake, self.hand_break, self.reverse,
                                      self.gear, self.manual_gear_shift)
        # rospy.spin()


def ego_vehicle_control_publisher(header, throttle, steer, brake, hand_break, reverse, gear, manual_gear_shift):
    pub = rospy.Publisher('/carla/ego_vehicle/vehicle_control_cmd', CarlaEgoVehicleControl, queue_size=10)
    pub.publish(header, throttle, steer, brake, hand_break, reverse, gear, manual_gear_shift)
    # rospy.spin()
