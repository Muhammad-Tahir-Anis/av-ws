from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.object_detection.save_npc_data import NpcDataStorage
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning


class DistanceThreshold:

    def __init__(self):
        # self.threshold = 16.0
        # self.ego_location = EgoLocation(0, 0)
        # self.route = route
        # self.predecessor: str = ""

        pass

    def distance_calculator(self, npc_dist, ego_dist):
        distance_diff = npc_dist - ego_dist
        return distance_diff

    def update_tragectory(self, path):
        counter = 0
        predecessor = ""

        load_file = NpcDataStorage()
        npc_road, npc_lane, distance = load_file.load_object("data.pickle")
        print("---", npc_lane, npc_road)
        for road_id in path:
            if road_id[0] == str(npc_road):
                path[counter] = [road_id[0], "-1"]
                counter = counter - 1
                for road in path:
                    if road == path[counter]:
                        path[counter] = [road[0], "-1"]
            counter += 1
        print(path)
        return path

#
# if __name__ == '__main__':
#     d = DistanceThreshold()
#     d.update_tragectory()
