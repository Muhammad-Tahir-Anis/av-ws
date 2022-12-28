from src.test_pkg.scripts.path_planning.path_list_maker import path_list
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.path_planning.Shortest_path_with_lanes import lane_list
from src.test_pkg.scripts.path_planning.shortest_path_finder import shortest_path
from src.test_pkg.scripts.Obstacle_avoidance.npc_distance_finder import NpcDistanceFinder
from src.test_pkg.scripts.object_detection.save_npc_data import NpcDataStorage


class DetectObstacle:

    def __init__(self):
        self.distance = NpcDistanceFinder()
        pass

    @property
    def get_path(self):
        routes = path_list()
        routes.make_list()
        route_graph = shortest_path(routes.map_graph)

        starting_road_id = "0"
        end = "3"
        path = route_graph.get_shortest_path_by_road_segments(starting_road_id, end)

        start_lane = "2"
        lane_path = lane_list()
        final_path_list = lane_path.lane_in_path(start_lane, path)

        # print(final_path_list)
        return final_path_list

    def get_Obstacle_location(self, x, y):
        print("x", x, "y", y)
        path = DetectObstacle()
        vehicle_path = path.get_path
        location = EgoLocation(x, y)
        obstacle_road_id = location.road_id
        obstacle_lane_id = location.lane_id
        for road in vehicle_path:
            if road[0] == str(obstacle_road_id):
                print("road: ", road[0], str(obstacle_road_id))
            if float(road[1]) == obstacle_lane_id:
                print("lane: ", road[1], str(location.lane_id))
        s, t = location.get_ego_location_st
        s, t = self.distance.get_unique_st(s, t, obstacle_road_id)
        npc_data = obstacle_road_id, obstacle_lane_id, s
        save_data = NpcDataStorage()
        save_data.save_object(npc_data)
        data = save_data.load_object("data.pickle")
        print(data)
