from matplotlib import pyplot as plt

from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning
from src.test_pkg.scripts.run_ego_vehicle.road_info import RoadInfo
import numpy as np


class PathWayPoints:
    def __init__(self):
        path = PathPlanning()
        planned_path = path.route
        self.waypoints = self.extract_waypoints(planned_path)

    @property
    def get_waypoints(self):
        return self.waypoints

    @classmethod
    def extract_waypoints(cls, route):
        print(route)
        road_info = RoadInfo()
        x_points = []
        y_points = []
        for road, lane in route:
            previous_road = route.index([road, lane]) - 1
            if previous_road < 0:
                sections = road_info.get_road_info(road, None)
            else:
                sections = road_info.get_road_info(road, route[previous_road][0])

            if sections.ndim == 1:
                x_list = []
                y_list = []

                x = sections[0]
                y = sections[1]
                length = sections[2]
                heading = sections[3]
                curvature = sections[4]
                axis_transformation = AxisTransformation(x, y, x, y, heading, curvature, 0)
                lane_center = road_info.lane_center_point(int(road), int(lane))

                # print('lc: ', lane_center)

                forward_start = axis_transformation.reverse_transformation(0, lane_center,
                                                                           x, y, heading, curvature)

                x_list.append(forward_start[0])
                y_list.append(forward_start[1])

                no_of_sections = int(length / 0.1 + 1)
                subsections = np.linspace(0, length, no_of_sections)
                for subsection in range(len(subsections) - 1):
                    forward_start = axis_transformation.reverse_transformation(subsections[subsection], lane_center, x,
                                                                               y, heading, curvature)
                    forward_end = axis_transformation.reverse_transformation(subsections[subsection + 1], lane_center,
                                                                             x, y, heading, curvature)
                    # print(f"1: {road}: {curvature}: ", forward_start, forward_end)

                    x_list.append(forward_end[0])
                    y_list.append(forward_end[1])

                if not road_info.successor:
                    x_list.reverse()
                    y_list.reverse()

                [x_points.append(x) for x in x_list]
                [y_points.append(y) for y in y_list]

            elif sections.ndim == 2:
                x_list = []
                y_list = []
                for section in sections:
                    x = section[0]
                    y = section[1]
                    length = section[2]
                    heading = section[3]
                    curvature = section[4]
                    axis_transformation = AxisTransformation(x, y, x, y, heading, curvature, 0)
                    lane_center = road_info.lane_center_point(int(road), int(lane))

                    # print('lc: ', lane_center)

                    forward_start = axis_transformation.reverse_transformation(0, lane_center,
                                                                               x, y, heading, curvature)

                    x_list.append(forward_start[0])
                    y_list.append(forward_start[1])

                    no_of_sections = int(length / 0.1 + 1)
                    subsections = np.linspace(0, length, no_of_sections)
                    for subsection in range(len(subsections) - 1):
                        forward_start = axis_transformation.reverse_transformation(subsections[subsection], lane_center,
                                                                                   x, y, heading, curvature)

                        forward_end = axis_transformation.reverse_transformation(subsections[subsection + 1],
                                                                                 lane_center, x, y, heading, curvature)

                        # print(f"1: {road}: {curvature}: ", forward_start, forward_end)

                        x_list.append(forward_end[0])
                        y_list.append(forward_end[1])

                if not road_info.successor:
                    x_list.reverse()
                    y_list.reverse()

                [x_points.append(x) for x in x_list]
                [y_points.append(y) for y in y_list]

        # plt_1 = plt.figure(figsize=(40, 22.5))
        # plt.plot(x_points, y_points, 'x-')
        #
        # plt.grid()
        # plt.show()

        waypoints = x_points, y_points
        return waypoints


# if __name__ == '__main__':
#     PathWayPoints()
