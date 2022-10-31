from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.logs import Log


class EgoLocation:
    def __init__(self):
        road_id = 0
        lane_id = 0

    @classmethod
    def get_ego_road(cls, x, y, log: Log):
        global axis
        x_origin = 0
        y_origin = 0
        curvature = 0
        s_value = 0
        geometry_length = 0

        # A point P is a point on coordinates where vehicle is located
        point_p = (x, y)
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
                        axis = AxisTransformation(x_origin, y_origin, x_origin, y_origin, heading, curvature, s_value,
                                                  log)
                        max_t, min_t = cls.get_t_values(road)

                        # Rectangle points A,B,C,D
                        rect_side_a, rect_side_b, rect_side_c, rect_side_d = axis.get_boundaries(max_t, min_t,
                                                                                                 geometry_length)

                        triangle_abc = cls.is_point_lies_in_triangle(point_p, rect_side_a, rect_side_b, rect_side_c)

                        s, t = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value,
                                                  log).s_t_axis
                        if triangle_abc:
                            print(road.id, t)
                        triangle_adc = cls.is_point_lies_in_triangle(point_p, rect_side_a, rect_side_d, rect_side_c)
                        if triangle_adc:
                            print(road.id, t)
            elif road.planview.geometry:
                geometry = road.planview.geometry
                x_origin = float(geometry.x)
                y_origin = float(geometry.y)
                heading = float(geometry.hdg)
                s_value = float(geometry.s)
                geometry_length = float(geometry.length)
                if geometry.arc:
                    curvature = float(geometry.arc.curvature)
                else:
                    curvature = 0
                    axis = AxisTransformation(x_origin, y_origin, x_origin, y_origin, heading, curvature, s_value, log)
                    max_t, min_t = cls.get_t_values(road)

                    # Rectangle points A,B,C,D
                    rect_side_a, rect_side_b, rect_side_c, rect_side_d = axis.get_boundaries(max_t, min_t,
                                                                                             geometry_length)
                    # Let's make two triangles ABC and ADC
                    triangle_abc = cls.is_point_lies_in_triangle(point_p, rect_side_a, rect_side_b, rect_side_c)

                    s, t = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value,
                                              log).s_t_axis
                    if triangle_abc:
                        print(road.id, t)
                    triangle_abd = cls.is_point_lies_in_triangle(point_p, rect_side_a, rect_side_b, rect_side_d)
                    if triangle_abd:
                        print(road.id, t)

    @classmethod
    def get_lane_id(cls, road_id, t):
        left_lanes_list = []
        right_lanes_list = []
        roads = opendrive.road_list
        for road in roads:
            if road.id == road_id:
                left_lane_section = road.lanes.lanesection.left
                lane_offsets = road.lanes.laneoffset_list
                if lane_offsets:
                    lane_offset = float(lane_offsets[0].a)
                else:
                    lane_offset = float(road.lanes.laneoffset.a)
                if left_lane_section:
                    left_lanes_list = cls.get_lane_list_with_t(left_lane_section)
                right_lane_section = road.lanes.lanesection.right
                if right_lane_section:
                    right_lanes_list = cls.get_lane_list_with_t(right_lane_section)


    @classmethod
    def get_lane_list_with_t(cls, lane_section):
        lanes_list = []
        t = 0
        if lane_section.lane_list:
            lane_list = lane_section.lane_list
            for lane in lane_list:
                if lane.width_list:
                    lanes_list.append((float(lane.id), t, lane.width_list[0].a))
                    t = t + float(lane.width_list[0].a)
                else:
                    lanes_list.append((float(lane.id), t, float(lane.width.a)))
                    t = t + float(lane.width.a)
        else:
            if lane_section.lane.width_list:
                lanes_list.append((float(lane_section.lane.id), t, float(lane_section.lane.width_list[0].a)))
                t = t + float(lane_section.lane.width_list[0].a)
            else:
                lanes_list.append((float(lane_section.lane.id), t, float(lane_section.lane.width.a)))
                t = t + float(lane_section.lane.width.a)
        return lanes_list

    @classmethod
    def is_point_lies_in_triangle(cls, point_p, point_a, point_b, point_c):
        is_point_lies_in = False
        # Triangle ABC
        area_of_tri_abc = cls.area_of_rectangle(point_a, point_b, point_c)

        # creating 3 more triangles with point P that are PAB PAD PBD

        # Triangle PAB
        area_of_tri_pab = cls.area_of_rectangle(point_p, point_a, point_b)

        # Triangle PAC
        area_of_tri_pac = cls.area_of_rectangle(point_p, point_a, point_c)

        # Triangle PBC
        area_of_tri_pbc = cls.area_of_rectangle(point_p, point_b, point_c)

        # Check if point P lies in Triangle ABD
        # If yes than sum of the areas of Triangle PAB PAC PBC are equal to area of Triangle ABC
        sum_of_p_triangles = area_of_tri_pab + area_of_tri_pac + area_of_tri_pbc
        if area_of_tri_abc != sum_of_p_triangles:
            is_point_lies_in = False
        else:
            is_point_lies_in = True
        return is_point_lies_in

    @classmethod
    def area_of_rectangle(cls, point_a, point_b, point_c):
        side_a = point_a[0] * (point_b[1] - point_c[1])
        side_b = point_b[0] * (point_c[1] - point_a[1])
        side_c = point_c[0] * (point_a[1] - point_b[1])
        area_of_triangle = abs((side_a + side_b + side_c) / 2)
        return area_of_triangle

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
                if not left_driving_lanes:
                    max_lane = 0
                    min_lane = 0
                else:
                    max_lane = max(left_driving_lanes)
                    min_lane = min(left_driving_lanes)
                # print(max_lane, min_lane)

                # left lanes list is like [3,2,1] so we need to reverse it to get correct t axis values
                lane_list.reverse()
                left_max_t = cls.get_max_t(max_lane, lane_list)
                left_min_t = cls.get_min_t(min_lane, lane_list)

                if road.lanes.laneoffset_list:
                    lane_offset = float(road.lanes.laneoffset_list[0].a)
                elif road.lanes.laneoffset:
                    lane_offset = float(road.lanes.laneoffset.a)
                # print(lane_offset)
                left_max_t = left_max_t + lane_offset
                left_min_t = left_min_t + lane_offset

                # print(left_max_t, left_min_t)

            elif left_lane_section.lane:
                left_lane = left_lane_section.lane
                if left_lane.width_list:
                    left_max_t = float(left_lane.width_list[0].a)
                elif left_lane.width:
                    left_max_t = float(left_lane.width.a)
                left_min_t = 0  # Add lane offset

        right_lane_section = road.lanes.lanesection.right
        if right_lane_section:
            if right_lane_section.lane_list:
                lane_list = right_lane_section.lane_list
                # take id of driving lanes only
                right_driving_lanes = [float(lane.id) for lane in lane_list if lane.type == "driving"]
                if not right_driving_lanes:
                    max_lane = 0
                    min_lane = 0
                else:
                    max_lane = min(right_driving_lanes)
                    min_lane = max(right_driving_lanes)
                # print(max_lane, min_lane)

                right_max_t = cls.get_max_t(max_lane, lane_list)
                right_min_t = cls.get_min_t(min_lane, lane_list)

                if road.lanes.laneoffset_list:
                    lane_offset = 0
                elif road.lanes.laneoffset:
                    lane_offset = float(road.lanes.laneoffset.a)

                # print(lane_offset)
                right_max_t = right_max_t - lane_offset
                right_min_t = right_min_t - lane_offset
            elif right_lane_section.lane:
                right_lane = right_lane_section.lane
                if right_lane.width_list:
                    right_max_t = float(right_lane.width_list[0].a)
                elif right_lane.width:
                    right_max_t = float(right_lane.width.a)
                right_min_t = 0  # Add lane offset

            # print(right_max_t, right_min_t)

        return left_max_t, -right_max_t

    @classmethod
    def get_max_t(cls, max_lane, lanes):
        # t is an axis along the width of a road
        global max_t
        t = 0
        lane_width = 0
        for lane in lanes:
            # print("max: ", t)
            if lane.width_list:
                lane_width = float(lane.width_list[0].a)
            elif lane.width:
                lane_width = float(lane.width.a)
            t = t + lane_width
            if max_lane == float(lane.id):
                max_t = t
                return max_t
            else:
                max_t = 0
        return max_t

    @classmethod
    def get_min_t(cls, min_lane, lanes):
        # t is an axis along the width of a road
        global min_t
        t = 0
        lane_width = 0
        for lane in lanes:
            # print("min: ", t)
            if lane.width_list:
                lane_width = float(lane.width_list[0].a)
            elif lane.width:
                lane_width = float(lane.width.a)
            t = t + lane_width
            if min_lane == float(lane.id):
                min_t = t - lane_width
                return min_t
            else:
                min_t = 0
        return min_t

    @classmethod
    def get_t_range(cls, lane_list, lane_id):
        max_t = 0
        min_t = 0
        t = 0

        for lane in lane_list:
            min_t = t
            if lane.id == lane_id:
                t = t + float(lane.width.a)
                max_t = t
            else:
                t = t + float(lane.width.a)


eg = EgoLocation()
log = Log()
# for road in opendrive.road_list:
#     if road.id == "0":
#         print(eg.get_t_values(road))
print(eg.get_ego_road(float(1.0464652330011117e+2), float(4.4613107285925366e+0), log))
