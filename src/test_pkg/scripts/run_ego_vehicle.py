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
        self.route = ["3", "0"]

    @property
    def route(self):
        return self.route

    @route.setter
    def route(self, value):
        self._route = value


class AxisTransformation:
    def __init__(self, x, y, x_origin, y_origin, heading):
        x_translated, y_translated = self.__axis_translation(x, y, x_origin, y_origin)
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


class Trajectory:
    path = PathPlanning()
    path.route = ["3", "0"]

    def __init__(self):
        self._t_axis = None
        self._s_axis = None
        self.route = ["3", "0"]
        self.path_index = 0

    @property
    def s_axis(self):
        return self.s_axis

    @property
    def t_axis(self):
        return self.t_axis

    @s_axis.setter
    def s_axis(self, value):
        self._s_axis = value

    @t_axis.setter
    def t_axis(self, value):
        self._t_axis = value

    @property
    def path_index(self):
        return self.path_index

    @path_index.setter
    def path_index(self, value):
        self._path_index = value

    @property
    def route(self):
        return self.route

    @route.setter
    def route(self, value):
        self._route = value

    def update_trajectory(self, x, y):
        print("X: ", x, "Y: ", y)
        print("S: ", self.s_axis, "T: ", self.t_axis)
        road_id = self.route[self.path_index]
        roads = opendrive.road_list
        for road in roads:
            if road_id == road.id:
                if self.s_axis > float(road.length):
                    AVEgoVehicleControl(0, 0, 1)
                    self.path_index += 1
                    self.s_axis = 0
                else:
                    AVEgoVehicleControl(0.2, 0, 0)
                if road.planview.geometry_list:
                    geometries = road.planview.geometry_list
                    for geometry in geometries:
                        if geometries.index(geometry) < len(geometries) - 1:
                            next_geometry = geometries[geometries.index(geometry) + 1]
                            if geometry.s <= self.s_axis < next_geometry.s:
                                if geometry.arc.curvature:
                                    curvature = geometry.arc.curvature
                                    arc_handler = ArcHandler(geometry.length, curvature, geometry.hdg)
                                    print(arc_handler.handle_arc())
                                else:
                                    heading = float(geometry.hdg)
                                    # s_value = float(geometry.s)
                                    x_origin = float(geometry.x)
                                    y_origin = float(geometry.y)
                                    xy_to_st = AxisTransformation(x, y, x_origin, y_origin, heading)
                                    self.s_axis, self.t_axis = xy_to_st.s_t_axis
                else:
                    geometry = road.planview.geometry
                    heading = float(geometry.hdg)
                    # s_value = float(geometry.s)
                    x_origin = float(geometry.x)
                    y_origin = float(geometry.y)
                    self.s_axis, self.t_axis = AxisTransformation(x, y, x_origin, y_origin, heading)


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
    trajectory = Trajectory()

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
        cls.trajectory.update_trajectory(cls.x, cls.y)


def main():
    rospy.init_node("AV_Drive")
    spawn_vehicle = SpawnEgoVehicle(3, "right")
    spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id)
    AVGnssStatus()


if __name__ == "__main__":
    main()
