from src.map_parser_pkg.scripts.odr_map_obj import opendrive


class path_list:
    map_graph = []
    nodes = []

    def __int__(self):
        pass

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

    @classmethod
    def make_list(cls):
        for roads in opendrive.road_list:
            if roads.link.successor.elementtype == "road":
                for road in opendrive.road_list:
                    if roads.link.successor.elementid == road.id:
                        cls.map_graph.append(list((roads.id, roads.link.successor.elementid)))
            elif roads.link.successor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.successor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                for road in opendrive.road_list:
                                    if connections.connectingroad == road.id:
                                        if cls.check_driving_lanes(roads) and cls.check_driving_lanes(road):
                                            cls.map_graph.append(list((roads.id, connections.connectingroad)))
            if roads.link.predecessor.elementtype == "road":
                for road in opendrive.road_list:
                    if roads.link.predecessor.elementid == road.id:
                        if cls.check_driving_lanes(roads) and cls.check_driving_lanes(road):
                            cls.map_graph.append(list((roads.id, roads.link.predecessor.elementid)))
            elif roads.link.predecessor.elementtype == "junction":
                for junction in opendrive.junction_list:
                    if junction.id == roads.link.predecessor.elementid:
                        for connections in junction.connection_list:
                            if connections.incomingroad == roads.id:
                                for road in opendrive.road_list:
                                    if connections.connectingroad == road.id:
                                        if cls.check_driving_lanes(roads) and cls.check_driving_lanes(road):
                                            cls.map_graph.append(list((roads.id, connections.connectingroad)))


def main():
    route = path_list()
    route.make_list()


if __name__ == '__main__':
    main()