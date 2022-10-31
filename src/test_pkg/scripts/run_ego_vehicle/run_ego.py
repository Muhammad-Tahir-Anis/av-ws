import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from sensor_msgs.msg import NavSatFix
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from src.test_pkg.scripts.ego_vehicle_control import EgoController
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning
from src.test_pkg.scripts.run_ego_vehicle.trajectory import Trajectory


class AVEgoVehicleStatus:
    ego_vehicle_status: CarlaEgoVehicleStatus = CarlaEgoVehicleStatus()

    def __init__(self):
        rospy.Subscriber('/carla/ego_vehicle/vehicle_status', CarlaEgoVehicleStatus, self.callback)

    @classmethod
    def callback(cls, data):
        cls.ego_vehicle_status = data


class AVEgoVehicleControl:
    header = AVEgoVehicleStatus.ego_vehicle_status.header

    def __init__(self, throttle: float, steer: float, brake: float):
        EgoController(self.header, throttle=throttle, steer=steer, brake=brake, hand_break=0, reverse=0, gear=0,
                      manual_gear_shift=0)


class AVGnssStatus:
    y = None
    x = None
    path = PathPlanning()
    route = path.route
    trajectory = Trajectory(route)
    xp = []
    yp = []

    def __init__(self):
        rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, self.callback)
        rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)
        rospy.spin()

    @classmethod
    def callback(cls, data: NavSatFix):
        # Converting GNSS lat long to XY coordinates of MAP
        gnss_const = 0.000009
        cls.y = data.latitude / gnss_const
        cls.x = data.longitude / gnss_const

        # --------------------------------------------
        throttle, steer, brake = cls.trajectory.update_trajectory(cls.x, cls.y)
        print(throttle, steer, brake)
        AVEgoVehicleControl(throttle, steer, brake)


def main():
    rospy.init_node("AV_Drive")
    spawn_vehicle = SpawnEgoVehicle(3, "right")
    spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id)
    AVGnssStatus()


if __name__ == "__main__":
    main()
