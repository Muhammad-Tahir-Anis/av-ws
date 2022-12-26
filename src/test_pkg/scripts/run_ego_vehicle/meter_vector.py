import numpy as np

from src.test_pkg.scripts.run_ego_vehicle.pathpoint import PathWayPoints


class DrivingRope:
    def __init__(self, x, y):
        waypoints = PathWayPoints()
        self.get_meter_point(waypoints.get_waypoints, x, y)

    @classmethod
    def get_meter_point(cls, waypoints, x, y):
        x_points, y_points = waypoints
        print(x_points)
        print(y_points)
        future_x = cls.find_nearest(x_points, x)
        future_y = cls.find_nearest(y_points, y)

    @classmethod
    def find_nearest(cls, array, value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    # @classmethod
    # def get_curve(cls):
    #     curve = np.polyfit(x, y, 3)
    #     poly = np.poly1d(curve)
    #     new_x = []
    #     new_y = []
    #     for i in range(10):
    #         print(i)
    #         new_x.append((i + 1))
    #         new_y.append(poly(i + 1))


if __name__ == '__main__':
    dr = DrivingRope(12, 23)
