from src.test_pkg.scripts.path_planning.Shortest_path_with_lanes import LaneList
from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation



class ObjectLocation:

    def __init__(self):
        pass

    @property
    def get_path(self):
        routes = path_list()
        routes.make_list()
        route_graph = shortest_path(routes.map_graph)

        starting_road_id = "0"
        end = "3"
        path = route_graph.get_shortest_path_by_road_segments(starting_road_id, end)

        start_lane = "-2"
        lane_path = LaneList()
        final_path_list = lane_path.lane_in_path(start_lane, path)
        return final_path_list

    @classmethod
    def get_Obstacle_location(cls, x, y):
        path = ObjectLocation()
        vehicle_path = path.get_path
        location = EgoLocation(x, y)
        print(location.road_id)
        print(vehicle_path)
        for road in vehicle_path:
            if road[0] == location.road_id:
                print(road[0], location.road_id)
                if int(road[1]) == int(location.lane_id):
                    print(road[1], location.lane_id)




