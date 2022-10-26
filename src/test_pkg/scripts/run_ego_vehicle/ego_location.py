from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.logs import Log


class EgoLocation:
    def __init__(self):
        road_id = 0
        lane_id = 0

    @classmethod
    def get_ego_road(cls, x, y, log: Log):
        x_origin = 0
        y_origin = 0
        curvature = 0
        s_value = 0
        geometry_length = 0
        roads = opendrive.road_list
        for road in roads:
            if road.planview.geometry_list:
                geometries = road.planview.geometry_list
                for geometry in geometries:
                    x_origin = float(geometry.x)
                    y_origin = float(geometry.y)
                    heading = float(geometry.hdg)
                    s_value = float(geometry.s)
                    geometry_length = float(geometry.length)
                    if geometry.arc:
                        curvature = float(geometry.arc.curvature)
                    else:
                        curvature = 0
                        axis = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value, log)
                        max_t, min_t = cls.get_t_values(road)
                        # print(axis.get_boundaries(max_t, min_t, geometry_length))

            elif road.planview.geometry:
                geometry = road.planview.geometry
                x_origin = float(geometry.x)
                y_origin = float(geometry.y)
                heading = float(geometry.hdg)
                s_value = float(geometry.s)
                if geometry.arc:
                    curvature = float(geometry.arc.curvature)
                else:
                    curvature = 0
                    axis = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value, log)
                    max_t, min_t = cls.get_t_values(road)
                    # print(axis.get_boundaries(max_t, min_t, geometry_length))

            # s, t = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value, log)

    @classmethod
    def get_t_values(cls, road):
        left_driving_lanes = []
        right_driving_lanes = []
        lanes_width = 0
        lane_offset = 0
        max_lane = 0
        min_lane = 0
        left_max_t = 0
        left_min_t = 0
        right_min_t = 0
        right_max_t = 0

        left_lane_section = road.lanes.lanesection.left
        if left_lane_section:
            if left_lane_section.lane_list:
                lane_list = left_lane_section.lane_list
                # take id of driving lanes only
                left_driving_lanes = [float(lane.id) for lane in lane_list if lane.type == "driving"]
                max_lane = max(left_driving_lanes)
                min_lane = min(left_driving_lanes)
                print(max_lane, min_lane)

                # left lanes list is like [3,2,1] so we need to reverse it to get correct t axis values
                lane_list.reverse()
                left_max_t = cls.get_max_t(max_lane, lane_list)
                left_min_t = cls.get_min_t(min_lane, lane_list)

                if road.lanes.laneoffset_list:
                    lane_offset = 0
                elif road.lanes.laneoffset:
                    lane_offset = float(road.lanes.laneoffset.a)
                print(lane_offset)
                left_max_t = left_max_t + lane_offset
                left_min_t = left_min_t + lane_offset

                print(left_max_t, left_min_t)

            elif left_lane_section.lane:
                left_lane = left_lane_section.lane
                max_t = float(left_lane.width.a)
                min_t = 0  # Add lane offset

        right_lane_section = road.lanes.lanesection.right
        if right_lane_section:
            if right_lane_section.lane_list:
                lane_list = right_lane_section.lane_list
                # take id of driving lanes only
                right_driving_lanes = [float(lane.id) for lane in lane_list if lane.type == "driving"]
                max_lane = min(right_driving_lanes)
                min_lane = max(right_driving_lanes)
                print(max_lane, min_lane)

                right_max_t = cls.get_max_t(max_lane, lane_list)
                right_min_t = cls.get_min_t(min_lane, lane_list)

                if road.lanes.laneoffset_list:
                    lane_offset = 0
                elif road.lanes.laneoffset:
                    lane_offset = float(road.lanes.laneoffset.a)

                print(lane_offset)
                right_max_t = right_max_t - lane_offset
                right_min_t = right_min_t - lane_offset
                print(right_max_t, right_min_t)

        return left_max_t, right_max_t

    @classmethod
    def get_max_t(cls, max_lane, lanes):
        # t is an axis along the width of a road
        t = 0
        for lane in lanes:
            print("max: ", t)
            t = t + float(lane.width.a)
            if max_lane == float(lane.id):
                max_t = t
                return max_t

    @classmethod
    def get_min_t(cls, min_lane, lanes):
        # t is an axis along the width of a road
        t = 0
        for lane in lanes:
            print("min: ", t)
            t = t + float(lane.width.a)
            if min_lane == float(lane.id):
                min_t = t - float(lane.width.a)
                return min_t


eg = EgoLocation()
for road in opendrive.road_list:
    if road.id == "20":
        print(eg.get_t_values(road))
