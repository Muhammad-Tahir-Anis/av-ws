from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning
from src.test_pkg.scripts.run_ego_vehicle.road_info import RoadInfo


class NpcDistanceFinder:

    def __init__(self):
        path = PathPlanning()
        planned_path = path.route

    @classmethod
    def get_unique_st(cls, s, t, road_id):
        successor = True
        road_id = int(road_id)
        # road_info = RoadInfo()
        path = PathPlanning()
        route = path.route
        last_s = 0
        count = 0
        print(route)
        road_info = RoadInfo()

        for road, lane in route:
            road = int(road)
            lane = int(lane)

            if count != 0:
                previous_road = route[count-1][0]
            else:
                previous_road = None
            # print(road, lane)
            print(road, road_id)
            if road == road_id:
                print('kkkkkkkkkkkkkkkkkkkkkkkk')
                advance_last_s, t, successor = cls.add_s(road_info, last_s, road, lane, previous_road)
                if not successor:
                    s = -s + advance_last_s
                else:
                    s = s + last_s
                road_info.reset()
                return s, t

            print(successor)
            last_s, t, successor = cls.add_s(road_info, last_s, road, lane, previous_road)
            count += 1
            print(count)
        print("s: ", s,"t: ", t)

    @classmethod
    def add_s(cls,road_info, last_s, road, lane, previous_road):
        lane_center = road_info.lane_center_point(int(road), int(lane))
        sections, successor = road_info.get_road_info(road, previous_road)
        print(road, successor)
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
        return s, t, successor

