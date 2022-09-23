from src.map_parser_pkg.scripts.odr_map_obj import opendrive

map_graph = []


def check_driving_lanes(road):
    is_driving = False  # For selecting roads that have driving lanes also
    # Checking if left lanes have any driving lane
    if road.lanes.lanesection.left:
        if road.lanes.lanesection.left.lane_list:
            for lane in road.lanes.lanesection.left.lane_list:
                if lane.type == "driving":
                    is_driving = True
        else:
            if road.lanes.lanesection.left.lane.type == "driving":
                is_driving = True
    # Checking if center lanes have any driving lane
    if road.lanes.lanesection.center:
        if road.lanes.lanesection.center.lane.type == "driving":
            is_driving = True
    # Checking if right have any driving lane
    if road.lanes.lanesection.right:
        if road.lanes.lanesection.right.lane_list:
            for lane in road.lanes.lanesection.right.lane_list:
                if lane.type == "driving":
                    is_driving = True
        else:
            if road.lanes.lanesection.right.lane.type == "driving":
                is_driving = True
    # If is there any driving lane than add that road to the graph

    return is_driving


for roads in opendrive.road_list:
    if roads.link.successor.elementtype == "road":
        for road in opendrive.road_list:
            if roads.link.successor.elementid == road.id:
                if check_driving_lanes(roads) and check_driving_lanes(road):
                    map_graph.append(list((roads.id, roads.link.successor.elementid, False)))
    elif roads.link.successor.elementtype == "junction":
        for junction in opendrive.junction_list:
            if junction.id == roads.link.successor.elementid:
                for connections in junction.connection_list:
                    if connections.incomingroad == roads.id:
                        for road in opendrive.road_list:
                            if connections.connectingroad == road.id:
                                if check_driving_lanes(roads) and check_driving_lanes(road):
                                    map_graph.append(list((roads.id, connections.connectingroad, False)))
    if roads.link.predecessor.elementtype == "road":
        for road in opendrive.road_list:
            if roads.link.predecessor.elementid == road.id:
                if check_driving_lanes(roads) and check_driving_lanes(road):
                    map_graph.append(list((roads.id, roads.link.predecessor.elementid, False)))
    elif roads.link.predecessor.elementtype == "junction":
        for junction in opendrive.junction_list:
            if junction.id == roads.link.predecessor.elementid:
                for connections in junction.connection_list:
                    if connections.incomingroad == roads.id:
                        for road in opendrive.road_list:
                            if connections.connectingroad == road.id:
                                if check_driving_lanes(roads) and check_driving_lanes(road):
                                    map_graph.append(list((roads.id, connections.connectingroad, False)))

map_graph_2 = []
for data in map_graph:
    my_list = []
    if data[0] not in [graph[0] for graph in map_graph_2]:
        # map_graph_2.append(data[0])
        for graph_data in map_graph:
            if data[0] == graph_data[0]:
                if graph_data[1] not in my_list:
                    my_list.append(graph_data[1])
            if data[0] == graph_data[1]:
                if graph_data[0] not in my_list:
                    my_list.append(graph_data[0])
        map_graph_2.append([data[0], my_list])

new_list = []


# for data in map_graph_2:
#     print(data)
# print("___________________________")


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    print(path)
    if start == end:
        return [path]
    if not start in [data[0] for data in graph]:
        return []
    paths = []
    for data in graph:
        if start == data[0]:
            for node in data[1]:
                if node not in path:
                    newpath = find_all_paths(graph, node, end, path)
                    if newpath:
                        if not paths or len(newpath) < len(paths):
                            shortest = newpath
    return paths


print(find_all_paths(map_graph_2, "0", "3"))
# find_all_paths(my_graph,0,3)
# for node in map_graph:
#     print(node)
