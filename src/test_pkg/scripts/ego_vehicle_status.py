import math
from math import cos, sin

import rospy
from carla_msgs.msg import CarlaEgoVehicleStatus
from ego_vehicle_control import EgoController
from gnss_status import GnssData
from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class EgoVehicle:

    @classmethod
    def xy_to_st(cls, x, y, road_id, heading):
        for road in opendrive.road_list:
            if road_id == road.id:
                if road.planview.geometry_list:
                    s_translation = (x - float(road.planview.geometry_list[0].x))
                    t_translation = (y - float(road.planview.geometry_list[0].y))
                else:
                    s_translation = (x - float(road.planview.geometry.x))
                    t_translation = (y - float(road.planview.geometry.y))
                s_rotation = s_translation * cos(heading) + t_translation * sin(heading)
                t_rotation = t_translation * cos(heading) - s_translation * sin(heading)
                s = s_rotation
                t = t_rotation
                return s, t

    # route = ["3", "0", "10", "17", "7", "90", "6", "735", "5", "516", "4", "8", "1", "675", "2", "566", "3"]
    route = ["3", "0", "10"]
    index = 0
    s = 0
    global heading, curvature

    @classmethod
    def update_route(cls, road_id, s):
        for road in opendrive.road_list:
            if road_id == road.id:
                if road.planview.geometry_list:
                    for geometry in road.planview.geometry_list:
                        road_s = float(geometry.s)
                        road_s = round(road_s,2)
                        s = round(s,2)
                        print(s, road_s)
                        if s == road_s:
                            cls.heading = float(geometry.hdg)
                            if geometry.arc:
                                cls.curvature = float(geometry.arc.curvature)
                            else:
                                cls.curvature = 0
                else:
                    cls.heading = float(road.planview.geometry.hdg)
                    cls.curvature = 0
                road_length = float(road.length)
                print(road_id, cls.heading, road_length, cls.curvature)
                return road_id, cls.heading, road_length, cls.curvature

    @classmethod
    def callback(cls, data):
        # print(data)
        global heading
        gnss = GnssData()
        # route = iter(route)
        road = cls.route[cls.index]
        road_id, heading, road_length, curvature = cls.update_route(road, cls.s)
        if curvature != 0:
            radius_of_curvature = 1 / curvature
            angle = cls.s / radius_of_curvature
            # angle = float(math.radians(angle))
            print(angle)
            heading = angle

        print(heading)
        cls.s, t = cls.xy_to_st(gnss.x, gnss.y, road_id, heading)
        print(gnss.x, gnss.y)
        print(cls.s, t, curvature)
        if cls.s <= road_length:
            EgoController(data.header, 0.15, -curvature*2.25, 0.0, 0, 0, 0, 0)
        else:
            cls.index += 1
            cls.s = 0
            EgoController(data.header, 0, 0, 1, 0, 0, 0, 0)
        # rospy.spin()

    @classmethod
    def ego_vehicle_status_subscriber(cls):
        sub = rospy.Subscriber('/carla/ego_vehicle/vehicle_status', CarlaEgoVehicleStatus, cls.callback)
        rospy.spin()


def main():
    ego_vehicle = EgoVehicle
    rospy.init_node('av_ego_status')
    ego_vehicle.ego_vehicle_status_subscriber()


if __name__ == '__main__':
    main()
