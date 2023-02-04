import numpy as np

from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation


class RoadInfo:
    successor = True

    def __init__(self):
        pass

    @classmethod
    def get_road_info(cls, road_id, previous_road_id):
        print(road_id, previous_road_id)
        # print(previous_road_id)
        information_list = []
        road_id = str(road_id)
        roads = opendrive.road_list
        road = [road for road in roads if road.id == road_id][0]

        # generating road information list
        geometries = road.planview.geometry_list
        if geometries:
            for geometry in geometries:
                x = geometry.x
                y = geometry.y
                length = geometry.length
                heading = geometry.hdg
                curvature = 0
                if geometry.arc:
                    curvature = geometry.arc.curvature
                information_list.append([x, y, length, heading, curvature])
        else:
            geometry = road.planview.geometry
            x = geometry.x
            y = geometry.y
            length = geometry.length
            heading = geometry.hdg
            curvature = 0
            if geometry.arc:
                curvature = geometry.arc.curvature
            information_list = [x, y, length, heading, curvature]
        information_list = np.float_(information_list)

        # decision for reversing the list
        junctions = opendrive.junction_list
        if previous_road_id:
            previous_road_id = str(previous_road_id)
            previous_road = [previous_road for previous_road in roads if previous_road.id == previous_road_id][0]
            if cls.successor:
                element_type = previous_road.link.successor.elementtype
                if element_type == 'road':
                    element_id = previous_road.link.successor.elementid
                    if element_id == road_id:
                        connecting_point = previous_road.link.successor.contactpoint
                        if connecting_point != 'start':
                            cls.successor = False
                            # information_list.reverse()
                            # if information_list.ndim != 1:
                            #     information_list = np.flip(information_list,0)

                elif element_type == 'junction':
                    element_id = previous_road.link.successor.elementid
                    junction = [junction for junction in junctions if junction.id == element_id][0]
                    connections = junction.connection_list
                    connection = [connection for connection in connections if
                                  connection.incomingroad == previous_road_id and connection.connectingroad == road_id][0]
                    if connection.contactpoint != 'start':
                        cls.successor = False
                        # information_list.reverse()
                        # if information_list.ndim != 1:
                        #     information_list = np.flip(information_list,0)

            else:
                # list will always flip until successor is false
                # if information_list.ndim != 1:
                #     information_list = np.flip(information_list,0)
                element_type = previous_road.link.predecessor.elementtype
                if element_type == 'road':
                    element_id = previous_road.link.predecessor.elementid
                    if element_id == road_id:
                        connecting_point = previous_road.link.predecessor.contactpoint
                        if connecting_point == 'start':
                            cls.successor = True
                            # information_list.reverse()
                            # if information_list.ndim != 1:
                            #     information_list = np.flip(information_list,0)

                elif element_type == 'junction':
                    element_id = previous_road.link.predecessor.elementid
                    junction = [junction for junction in junctions if junction.id == element_id][0]
                    connections = junction.connection_list
                    connection = [connection for connection in connections if
                                  connection.incomingroad == previous_road_id and connection.connectingroad == road_id][0]

                    if connection.contactpoint == 'start':
                        cls.successor = True
                        # information_list.reverse()
                        # if information_list.ndim != 1:
                        #     information_list = np.flip(information_list,0)

        # print(road_id, information_list)
        print(cls.successor)
        return information_list, cls.successor

    @classmethod
    def reset(cls):
        cls.successor = True

    @classmethod
    def get_t_range(cls, road_id: int, lane_id: int):
        road_id = str(road_id)
        lanes_list = cls.get_lanes_list_with_t_range(road_id)
        for lane in lanes_list:
            if lane[0] == lane_id:
                return lane[1], lane[2]

    @classmethod
    def get_lanes_list_with_t_range(cls, road_id):
        left_lanes_list = []
        right_lanes_list = []
        roads = opendrive.road_list
        for road in roads:
            if road.id == road_id:
                lane_offsets = road.lanes.laneoffset_list
                if lane_offsets:
                    lane_offset = float(lane_offsets[0].a)
                else:
                    lane_offset = float(road.lanes.laneoffset.a)

                left_lane_section = road.lanes.lanesection.left
                if left_lane_section:
                    left_lanes_list = cls.get_lane_list_with_t(left_lane_section, lane_offset)

                right_lane_section = road.lanes.lanesection.right
                if right_lane_section:
                    right_lanes_list = cls.get_lane_list_with_t(right_lane_section, lane_offset)

                lanes_list = left_lanes_list + right_lanes_list
                return lanes_list

    @classmethod
    def get_lane_list_with_t(cls, lane_section, lane_offset):
        lanes_list = []
        t = lane_offset
        if lane_section.lane_list:
            lane_list = lane_section.lane_list
            lane_id = lane_list[0].id
            lane_id = float(lane_id)
            # for left lanes
            if lane_id > 0:
                lane_list.reverse()
                for lane in lane_list:
                    if lane.width_list:
                        lanes_list.append((float(lane.id), t, t + float(lane.width_list[0].a)))
                        t = t + float(lane.width_list[0].a)
                    else:
                        lanes_list.append((float(lane.id), t, t + float(lane.width.a)))
                        t = t + float(lane.width.a)
                lane_list.reverse()
            # for right lanes
            elif lane_id < 0:
                for lane in lane_list:
                    if lane.width_list:
                        lanes_list.append((float(lane.id), t, t - float(lane.width_list[0].a)))
                        t = t - float(lane.width_list[0].a)
                    else:
                        lanes_list.append((float(lane.id), t, t - float(lane.width.a)))
                        t = t - float(lane.width.a)
        else:
            lane_id = float(lane_section.lane.id)
            # for left lane
            if lane_id > 0:
                if lane_section.lane.width_list:
                    lanes_list.append((float(lane_section.lane.id), t, t + float(lane_section.lane.width_list[0].a)))
                    t = t + float(lane_section.lane.width_list[0].a)
                else:
                    lanes_list.append((float(lane_section.lane.id), t, t + float(lane_section.lane.width.a)))
                    t = t + float(lane_section.lane.width.a)
            # for right lane
            elif lane_id < 0:
                if lane_section.lane.width_list:
                    lanes_list.append((float(lane_section.lane.id), t, t - float(lane_section.lane.width_list[0].a)))
                    t = t - float(lane_section.lane.width_list[0].a)
                else:
                    lanes_list.append((float(lane_section.lane.id), t, t - float(lane_section.lane.width.a)))
                    t = t - float(lane_section.lane.width.a)
        return lanes_list

    @classmethod
    def get_road_origin(cls, road_id: int):
        road_id = str(road_id)
        roads = opendrive.road_lis
        for road in roads:
            if road.id == road_id:
                if road.planview.geometry:
                    x = road.planview.geometry.x
                    y = road.planview.geometry.y
                    heading = road.planview.geometry.hdg
                    return x, y, heading
                if road.planview.geometry_list:
                    x = road.planview.geometry_list[0].x
                    y = road.planview.geometry_list[0].y
                    heading = road.planview.geometry_list[0].hdg
                    return x, y, heading

    @classmethod
    def get_new_curvature(cls, curvature, offset):
        # curvature = 1/radius
        radius = 1 / curvature
        new_radius = radius + offset
        new_curvature = 1 / new_radius

    @classmethod
    def lane_center_point(cls, road_id, lane_id):
        t_range = cls.get_t_range(road_id, lane_id)
        center_point = t_range[0] + ((t_range[1] - t_range[0]) / 2)
        return center_point


if __name__ == '__main__':
    road_info = RoadInfo()
