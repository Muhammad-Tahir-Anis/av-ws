from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path


class lane_list:

    @classmethod
    def lane_in_path(cls, starting_lane, shortest_path_list=None):
        if shortest_path_list is None:
            shortest_path_list = []
        final_shortest_path = []
        for path in shortest_path_list:
            for roads in opendrive.road_list:
                if roads.id == path:
                    current_road = roads.id
                    if starting_lane == "2" or starting_lane == "1" or starting_lane == "4" or starting_lane == "5":
                        next_road = roads.link.predecessor.elementid
                        if roads.link.predecessor.elementtype == "junction":
                            for junction in opendrive.junction_list:
                                if junction.id == next_road:
                                    for conn in junction.connection_list:
                                        for road_id in shortest_path_list:
                                            if conn.connectingroad == road_id:
                                                if conn.lanelink:
                                                    starting_lane = conn.lanelink.to
                            final_shortest_path.append(list((current_road, starting_lane)))
                        elif roads.link.predecessor.elementtype == "road":
                            final_shortest_path.append(list((current_road, starting_lane)))
                            if roads.lanes.lanesection.left.lane_list:
                                for lane in roads.lanes.lanesection.left.lane_list:
                                    if lane.id == starting_lane:
                                        starting_lane = lane.link.predecessor.id
                            elif roads.lanes.lanesection.left.lane:
                                starting_lane = roads.lanes.lanesection.left.lane.link.predecessor.id
                    elif starting_lane == "-2" or starting_lane == "-1" or starting_lane == "-4" or starting_lane == "-5":
                        next_road = roads.link.successor.elementid
                        if roads.link.successor.elementtype == "junction":
                            for junction in opendrive.junction_list:
                                if junction.id == next_road:
                                    for conn in junction.connection_list:
                                        for road_id in shortest_path_list:
                                            if conn.connectingroad == road_id:
                                                if conn.lanelink:
                                                    starting_lane = conn.lanelink.from_
                            final_shortest_path.append(list((current_road, starting_lane)))
                        elif roads.link.successor.elementtype == "road":
                            final_shortest_path.append(list((current_road, starting_lane)))
                            if roads.lanes.lanesection.right.lane_list:
                                for lane in roads.lanes.lanesection.right.lane_list:
                                    if lane.id == starting_lane:
                                        starting_lane = lane.link.successor.id
                            elif roads.lanes.lanesection.right.lane:
                                starting_lane = roads.lanes.lanesection.right.lane.link.successor.id
        return final_shortest_path


if __name__ == '__main__':
    routes = path_list()
    routes.make_list()
    route_graph = shortest_path(routes.map_graph)

    starting_road_id = "0"
    end = "13"
    path = route_graph.get_shortest_path_by_road_segments(starting_road_id, end)

    start_lane = "2"
    lane_path = lane_list()
    final_path_list = lane_path.lane_in_path(start_lane, path)

    print(final_path_list)