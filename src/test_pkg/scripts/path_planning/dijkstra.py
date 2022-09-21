from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class MapTree:
    roads = opendrive.road_list
    junctions = opendrive.junction_list
    map_tree: list = list()

    def __init__(self):
        pass

    @classmethod
    def traverse_map_flow(cls, id):
        print(id)
        is_road: bool = False
        for road in cls.roads:
            if id == road.id:
                cls.map_tree.append(id)
                is_road = True
                pass
        if not is_road:
            for junction in cls.junctions:
                if id == junction.id:
                    print("junction" + id)
                    # junction_roads: list = list()
                    for connection in junction.connection_list:
                        # if len(cls.map_tree) >= 1:
                        if connection.incomingroad == cls.map_tree[len(cls.map_tree) - 1]:
                            cls.traverse_map_flow(connection.connectingroad)

        road_id = cls.next_road(id)
        if len(cls.map_tree) >= 2:
            if road_id == cls.map_tree[len(cls.map_tree) - 2]:
                road_id = cls.previse_road(cls.map_tree[len(cls.map_tree) -1])
                cls.traverse_map_flow(road_id)
            elif road_id == "0":
                pass
            else:
                cls.traverse_map_flow(road_id)
        else:
            cls.traverse_map_flow(road_id)

    @classmethod
    def next_road(cls, id):
        for road in cls.roads:
            if road.id == id:
                if road.link.successor.elementtype == "road":
                    return road.link.successor.elementid
                elif road.link.successor.elementtype == "junction":
                    return road.link.successor.elementid

    @classmethod
    def previse_road(cls, road_id):
        for road in cls.roads:
            if road.id == road_id:
                if road.link.successor.elementtype == "road":
                    return road.link.predecessor.elementid
                elif road.link.predecessor.elementtype == "junction":
                    return road.link.predecessor.elementid


def main():
    map_tree = MapTree()
    map_tree.traverse_map_flow("0")


if __name__ == '__main__':
    main()
