from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.logs import Log


class EgoLocation:
    def __init__(self):
        road_id = 0
        lane_id = 0

    @classmethod
    def get_ego_road(cls, x, y, heading, log: Log):
        x_origin = 0
        y_origin = 0
        curvature = 0
        s_value = 0
        roads = opendrive.road_list
        for road in roads:
            if road.planview.geometry_list:
                geometries = road.planview.geometry_list
                for geometry in geometries:
                    if geometries.index(geometry) < len(geometries) - 1:
                        next_geometry = geometries[geometries.index(geometry) + 1]
                        geometry.s = float(geometry.s)
                        next_geometry.s = float(next_geometry.s)
                    # if last geometry
                    elif geometries[len(geometries) - 1]:
                        pass
                    x_origin = geometry.x
                    y_origin = geometry.y
                    heading = geometry.hdg
                    s_value = geometry.s
                    if geometry.arc:
                        curvature = geometry.arc.curvature
                    else:
                        curvature = 0
            elif road.planview.geometry:
                geometry = road.planview.geometry
                x_origin = geometry.x
                y_origin = geometry.y
                heading = geometry.hdg
                s_value = geometry.s
                if geometry.arc:
                    curvature = geometry.arc.curvature
                else:
                    curvature = 0

            s, t = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value, log)

    @classmethod
    def get_max_min_t(cls, road_id):
        left_driving_lanes = []
        right_driving_lanes = []
        max_lane = 0
        min_lane = 0
        max_t = 0
        min_t = 0
        roads = opendrive.road_list
        for road in roads:
            if road_id == road.id:
                left_lane_section = road.lanes.lanesection.left
                if left_lane_section:
                    if left_lane_section.lane_list:
                        lane_list = left_lane_section.lane_list
                        for lane in lane_list:
                            if lane.type == "driving":
                                left_driving_lanes.append(float(lane.id))
                        max_lane = max(left_driving_lanes)
                        min_lane = min(left_driving_lanes)
                        # max_t =
                    elif left_lane_section.lane:
                        left_lane = left_lane_section.lane
                        max_t = float(left_lane.width.a)
                        min_t = 0
                right_lane_section = road.lanes.lanesection.right
                if right_lane_section:
                    if right_lane_section.lane_list:
                        lane_list = right_lane_section.lane_list
                        for lane in lane_list:
                            if lane.type == "driving":
                                right_driving_lanes.append(lane.id)
