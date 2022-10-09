import math
from math import cos, sin

import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus, CarlaEgoVehicleControl
from sensor_msgs.msg import NavSatFix
from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle
from src.test_pkg.scripts.ego_vehicle_control import EgoController


class PathPlanning:
    def __init__(self):
        self.route = ["3", "0", "10"]


class AxisTransformation:
    def __init__(self, x, y, x_origin, y_origin, heading, curvature):
        x_translated, y_translated = self.__axis_translation(x, y, x_origin, y_origin)
        if curvature != 0:
            radius_of_curvature = 1 / curvature
            self.x_prime, self.y_prime = self.__axis_translation(x, y, x_origin, y_origin)
            self.opposite, self.adjacent = self.__axis_translation(x, y, self.x_prime, self.y_prime)
            # To calculate original angle values we use
            # tan(theta) = adjacent / opposite
            # theta = tan_inverse(adjacent / opposite)
            angle_in_radian = math.atan(self.adjacent / self.opposite)
            # To calculate S and T we use S = r*angle
            # For this purpose we use radius of curvature of the road.
            self.s = radius_of_curvature * angle_in_radian
            # To get displacement of vehicle from origin which would be hypotenuse
            self.t = radius_of_curvature - ((self.opposite ^ 2 + self.adjacent ^ 2) ^ 1 / 2)

        self.s, self.t = self.__axis_rotation(x_translated, y_translated, heading)

    @classmethod
    def __axis_translation(cls, x, y, x_origin, y_origin):
        x_translation = (x - x_origin)
        y_translation = (y - y_origin)
        return x_translation, y_translation

    @classmethod
    def __axis_rotation(cls, x_translated, y_translated, heading):
        s = x_translated * cos(heading) + y_translated * sin(heading)
        t = y_translated * cos(heading) - x_translated * sin(heading)
        print(s, t)
        return s, t

    @property
    def s_t_axis(self):
        return self.s, self.t


class MapAnalysis:
    x_origin: float = 0
    y_origin: float = 0
    heading: float = 0
    curvature: float = 0
    road_ended: bool = False

    def __int__(self):
        self.x_origin: float = 0
        self.y_origin: float = 0
        self.heading: float = 0
        self.curvature: float = 0

    def road_info(self, road_id, s_axis):
        roads = opendrive.road_list
        for road in roads:
            if road_id == road.id:
                if s_axis == float(road.length):
                    # AVEgoVehicleControl(0, 0, 1)
                    # self.path_index += 1
                    # self._s_axis = 0
                    self.road_ended = True
                # else:
                #     AVEgoVehicleControl(0.2, 0, 0)
                if road.planview.geometry_list:
                    geometries = road.planview.geometry_list
                    for geometry in geometries:
                        if geometries.index(geometry) < len(geometries) - 1:
                            next_geometry = geometries[geometries.index(geometry) + 1]
                            if geometry.s <= s_axis < next_geometry.s:
                                if geometry.arc.curvature:
                                    self.curvature = geometry.arc.curvature
                                    # arc_handler = ArcHandler(geometry.length, curvature, geometry.hdg)
                                    # print(arc_handler.handle_arc())
                                else:
                                    self.heading = float(geometry.hdg)
                                    # s_value = float(geometry.s)
                                    self.x_origin = float(geometry.x)
                                    self.y_origin = float(geometry.y)
                                    # xy_to_st = AxisTransformation(x, y, x_origin, y_origin, heading)
                                    # self._s_axis, self._t_axis = xy_to_st.s_t_axis
                else:
                    geometry = road.planview.geometry
                    self.heading = float(geometry.hdg)
                    # s_value = float(geometry.s)
                    self.x_origin = float(geometry.x)
                    self.y_origin = float(geometry.y)
                    # self._s_axis, self._t_axis = AxisTransformation(x, y, x_origin, y_origin, heading)
        return self.x_origin, self.y_origin, self.heading, self.curvature, self.road_ended


