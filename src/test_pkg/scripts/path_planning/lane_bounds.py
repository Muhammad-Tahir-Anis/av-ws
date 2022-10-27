from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path


class bounds:

    @staticmethod
    def check_lane_bounds():
        routes = path_list
        routes.make_list()
        route_graph = shortest_path(routes.map_graph)
        start = "0"
        end = "3"

        path = []
        path = route_graph.get_shortest_path(start, end)
        bounds_list = []

        for p in path:
            for road in opendrive.road_list:
                if p == road.id:
                    if road.lanes.lanesection.left:
                        if road.lanes.lanesection.left.lane_list:
                            for lane in road.lanes.lanesection.left.lane_list:
                                if lane.type == "driving":
                                    if lane.width:
                                        bounds_list.append(list((road.id, lane.id)))
                    if road.lanes.lanesection.right:
                        if road.lanes.lanesection.right.lane_list:
                            for lane in road.lanes.lanesection.right.lane_list:
                                if lane.type == "driving":
                                    if lane.width:
                                        bounds_list.append(list((road.id, lane.id)))
        print(bounds_list)


if __name__ == '__main__':
    b = bounds()
    b.check_lane_bounds()

