from src.map_parser_pkg.scripts.odr_map_obj import opendrive
from src.test_pkg.scripts.Obstacle_avoidance.npc_distance_finder import NpcDistanceFinder
from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.object_detection.save_npc_data import NpcDataStorage
from src.test_pkg.scripts.run_ego_vehicle.path_planning import PathPlanning


class DistanceThreshold:

    def __init__(self):
        # self.threshold = 16.0
        # self.ego_location = EgoLocation(0, 0)
        # self.route = route
        # self.predecessor: str = ""
        self.egolocation = EgoLocation(0, 0)
        pass

    def distance_calculator(self, npc_dist, ego_dist):
        distance_diff = npc_dist - ego_dist
        return distance_diff

    def update_tragectory(self, path):
        # counter = 0
        # predecessor = ""

        load_file = NpcDataStorage()
        npc_road, npc_lane, distance = load_file.load_object("../object_detection/data.pickle")
        print("---", npc_lane, npc_road, distance)
        path = self.update_path(npc_road, npc_lane, path)
        # for road_id, lane_id in path:
        #     if road_id == str(npc_road):
        #         lane = self.get_new_lane(npc_road, npc_lane, path)
        #     path[counter] = [road_id, str(lane)]
        #     counter = counter - 1
        #     for road in path:
        #         if road == path[counter]:
        #             path[counter] = [road[0], "-1"]
        #     counter += 1
        print(path)
        return path

    def update_path(self, npc_road, npc_lane, path):
        counter = 0
        throttle = 0.2
        brake = 0
        for road_id, lane_id in path:
            if road_id == str(npc_road):
                driving_lanes = self.egolocation.get_all_driving_lanes(road_id)
                if len(driving_lanes) == 4:
                    # Left Lanes
                    if int(lane_id) > 0:
                        driving_lanes = [driving_lane for driving_lane in driving_lanes if int(driving_lane) > 0]
                    # Right Lanes
                    elif int(lane_id) < 0:
                        driving_lanes = [driving_lane for driving_lane in driving_lanes if int(driving_lane) < 0]
                    # if npc on path
                    if int(npc_lane) == int(lane_id):
                        # change lane if possible
                        print('ll',len(driving_lanes))
                        driving_lane = \
                            [driving_lane for driving_lane in driving_lanes if int(driving_lane) != int(npc_lane)][0]
                        path[counter] = [road_id, str(driving_lane)]
                        # change previous lane also.
                        lane = self.change_previous_lane(npc_lane, counter, path)
                        print('lane', lane)
                        if lane is None:
                            pass
                        elif lane != 0:
                            path[counter - 1][1] = str(lane)
                        else:
                            throttle = 0
                            brake = 1
                            print(throttle, brake)
                        print('dl', driving_lane)

                elif len(driving_lanes) == 2:
                    if int(npc_lane) == int(lane_id):
                        throttle = 0
                        brake = 1
                        print(throttle, brake)

                elif len(driving_lanes) == 1:
                    # No need to change previous lane.
                    print('1', driving_lanes)
                    throttle = 0
                    brake = 1
                    print(throttle, brake)
            counter += 1
        return path, throttle, brake

    def change_previous_lane(self, npc_lane, counter, path):
        road_id, lane_id = path[counter - 1]
        if int(npc_lane) > 0 and int(lane_id) > 0:
            lanes = self.egolocation.get_all_driving_lanes(str(road_id))
            lanes = [lane for lane in lanes if int(lane) > 0]
            if len(lanes) == 2:
                if int(npc_lane) == int(lane_id):
                    lane = [lane for lane in lanes if lane != str(lane_id)][0]
                    return lane
            elif len(lanes) == 1:
                if int(npc_lane) == int(lane_id):
                    return 0
        elif int(npc_lane) < 0 and int(lane_id) < 0:
            lanes = self.egolocation.get_all_driving_lanes(str(road_id))
            lanes = [lane for lane in lanes if int(lane) < 0]
            if len(lanes) == 2:
                if int(npc_lane) == int(lane_id):
                    lane = [lane for lane in lanes if lane != str(lane_id)][0]
                    return lane
            elif len(lanes) == 1:
                if int(npc_lane) == int(lane_id):
                    return 0
        elif int(npc_lane) > 0 and int(lane_id) < 0:
            lanes = self.egolocation.get_all_driving_lanes(str(road_id))
            lanes = [lane for lane in lanes if int(lane) < 0]
            if len(lanes) == 2:
                if int(npc_lane) == -int(lane_id):
                    lane = [lane for lane in lanes if lane != str(lane_id)][0]
                    return lane
            elif len(lanes) == 1:
                if int(npc_lane) == -int(lane_id):
                    return 0
        elif int(npc_lane) < 0 and int(lane_id) > 0:
            lanes = self.egolocation.get_all_driving_lanes(str(road_id))
            lanes = [lane for lane in lanes if int(lane) > 0]
            if len(lanes) == 2:
                if int(npc_lane) == -int(lane_id):
                    lane = [lane for lane in lanes if lane != str(lane_id)][0]
                    return lane
            elif len(lanes) == 1:
                print('ok')
                if int(npc_lane) == -int(lane_id):
                    return 0


# if __name__ == '__main__':
#     d = DistanceThreshold()
#     distance = NpcDistanceFinder()
#     print(distance.get_unique_st(0,0,7))
#     print(d.distance_calculator(12, 10))
#     path = PathPlanning()
#     route = path.route
#     d.update_tragectory(route)
    # path, throttle, brake = d.update_path(22, str(-1), route)
    # print(path, throttle, brake)