class Trajectory:
    """
    Trajectory could have route points with specified speed
    route points could be get from path planning module
    """

    def __init__(self, route):
        self._t_axis = 0
        self._s_axis = 0
        self._curvature = 0
        self.route = route
        self.path_index = 0
        self.brake: bool = False
        self.throttle: float = 0
        self.steering: float = 0

    def update_trajectory(self, x, y):
        print("X: ", x, "Y: ", y)
        print("S: ", self._s_axis, "T: ", self._t_axis)
        road_id = self.route[self.path_index]
        self.throttle, self.steering, self.brake = self.follow_trajectory(x, y, road_id)
        return self.throttle, self.steering, self.brake

    def follow_trajectory(self, x, y, road_id):
        map_analysis = MapAnalysis()
        x_origin, y_origin, heading, curvature, road_ended = map_analysis.road_info(road_id, self._s_axis)
        self._s_axis, self._t_axis = AxisTransformation(x, y, x_origin, y_origin, heading, curvature)
        if road_ended:
            self._s_axis = 0
            self.path_index += 1
            self.brake = 1
            self.steering = 0
            self.throttle = 0
        elif curvature != 0 and not road_ended:
            self.throttle = 0.1
            self.brake = 0
            self.steering = 0.25
        else:
            self.throttle = 0.2
            self.brake = 0
            self.steering = 0

        return self.throttle, self.steering, self.brake

    # def analyse_map(self, road_id):
    #     roads = opendrive.road_list
    #     for road in roads:
    #         if road_id == road.id:
    #             if self._s_axis > float(road.length):
    #                 # AVEgoVehicleControl(0, 0, 1)
    #                 self.path_index += 1
    #                 self._s_axis = 0
    #             # else:
    #             #     AVEgoVehicleControl(0.2, 0, 0)
    #             if road.planview.geometry_list:
    #                 geometries = road.planview.geometry_list
    #                 for geometry in geometries:
    #                     if geometries.index(geometry) < len(geometries) - 1:
    #                         next_geometry = geometries[geometries.index(geometry) + 1]
    #                         if geometry.s <= self._s_axis < next_geometry.s:
    #                             if geometry.arc.curvature:
    #                                 curvature = geometry.arc.curvature
    #                                 # arc_handler = ArcHandler(geometry.length, curvature, geometry.hdg)
    #                                 # print(arc_handler.handle_arc())
    #                             else:
    #                                 heading = float(geometry.hdg)
    #                                 # s_value = float(geometry.s)
    #                                 x_origin = float(geometry.x)
    #                                 y_origin = float(geometry.y)
    #                                 # xy_to_st = AxisTransformation(x, y, x_origin, y_origin, heading)
    #                                 # self._s_axis, self._t_axis = xy_to_st.s_t_axis
    #             else:
    #                 geometry = road.planview.geometry
    #                 heading = float(geometry.hdg)
    #                 # s_value = float(geometry.s)
    #                 x_origin = float(geometry.x)
    #                 y_origin = float(geometry.y)
    #                 # self._s_axis, self._t_axis = AxisTransformation(x, y, x_origin, y_origin, heading)
    #     return x_origin, y_origin, heading, curvature


class ArcHandler:
    __geometry_length: float
    __curvature: float
    __geometry_heading: float
    s_values_list: list

    def __init__(self, road_length, curvature, road_heading):
        self.__geometry_length = float(road_length)
        self.__curvature = float(curvature)
        self.__geometry_heading = float(road_heading)

    @classmethod
    def handle_arc(cls):
        # S = r * angle (in radian)
        total_angle_slices = 100
        radius = 1 / cls.__curvature
        curvature_angle = cls.__geometry_length / radius
        one_angle_slice = curvature_angle / total_angle_slices
        for multiplier in range(total_angle_slices + 1):
            angle = multiplier * one_angle_slice
            if angle <= cls.__curvature:
                geometry_heading = cls.__geometry_heading + angle
                s_axis_value = radius * angle
                cls.s_values_list.append([s_axis_value, geometry_heading])
        return cls.s_values_list


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
        AVEgoVehicleControl(throttle, steer, brake)


def main():
    rospy.init_node("AV_Drive")
    spawn_vehicle = SpawnEgoVehicle(0, "right")
    spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id)
    AVGnssStatus()


if __name__ == "__main__":
    main()
