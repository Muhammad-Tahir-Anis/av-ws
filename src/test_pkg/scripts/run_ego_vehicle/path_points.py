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
            previous_road = route.index([road, lane]) - 1
            if previous_road < 0:
                sections = road_info.get_road_info(road, None)
            else:
                sections = road_info.get_road_info(road, route[previous_road][0])
            # sections = road_info.get_road_info(road)
            # print(sections)
            if sections.ndim == 1:
                x = sections[0]
                y = sections[1]
                length = sections[2]
                heading = sections[3]
                curvature = sections[4]
                axis_transformation = AxisTransformation(x, y, x, y, heading, curvature, 0)
                # lane_center = road_info.lane_center_point(int(road), int(lane))
                lane_center = 0
                print('lc: ', lane_center)

                forward_start = axis_transformation.reverse_transformation(0, lane_center, x, y, heading, curvature)
                forward_end = axis_transformation.reverse_transformation(length, lane_center, x, y, heading, curvature)
                print(f"1: {road}: {curvature}: ", forward_start, forward_end)

                if road_info.successor:
                    x_points.append(forward_start[0])
                    x_points.append(forward_end[0])
                    y_points.append(forward_start[1])
                    y_points.append(forward_end[1])
                else:
                    x_points.append(forward_end[0])
                    x_points.append(forward_start[0])
                    y_points.append(forward_end[1])
                    y_points.append(forward_start[1])

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
                    # lane_center = road_info.lane_center_point(int(road), int(lane))
                    lane_center = 0
                    print('lc: ', lane_center)

                    forward_start = axis_transformation.reverse_transformation(0, lane_center, x, y, heading,
                                                                               curvature)
                    forward_end = axis_transformation.reverse_transformation(length, lane_center, x, y, heading,
                                                                             curvature)

                    print(f"1: {road}: {curvature}: ", forward_start, forward_end)

                    # x_points.append(forward_start[0])
                    # x_points.append(forward_end[0])
                    # y_points.append(forward_start[1])
                    # y_points.append(forward_end[1])

                    x_list.append(forward_start[0])
                    x_list.append(forward_end[0])
                    y_list.append(forward_start[1])
                    y_list.append(forward_end[1])

                    if not road_info.successor:
                        x_list.reverse()
                        y_list.reverse()
                # x_points.append(x_list)
                # y_points.append(y_list)
                a = [x_points.append(x) for x in x_list]
                b = [y_points.append(y) for y in y_list]
        print(x_points, y_points)


if __name__ == '__main__':
    path = PathPlanning()
    PathWayPoints(path.route)
