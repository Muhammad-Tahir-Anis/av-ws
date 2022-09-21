from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.path_planning.road_node import RoadNode, JunctionNode


class MapTree:
    roads = opendrive.road_list
    junctions = opendrive.junction_list
    map_tree: list = list()
    road_list: list = list()

    def __init__(self):
        pass

    # @classmethod
    # def traverse_map_flow(cls, id):
    #     print(id)
    #     is_road: bool = False
    #     for road in cls.roads:
    #         if id == road.id:
    #             cls.map_tree.append(id)
    #             is_road = True
    #             pass
    #     if not is_road:
    #         for junction in cls.junctions:
    #             if id == junction.id:
    #                 # junction_roads: list = list()
    #                 for connection in junction.connection_list:
    #                     # if len(cls.map_tree) >= 1:
    #                     if connection.incomingroad == cls.map_tree[len(cls.map_tree) - 1]:
    #                         cls.traverse_map_flow(connection.connectingroad)
    #                         # road_id = junction_roads.append(connection.connectingroad)
    #                     # else:
    #                     #     cls.traverse_map_flow(connection.connectingroad)
    #
    #     road_id = cls.next_road(id)
    #     if len(cls.map_tree) >= 2:
    #         if road_id == cls.map_tree[(len(cls.map_tree) - 2)]:
    #             road_id = cls.previse_road(cls.map_tree[len(cls.map_tree) - 1])
    #         # else:
    #         #     print(road_id)
    #     cls.traverse_map_flow(road_id)
    #
    # @classmethod
    # def next_road(cls, road_id):
    #     for road in cls.roads:
    #         if road.id == road_id:
    #             if road.link.successor.elementtype == "road":
    #                 return road.link.successor.elementid
    #
    # @classmethod
    # def previse_road(cls, road_id):
    #     for road in cls.roads:
    #         if road.id == road_id:
    #             if road.link.successor.elementtype == "road":
    #                 return road.link.predecessor.elementid

    @classmethod
    def road_node(cls, id):
        if not id in cls.road_list:
            for road in cls.roads:
                if road.id == id:
                    road_id = id
                    cls.road_list.append(road_id)
                    # previous_road = cls.road_node(road.link.predecessor.elementid)
                    # next_road = cls.road_node(road.link.successor.elementid)
                    previous_road = road.link.predecessor.elementid
                    next_road = road.link.successor.elementid
                    cls.map_tree.append(RoadNode(previous_road, road_id, next_road))
                    cls.road_node(previous_road)
                    cls.road_node(next_road)
                    # return RoadNode(previous_road, road_id, next_road)
            for junction in cls.junctions:
                if junction.id == id:
                    roads: list = list()
                    junction_id = id
                    # cls.map_tree.pop()
                    for connection in junction.connection_list:
                        # roads.append(connection.connectingroad)
                        cls.road_node(connection.connectingroad)
                    # return JunctionNode(junction_id, roads)
                    # cls.map_tree.append(JunctionNode(junction_id, roads))

    @classmethod
    def find_rout(cls, to, from_):
        if not to == from_:
            for roads in cls.map_tree:
                if to == roads.road_id:
                    print(roads.road_id)
                    to = roads.next_road
                    cls.find_rout(to, from_)


def main():
    tree = MapTree()
    tree.road_node("0")
    # for tree in tree.map_tree:
    #     print(tree.previous_road, tree.road_id, tree.next_road)
    tree.find_rout("0", "3")


if __name__ == '__main__':
    main()
