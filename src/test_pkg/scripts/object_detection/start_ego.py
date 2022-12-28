import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from src.test_pkg.scripts.ego_vehicle_control import EgoController
from src.test_pkg.scripts.object_detection.npc_spawn_subscriber import NpcSubscriber
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning
from src.test_pkg.scripts.run_ego_vehicle.trajectory import Trajectory
from src.test_pkg.scripts.Obstacle_avoidance.npc_distance_finder import NpcDistanceFinder
from src.test_pkg.scripts.object_detection.detect_obstacle import DetectObstacle
from src.test_pkg.scripts.object_detection.save_npc_data import NpcDataStorage
from src.test_pkg.scripts.Obstacle_avoidance.distancethreshold import DistanceThreshold


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
    npc_subscriber = NpcSubscriber()

    y = None
    x = None
    path = PathPlanning()
    route = path.updated_route


    trajectory = Trajectory(route)
    xp = []
    yp = []

    distance = NpcDistanceFinder()
    s = 0.0
    t = 0.0
    ego_s = 0.0
    ego_t = 0.0
    road_id = 0
    lane_id = 0.0
    npc_distance = DetectObstacle()
    distance_diff = DistanceThreshold()
    imu_data = AVimuStatus()



    def __init__(self):
        rospy.Subscriber('/carla/ego_vehicle/gnss_sensor', NavSatFix, self.callback)
        # rospy.Subscriber('/carla/ego_vehicle/radar_sensor', PointCloud2, self.lidar)
        rospy.wait_for_message("/carla/ego_vehicle/gnss_sensor", NavSatFix)
        # rospy.wait_for_message("/carla/ego_vehicle/lidar_sensor", PointCloud2)
        rospy.spin()
    @classmethod
    def get_updated_trajectory_path(cls):
        path = cls.distance_diff.update_tragectory(cls.route)
        return path
    @classmethod
    def callback(cls, data: NavSatFix):
        # Converting GNSS lat long to XY coordinates of MAP
        gnss_const = 0.000009
        cls.y = data.latitude / gnss_const
        cls.x = data.longitude / gnss_const
        # --------------------------------------------
        cls.xp.append(cls.x)
        cls.yp.append(cls.y)

        throttle, steer, brake = cls.trajectory.update_trajectory(cls.x, cls.y)
        AVEgoVehicleControl(throttle, steer, brake)
        location = EgoLocation(cls.x, cls.y)
        cls.s, cls.t = location.get_ego_location_st
        cls.road_id = location.road_id
        cls.lane_id = location.lane_id
        cls.distance = NpcDistanceFinder()
        cls.ego_s, cls.ego_t = cls.distance.get_unique_st(cls.s, cls.t, cls.road_id)
        print('stststststtsttstts: ', cls.ego_s, cls.ego_t)
        # load_file = NpcDataStorage()
        # data = load_file.load_object("data.pickle")
        # npc_road, npc_lane, npc_dist = data
        # print(npc_road, 'NR')
        # print("npc_distance ; ", npc_road, npc_lane, npc_dist)
        cls.distance_diff.update_tragectory(cls.route)



def main():
    rospy.init_node("AV_Drive")
    spawn_vehicle = SpawnEgoVehicle(3, "right", "ego_vehicle")
    spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id, "gnss", "camera", "imu", "odometer",
                               "speedometer", "radar", "actor_list_sensor")
    gnss = AVGnssStatus()
    # print(gnss.xp)
    # print(gnss.yp)


if __name__ == "__main__":
    main()
