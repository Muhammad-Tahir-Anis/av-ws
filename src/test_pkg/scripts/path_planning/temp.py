from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path


class lane_list:

    @classmethod
    def lane_in_path(cls, starting_road, starting_lane, end, shortest_path_list=None):
        cn = "start"
        next_lane = starting_lane
        previous_road: str = ""
        current_road: str = ""
        next_road: str = ""
        future_road: str = ""
        if shortest_path_list is None:
            shortest_path_list = []
        final_shortest_path = []

        for path in shortest_path_list:
            for roads in opendrive.road_list:
                if roads.id == path:
                    if roads.id == starting_road:
                        final_shortest_path.append(list((roads.id, starting_lane)))
                        previous_road = roads.id
                        if starting_lane < "0":
                            next_road = roads.link.predecessor.elementid
                            if roads.lanes.lanesection.left:
                                if roads.lanes.lanesection.left.lane_list:
                                    for lane in roads.lanes.lanesection.left.lane_list:
                                        if lane.id == starting_lane:
                                            if roads.link.predecessor.elementtype == "junction":
                                                for junction in opendrive.junction_list:
                                                    if junction.id == next_road:
                                                        for conn in junction.connection_list:
                                                            pass

                                            elif roads.link.predecessor.elementtype == "road":
                                                pass

                                elif roads.lanes.lanesection.left.lane:
                                    pass
                        elif starting_lane > "0":
                            next_road = roads.link.predecessor.elementid

                    elif roads.id == next_road:
                        pass


                    print(previous_road, current_road, next_road)


if __name__ == '__main__':
    routes = path_list()
    routes.make_list()
    route_graph = shortest_path(routes.map_graph)

    starting_road_id = "0"
    end = "3"
    path = route_graph.get_shortest_path(starting_road_id, end)

    start_lane = "-2"
    end_lane = "-2"
    lane_path = lane_list()
    final_path_list = lane_path.lane_in_path(starting_road_id, start_lane, end_lane, path)

    print(final_path_list)
