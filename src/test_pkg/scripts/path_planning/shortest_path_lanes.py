from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path


class lane_list:

    @classmethod
    def lane_in_path(cls, starting_lane, end, shortest_road_list=None):
        cn = "start"
        current_lane = starting_lane
        if shortest_road_list is None:
            shortest_road_list = []
        final_shortest_path = []

        for R in shortest_road_list:
            for roads in opendrive.road_list:
                if roads.id == R:
                    # print(roads.id, start)
                    if starting_lane == "2" or starting_lane == "1":
                        if cn == "start":
                            if roads.link.predecessor.elementtype == "junction":
                                for junctions in opendrive.junction_list:
                                    if junctions.id == roads.link.predecessor.elementid:
                                        for conn in junctions.connection_list:
                                            if conn.incomingroad == roads.id:
                                                for p in shortest_road_list:
                                                    if p == conn.connectingroad:
                                                        if conn.lanelink:
                                                            current_lane = conn.lanelink.to
                                                            starting_lane = conn.lanelink.from_
                                                            cn = conn.contactpoint
                            elif roads.link.predecessor.elementtype == "road":
                                for road in opendrive.road_list:
                                    if road.id == roads.link.predecessor.elementid:
                                        if road.lanes.lanesection.left and road.lanes.lanesection.left.lane_list:
                                            for lanes in road.lanes.lanesection.left.lane_list:
                                                if lanes.id == starting_lane and lanes.link:
                                                    current_lane = starting_lane
                                                    starting_lane = lanes.link.successor.id
                        elif cn == "end":
                            current_lane = starting_lane
                            starting_lane = "-1"
                            cn = "start"
                    elif starting_lane == "-2" or starting_lane == "-1":
                        if roads.lanes.lanesection.right and roads.lanes.lanesection.right.lane_list:
                            for lanes in roads.lanes.lanesection.right.lane_list:
                                if lanes.id == starting_lane and lanes.link:
                                    current_lane = lanes.id
                                    starting_lane = lanes.link.successor.id
                    if R == str(shortest_road_list[-1]):
                        current_lane = end
                        final_shortest_path.append(list((roads.id, current_lane)))
                    else:
                        final_shortest_path.append(list((roads.id, current_lane)))
                        current_lane = starting_lane
        return final_shortest_path


if __name__ == '__main__':
    routes = path_list()
    routes.make_list()
    route_graph = shortest_path(routes.map_graph)

    start = "0"
    end = "3"
    path = route_graph.get_shortest_path(start, end)

    start_lane = "-2"
    end_lane = "-2"
    lane_path = lane_list()
    final_path_list = lane_path.lane_in_path(start_lane, end_lane, path)

    print(final_path_list)
