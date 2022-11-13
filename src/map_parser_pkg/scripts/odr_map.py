import math
from math import sin, cos, pi

import numpy as np

from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation


class OdrMap:
    lane_width = None
    driving_lane = None
    driving_lanes: list = list()
    _road = None

    def __init__(self):
        self.lane_width = None
        self.lane_offset = None
        self.heading = None
        self.y = None
        self.x = None

    def spawn_at_road(self, road_id: int, lane_section: str):
        roads = opendrive.road_list
        road_id = str(road_id)
        for road in roads:
            if road_id == road.id:
                self._road = road
            else:
                print("Junction")
        if self._road.planview.geometry_list:
            self.x = float(self._road.planview.geometry_list[0].x)
            self.y = float(self._road.planview.geometry_list[0].y)
            self.heading = float(self._road.planview.geometry_list[0].hdg)
            # according to OpenDrive standards value of 's' on first
            # index of geometry list will always be 0
        else:
            self.x = float(self._road.planview.geometry.x)
            self.y = float(self._road.planview.geometry.y)
            self.heading = float(self._road.planview.geometry.hdg)
        if self._road.lanes.laneoffset_list:
            self.lane_offset = float(self._road.lanes.laneoffset_list[0].a)
        else:
            self.lane_offset = float(self._road.lanes.laneoffset.a)
        if lane_section == "left":
            if self._road.lanes.lanesection.left.lane_list:
                lane_section_list = self._road.lanes.lanesection.left.lane_list
            else:
                lane_section_list = self._road.lanes.lanesection.left.lane
            self.lane_width = self.select_lane_section(lane_section_list)
            if self.lane_offset >= 0:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               self.lane_offset)
            else:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               lane_offset=0)
        if lane_section == "right":
            if self._road.lanes.lanesection.right.lane_list:
                lane_section_list = self._road.lanes.lanesection.right.lane_list
            else:
                lane_section_list = self._road.lanes.lanesection.right.lane
            self.lane_width = self.select_lane_section(lane_section_list)
            if self.lane_offset <= 0:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               -self.lane_offset)
            else:
                return self.adjust_spawn_point(self.x, self.y, lane_section, self.heading, self.lane_width,
                                               lane_offset=0)

    @classmethod
    def select_lane_section(cls, lane_section_list):
        if isinstance(lane_section_list, list):
            for lane in lane_section_list:
                if lane.type == "driving":
                    cls.driving_lanes.append(lane.id)
            cls.driving_lane = int(max(cls.driving_lanes))
            print(cls.driving_lanes)
            print(cls.driving_lane)
            for lane in lane_section_list:
                if lane.id == str(cls.driving_lane):
                    cls.lane_width = float(lane.width.a)
        else:
            if lane_section_list.type == "driving":
                cls.driving_lanes.append(int(lane_section_list.id))
            if lane_section_list.id == str(cls.driving_lane):
                cls.lane_width = float(lane_section_list.width.a)
        return cls.lane_width

    @classmethod
    def rad_to_degree(cls, radian):
        degree = (radian / pi) * 180
        return degree

    @classmethod
    def anticlockwise_degree_to_clockwise(cls, degree):
        # if degree < 0:
        #     degree = 360 + degree
        return degree

    @classmethod
    def adjust_spawn_point(cls, x, y, lane_section, heading, lane_width, lane_offset):
        global z
        print(heading)
        angle = cls.rad_to_degree(heading)
        print(angle)
        degree = cls.anticlockwise_degree_to_clockwise(angle)
        print(degree)
        w = 0
        x_origin = x
        y_origin = y
        print(x_origin, y_origin)
        x_point = x
        y_point = y
        print(x_point, y_point)

        # New Added Axis Transformation Testing
        axis_transformation = AxisTransformation(x_point, y_point, x_origin, y_origin, heading, 0, 0)
        s_transformed, t_transformed = axis_transformation.s_t_axis
        s_transformed = s_transformed + 1
        # s_transformed = s_transformed

        # # Axis Translation from Inertial XY to Reference Line ST
        # s_translated = x_point - x_origin
        # t_translated = y_point - y_origin
        # print(s_translated, t_translated)
        #
        # # Axis Rotation from Reference Line ST to local UV
        # u_rotated = s_translated * cos(heading) + t_translated * sin(heading) + 1
        # v_rotated = t_translated * cos(heading) - s_translated * sin(heading)
        # print(u_rotated, v_rotated)

        # Setting Direction of vehicle on road while spawning
        if lane_section == "left":
            w = cos((heading+pi)/2)
            z = sin((heading+pi)/2)
            # v_rotated = v_rotated + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
            t_transformed = t_transformed + lane_offset + cls.center_lane(len(cls.driving_lanes), lane_width)
        elif lane_section == "right":
            w = cos(heading / 2)
            z = sin(heading / 2)
            # v_rotated = v_rotated - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
            t_transformed = t_transformed - lane_offset - cls.center_lane(len(cls.driving_lanes), lane_width)
        # print(u_rotated, v_rotated)

        # Reverse Rotation from Local UV to Reference Line ST
        print(degree)
        print(cos(heading))
        print(sin(-heading))
        # s_translated = (u_rotated * np.cos(-heading)) + (v_rotated * np.sin(-heading))
        # t_translated = (v_rotated * np.cos(-heading)) - (u_rotated * np.sin(-heading))
        x, y = axis_transformation.reverse_transformation(s_transformed,t_transformed,x_origin,y_origin,heading,0)
        # print(s_translated, t_translated)

        # Reverse Translation from Reference Line ST to Inertial XY
        # x = s_translated + x_origin
        # y = t_translated + y_origin
        print(x, y)
        return x, y, z, w

    @classmethod
    def center_lane(cls, no_of_lanes, lane_width):
        point = ((2 * no_of_lanes - 1) / 2) * lane_width
        # print(point)
        return point

    # def normalize_s(self, last_s, next_road, s_list):
    #     for road in opendrive.road_list:
    #         if float(road.id) == next_road:
    #             if road.planview.geometry_list:
    #                 for geometry in road.planview.geometry_list:
    #                     s_list.append([float(geometry.s) + last_s, road.id])
    #                 last_s = float(road.planview.geometry_list[len(road.planview.geometry_list) - 1].s)
    #             else:
    #                 s_list.append([float(road.planview.geometry.s) + last_s, road.id])
    #                 last_s = float(road.planview.geometry.s)
    #             next_road = float(self.what_next(next_road)[0])
    #             self.normalize_s(last_s, next_road, s_list)

    # def what_s(self):
    #     s_list = []
    #     last_s = 0
    #     next_road = 0
    #     self.normalize_s(last_s, next_road, s_list)
    #     [print(s) for s in s_list]

    # def what_next(self, road_id):
    #     roads = opendrive.road_list
    #     for road in roads:
    #         if road_id == float(road.id):
    #             next_road = road.link.successor.elementid
    #             previous_road = road.link.predecessor.elementid
    #             return next_road, previous_road


# def main():
#     odr_map = OdrMap()
#     odr_map.spawn_at_road(10, "left")
#
#
# if __name__ == '__main__':
#     main()
