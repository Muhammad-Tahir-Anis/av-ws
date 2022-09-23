from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class algo:
    map_graph = []

    def __int__(self):
        pass



    @classmethod
    def make_list(cls):
        for roads in opendrive.road_list:
            if roads.link.successor.elementtype == "road":
                cls.map_graph.append(list((roads.id, roads.link.successor.elementid)))
            elif roads.link.successor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.successor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                cls.map_graph.append(list((roads.id, connections.connectingroad)))
            if roads.link.predecessor.elementid == "road":
                cls.map_graph.append(list((roads.id, roads.link.predecessor.elementid)))
            elif roads.link.predecessor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.predecessor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                cls.map_graph.append(list((roads.id, connections.connectingroad, False)))





def main():
    route = algo()
    route.make_list()
    for data in route.map_graph:
        print(data)

    # l = 1.1992999999999999e+2
    # l1 = float(4.5320610542389453e+1)
    # l2 = float(3.2221759014301284e+1)
    # l3 = float(3.3174042248452480e+1)
    # l4 = float(9.2135881948567686e+0)
    # l5 = l1 + l2 + l3 + l4
    # print(float(l))
    # print(l5)


if __name__ == '__main__':
    main()
