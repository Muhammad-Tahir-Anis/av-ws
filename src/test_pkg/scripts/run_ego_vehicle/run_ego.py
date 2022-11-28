import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from src.test_pkg.scripts.ego_vehicle_control import EgoController
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
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


class AVimuStatus:

    def __init__(self):
        self.imu_data: Imu = Imu()
        rospy.Subscriber('/carla/ego_vehicle/imu_sensor', Imu, self.callback)
        # rospy.wait_for_message("/carla/ego_vehicle/imu_sensor", Imu)
        # rospy.spin()

    def callback(self, data):
        self.imu_data = data

    @property
    def get_imu(self):
        return self.imu_data


class AVGnssStatus:
    y = None
    x = None
    path = PathPlanning()
    route = path.route
    trajectory = Trajectory(route)
    xp = []
    yp = []

    imu_data = AVimuStatus()

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
        print("xy: ", cls.x, cls.y)
        cls.xp.append(cls.x)
        cls.yp.append(cls.y)
        print(cls.imu_data.get_imu)
        throttle, steer, brake = cls.trajectory.update_trajectory(cls.x, cls.y)
        # throttle, steer, brake = 0, 0, 0
        AVEgoVehicleControl(throttle, steer, brake)


def main():
    rospy.init_node("AV_Drive")
    spawn_vehicle = SpawnEgoVehicle(3, "right")
    spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id)
    gnss = AVGnssStatus()
    print(gnss.xp)
    print(gnss.yp)


if __name__ == "__main__":
    main()
