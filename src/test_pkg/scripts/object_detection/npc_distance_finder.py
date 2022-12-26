from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning
from src.test_pkg.scripts.run_ego_vehicle.road_info import RoadInfo


class NpcDistanceFinder:

    def __init__(self):
        path = PathPlanning()
        planned_path = path.route

    @classmethod
    def get_unique_st(cls, s, t, road_id):
        road_id = int(road_id)
        # road_info = RoadInfo()
        path = PathPlanning()
        route = path.route
        last_s = 0
        for road, lane in route:
            road = int(road)
            lane = int(lane)

            # print(road, lane)
            if road == road_id:
                s = s + last_s
                return s, t
            last_s, t = cls.add_s(last_s, road, lane)
        print("s: ", s,"t: ", t)

    @classmethod
    def add_s(cls, last_s, road, lane):
        road_info = RoadInfo()
        lane_center = road_info.lane_center_point(int(road), int(lane))
        sections = road_info.get_road_info(road, None)
        if sections.ndim == 1:
            x, y, length, heading, curvature = sections
            axis = AxisTransformation(x, y, x, y, heading, curvature, 0)
            xr, yr = axis.reverse_transformation(length, lane_center, x, y, heading, curvature)
            axis = AxisTransformation(xr, yr, x, y, heading, curvature, 0)
            s, t = axis.s_t_axis
            s = s + last_s
        elif sections.ndim == 2:
            init_s = 0
            for section in sections:
                x, y, length, heading, curvature = section
                axis = AxisTransformation(x, y, x, y, heading, curvature, 0)
                xr, yr = axis.reverse_transformation(length, lane_center, x, y, heading, curvature)
                axis = AxisTransformation(xr, yr, x, y, heading, curvature, 0)
                s, t = axis.s_t_axis
                init_s = s + init_s
            s = init_s + last_s
        return s, t

