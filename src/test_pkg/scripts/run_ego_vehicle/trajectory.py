from fontTools.ttLib.tables.F__e_a_t import table_F__e_a_t

from src.test_pkg.scripts.run_ego_vehicle.ego_location import EgoLocation
from src.test_pkg.scripts.run_ego_vehicle.map_analysis import MapAnalysis

from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from logs import Log


class Trajectory:
    """
    Trajectory could have route points with specified speed
    route points could be got from path planning module
    """

    def __init__(self, route):
        self._t_axis: float = 0
        self._s_axis: float = 0
        self._curvature = 0
        self.route = route
        self.path_index = 0
        self.brake: bool = False
        self.throttle: float = 0
        self.steering: float = 0
        self.log = Log()

    def update_trajectory(self, x, y):
        # print("X: ", x, "Y: ", y)
        self.log.x = x
        self.log.y = y
        # print("S: ", self._s_axis, "T: ", self._t_axis)
        self.log.t = self._t_axis
        self.log.s = self._s_axis
        # print(self.path_index)
        road_id, lane_id = self.route[self.path_index]
        self.throttle, self.steering, self.brake = self.follow_trajectory(x, y, road_id, lane_id)
        # print(self.throttle, self.steering, self.brake)
        return self.throttle, self.steering, self.brake

    def follow_trajectory(self, x, y, road_id, lane_id):
        map_analysis = MapAnalysis()
        print("rid: ", road_id)
        x_origin, y_origin, heading, curvature, s_value, road_ended = map_analysis.road_info(road_id, self._s_axis,
                                                                                             self._t_axis, self.log)
        print("map anal: ", road_id, x_origin, y_origin, heading, curvature, road_ended)
        self.log.heading = heading
        axis_transformation = AxisTransformation(x, y, x_origin, y_origin, heading, curvature, s_value, self.log)
        self._s_axis, self._t_axis = axis_transformation.s_t_axis
        print("S,T: ", self._s_axis, self._t_axis)
        # print("Path Index: ", self.path_index)
        self.log.path_index = self.path_index
        ego_location = EgoLocation(x, y)
        print("el: ", ego_location.get_location)
        t_range = list(ego_location.get_t_range(road_id, float(lane_id)))
        print(ego_location.get_location)
        self.steering = self.keep_in_lane(t_range, self._t_axis)
        print(road_id, self._s_axis, self._t_axis)
        if road_ended:
            self._s_axis = 0
            self.path_index += 1
            self.brake = 1
            self.steering = 0
            self.throttle = 0
        elif curvature != 0 and not road_ended:
            self.throttle = 0.2
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
        print("k : ", t_range, t_axis)
        if t_axis > 0:
            t_range.reverse()
        print(t_range[0] - 1, t_range[1] + 2)
        if (t_range[0] - 1) < t_axis:
            return 1
        elif (t_range[1] + 2) > t_axis:
            return -1
        else:
            return 0

# traj = Trajectory(["3", "0", "10"])
# x = 109.6906770464934
# for y in range(5, 10):
#     print("xy: ",x,y)
#     traj.update_trajectory(x, y)
