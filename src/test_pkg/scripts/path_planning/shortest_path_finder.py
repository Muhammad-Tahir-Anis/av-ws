from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.map_parser_pkg.scripts.odr_map_obj import opendrive

class shortest_path:

    map_graph = []

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path_by_road_segments(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path_by_road_segments(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        if len(sp) == 2:
                            pass
                        else:
                            shortest_path = sp
        return shortest_path

    def get_shortest_path_by_length(self, shortest_path_list_length, possible_shortest_paths=[]):
        path_length: float = 0.0
        shortest_path_length: float = 0.0
        for lists in possible_shortest_paths:
            if len(lists) == shortest_path_list_length:
                for road_id in lists:
                    for roads in opendrive.road_list:
                        if roads.id == road_id:
                            road_length = float(roads.length)
                            path_length += road_length
                # print(path_length)
                if shortest_path_length == 0.0 or path_length < shortest_path_length:
                    shortest_path_length = path_length
                    print(shortest_path_length)
                    print(lists)


if __name__ == '__main__':
    routes = path_list()
    routes.make_list()
    route_graph = shortest_path(routes.map_graph)

    start = "0"
    end = "3"

    # all possible paths in the map from start to end point
    possible_shortest_paths = route_graph.get_paths(start, end)
    # shortest path by least no of road segments
    shortest_path = route_graph.get_shortest_path_by_road_segments(start, end)
    # length of list of shortest path for checking if there is other possible paths of the same no of road segments
    shortest_path_list_length = len(shortest_path)
    # shortest path by min total length of roads in each possible shortest paths
    route_graph.get_shortest_path_by_length(shortest_path_list_length, possible_shortest_paths)
