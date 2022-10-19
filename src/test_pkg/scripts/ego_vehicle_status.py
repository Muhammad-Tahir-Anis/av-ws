import math
from math import cos, sin
import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from ego_vehicle_control import EgoController
from gnss_status import GnssData
from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.carla_spawn_sensor import SpawnSensor
from src.test_pkg.scripts.carla_spawn_vehicle import SpawnEgoVehicle


class EgoVehicle:
    route = ['0', '10', '17', '7', '24', '22', '16', '15', '375', '20', '875', '21', '630', '3']
    # route = ["3","0","10"]
    # route = ["10"]
    index = 0
    s = 0
    heading = 0
    curvature = 0

    @classmethod
    def curvature_points(cls, curvature, curvature_length, heading):
        curvature_radius = 1 / curvature
        curvature_angle = float(curvature_length) / curvature_radius
        total_slices = 100
        one_angle_slice = curvature_angle / total_slices
        s_list = []
        for x in range(total_slices + 1):
            theta = x * one_angle_slice
            if theta <= curvature_angle:
                print(theta, curvature_angle)
                road_heading = theta + heading
                # S = r*theta
                s_list.append([theta * curvature_radius, road_heading])
        # for s in s_list:
        #     print(s)

    @classmethod
    def xy_to_st(cls, x, y, road_id):
        for road in opendrive.road_list:
            if road_id == road.id:
                if road.planview.geometry_list:
                    s_translation = (x - float(road.planview.geometry_list[0].x))
                    t_translation = (y - float(road.planview.geometry_list[0].y))
                else:
                    s_translation = (x - float(road.planview.geometry.x))
                    t_translation = (y - float(road.planview.geometry.y))
                s_rotation = s_translation * cos(cls.heading) + t_translation * sin(cls.heading)
                t_rotation = t_translation * cos(cls.heading) - s_translation * sin(cls.heading)
                s = s_rotation
                t = t_rotation
                return s, t

    @classmethod
    def update_route(cls, road_id, s):
        global heading
        for road in opendrive.road_list:
            if road_id == road.id:
                if road.planview.geometry_list:
                    for geometry in road.planview.geometry_list:
                        road_s = float(geometry.s)
                        # road_s = round(road_s, 2)
                        # s = round(s, 2)
                        print("Road S: ", s, "Geometry S: ", road_s)
                        print("Curvature : ", cls.curvature)
                        if road.planview.geometry_list.index(geometry) < len(road.planview.geometry_list) - 1:
                            if road_s <= s < float(
                                    road.planview.geometry_list[road.planview.geometry_list.index(geometry) + 1].s):
                                heading = float(geometry.hdg)
                                if geometry.arc:
                                    cls.curvature = float(geometry.arc.curvature)
                                    # cls.curvature_points(cls.curvature, road.length, )
                                else:
                                    cls.curvature = 0

                        elif road.planview.geometry_list[len(road.planview.geometry_list)-1]:
                            if road_s <= s:
                                heading = float(geometry.hdg)
                                if geometry.arc:
                                    cls.curvature = float(geometry.arc.curvature)
                                    # cls.curvature_points(cls.curvature, road.length, )
                                else:
                                    cls.curvature = 0
                else:
                    heading = float(road.planview.geometry.hdg)
                    cls.curvature = 0
                if cls.curvature != 0:
                    radius_of_curvature = 1 / cls.curvature
                    angle = cls.s / radius_of_curvature
                    # cls.heading = heading + angle
                    # print("CLS Heading: ", cls.heading, " heading: ", heading)
                else:
                    cls.heading = heading
                road_length = float(road.length)
                print("Road ID: ", road_id, "Road Length: ", road_length)
                return road_id, road_length

    @classmethod
    def callback(cls, data):
        gnss = GnssData()
        road = cls.route[cls.index]
        road_id, road_length = cls.update_route(road, cls.s)
        print("Road Heading: ", cls.heading)
        cls.s, t = cls.xy_to_st(gnss.x, gnss.y, road_id)
        print("X: ", gnss.x, "Y: ", gnss.y)
        print("S: ", cls.s, "T: ", t, "Curvature: ", cls.curvature)
        if cls.s <= road_length and cls.s <= 60:
            EgoController(data.header, 0.2, -cls.curvature * 2.23, 0.0, 0, 0, 0, 0)
            # EgoController(data.header, 0.15, 0, 0.0, 0, 0, 0, 0)
        else:
            cls.index += 1
            cls.s = 0
            EgoController(data.header, 0, 0, 1, 0, 0, 0, 0)
        # rospy.spin()

    @classmethod
    def ego_vehicle_status_subscriber(cls):
        rospy.Subscriber('/carla/ego_vehicle/vehicle_status', CarlaEgoVehicleStatus, cls.callback)
        rospy.spin()


def main():
    ego_vehicle = EgoVehicle
    rospy.init_node('av_ego_status')
    spawn_vehicle = SpawnEgoVehicle(3, "right")
    spawn_sensor = SpawnSensor(spawn_vehicle.ego_vehicle_id)
    ego_vehicle.ego_vehicle_status_subscriber()
    # ego_vehicle.curvature_points(0.025372645725697789, 62.506300531593439, 1.5560509823599684)


if __name__ == '__main__':
    main()

