from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.run_ego_vehicle.map_analysis import MapAnalysis
from logs import Log


class Trajectory:
    """
    Trajectory could have route points with specified speed
    route points could be got from path planning module
    """

    def __init__(self, route):
        self._t_axis: float = 0
        self._s_axis: float = 1
        self._curvature = 0
        self.route = route
        self.path_index = 0
        self.brake: bool = False
        self.throttle: float = 0
        self.steering: float = 0
        self.log = Log()
        self.road_ended = False

    def update_trajectory(self, x, y):
        self.log.x = x
        self.log.y = y
        road_id, lane_id = self.route[self.path_index]
        self.throttle, self.steering, self.brake = self.follow_trajectory(x, y, road_id, lane_id)
        return self.throttle, self.steering, self.brake

    def follow_trajectory(self, x, y, road_id, lane_id):
        map_analysis = MapAnalysis()

        ego_location = EgoLocation(x, y)

        actual_roads = ego_location.get_location
        is_road_present = False
        if len(actual_roads) == 1:
            if road_id == actual_roads[0][0]:
                self._s_axis, self._t_axis = ego_location.get_ego_location_st
                is_road_present = True
        for roads in actual_roads:
            if road_id == roads[0]:
                self._s_axis = roads[2]
                self._t_axis = roads[3]
                is_road_present = True
        if not is_road_present:
            self.road_ended = True

        x_origin, y_origin, heading, curvature = map_analysis.road_info(road_id, self._s_axis,
                                                                        self._t_axis, self.log)

        t_range = list(ego_location.get_t_range(road_id, float(lane_id)))
        self.steering = self.keep_in_lane(t_range, self._t_axis)
        if self.road_ended:
            self.path_index += 1
            self.brake = 1
            self.steering = 0
            self.throttle = 0
            self.road_ended = False
        elif curvature != 0 and not self.road_ended:
            self.throttle = 0.1
            self.brake = 0
            # self.steering = -curvature * 2.23
        else:
            self.throttle = 0.2
            self.brake = 0
            # self.steering = 0
        self.log.set_log()
        print(self.throttle, self.steering, self.brake)
        return self.throttle, self.steering, self.brake

    @classmethod
    def keep_in_lane(cls, t_range, t_axis):

        if t_axis > 0:
            t_range.reverse()
            print(t_range)
            print(t_range[0] - 1, t_range[1] + 2)
            if (t_range[0] - 1) < t_axis:
                return -1
            elif (t_range[1] + 2) > t_axis:
                return 1
            else:
                return 0

        else:
            print(t_range[0] - 1, t_range[1] + 2)
            if (t_range[0] - 1) < t_axis:
                return 1
            elif (t_range[1] + 2) > t_axis:
                return -1
            else:
                return 0
