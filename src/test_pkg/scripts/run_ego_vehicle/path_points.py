from matplotlib import pyplot as plt

from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning
from src.test_pkg.scripts.run_ego_vehicle.road_info import RoadInfo
import numpy as np


class PathWayPoints:
    def __init__(self, planed_path):
        self.extract_waypoints(planed_path)

    @classmethod
    def extract_waypoints(cls, route):
        print(route)
        road_info = RoadInfo()
        x_points = []
        y_points = []

        for road, lane in route:
            sections = cls.get_section(route, road_info, road, lane)
            # subsections = cls.get_subsections(sections, road_info, road, lane)

            if sections.ndim == 1:
                x, y = cls.get_subsections(sections, road_info, road, lane)
                x_points.append(x)
                y_points.append(y)

                # k = []
                # j = []
                #
                # [k.append(l) for i in x_points for l in i]
                # [j.append(l) for i in y_points for l in i]

            elif sections.ndim == 2:
                x_list = []
                y_list = []
                for section in sections:
                    x, y = cls.get_subsections(section, road_info, road, lane)
                    x_list.append(x)
                    y_list.append(y)

                if not road_info.successor:
                    x_list.reverse()
                    y_list.reverse()

                [x_points.append(x) for x in x_list]
                [y_points.append(y) for y in y_list]

                k = []
                j = []

                [k.append(l) for i in x_points for l in i]
                [j.append(l) for i in y_points for l in i]
        # print(x_points, y_points)

        # plt_1 = plt.figure(figsize=(40, 22.5))
        # plt.plot(k, j, 'x-')
        #
        # plt.grid()
        # plt.show()
        # print(k, j)

    @classmethod
    def get_section(cls, route, road_info, road, lane):
        previous_road = route.index([road, lane]) - 1
        if previous_road < 0:
            sections = road_info.get_road_info(road, None)
        else:
            sections = road_info.get_road_info(road, route[previous_road][0])
        return sections

    @classmethod
    def get_subsections(cls, section, road_info, road, lane):
        if section.ndim == 1:
            x, y, length, heading, curvature = section
            axis_transformation = AxisTransformation(x, y, x, y, heading, curvature, 0)
            lane_center = road_info.lane_center_point(int(road), int(lane))

            no_of_sections = int(length / 0.1 + 1)
            subsections = np.linspace(0, length, no_of_sections)

            x_list = []
            y_list = []
            # print(len(subsections))
            for sections in range(len(subsections)):
                if sections < len(subsections) - 1:
                    # print(subsections[sections])
                    forward_start = axis_transformation.reverse_transformation(subsections[sections], lane_center, x, y,
                                                                               heading, curvature)

                    forward_end = axis_transformation.reverse_transformation(subsections[sections + 1], lane_center, x,
                                                                             y, heading, curvature)

                    x_list.append(forward_start[0])
                    x_list.append(forward_end[0])
                    y_list.append(forward_start[1])
                    y_list.append(forward_end[1])

                    if not road_info.successor:
                        x_list.reverse()
                        y_list.reverse()

            return x_list, y_list

    @classmethod
    def get_waypoints(cls):
        pass


if __name__ == '__main__':
    path = PathPlanning()
    PathWayPoints(path.route)
