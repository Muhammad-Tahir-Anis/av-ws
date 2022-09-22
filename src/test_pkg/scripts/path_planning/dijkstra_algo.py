from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class algo:
    map_graph = []

    def __int__(self):
        pass

    @classmethod
    def make_list(cls):
        for roads in opendrive.road_list:
            if roads.link.successor.elementtype == "road":
                cls.map_graph.append(list((roads.id, roads.link.successor.elementid, False)))
            elif roads.link.successor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.successor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                cls.map_graph.append(list((roads.id, connections.connectingroad, False)))
            elif roads.link.predecessor.elementid == "road":
                cls.map_graph.append(list((roads.id, roads.link.predecessor.elementid, False)))
            elif roads.link.predecessor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.predecessor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                cls.map_graph.append(list((roads.id, connections.connectingroad, False)))


# def path(from_, to):
#     new_list = []
#     for node in map_graph:
#         if from_ in node[0]:
#             new_list.append()


#
# print(path("0", "3"))
#
# for node in map_graph:
#     print(node)

def main():
    route = algo()
    route.make_list()
    # route.localize_map("-2.7782101881329197e+1")
    for data in route.map_graph:
        print(data)


if __name__ == '__main__':
    main()
