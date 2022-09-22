from src.map_parser_pkg.scripts.odr_map_obj import opendrive

map_graph = []

for roads in opendrive.road_list:
    if roads.link.successor.elementtype == "road":
        map_graph.append(list((roads.id, roads.link.successor.elementid, False)))
    elif roads.link.successor.elementtype == "junction":
        for junction in opendrive.junction_list:
            if junction.id == roads.link.successor.elementid:
                for connections in junction.connection_list:
                    if connections.incomingroad == roads.id:
                        map_graph.append(list((roads.id, connections.connectingroad, False)))
    elif roads.link.predecessor.elementid == "road":
        map_graph.append(list((roads.id, roads.link.predecessor.elementid, False)))
    elif roads.link.predecessor.elementtype == "junction":
        for junction in opendrive.junction_list:
            if junction.id == roads.link.predecessor.elementid:
                for connections in junction.connection_list:
                    if connections.incomingroad == roads.id:
                        map_graph.append(list((roads.id, connections.connectingroad, False)))


# def path(from_, to):
#     new_list = []
#     for node in map_graph:
#         if from_ in node[0]:
#             new_list.append()




print(path("0", "3"))

for node in map_graph:
    print(node)
