import numpy as np

from src.test_pkg.scripts.run_ego_vehicle.pathpoint import PathWayPoints

from scipy import spatial


class DrivingRope:
    def __init__(self, x, y):
        waypoints = PathWayPoints()
        self.get_meter_point(waypoints.get_waypoints, x, y)

    @classmethod
    def get_meter_point(cls, waypoints, x, y):
        x_points, y_points = waypoints
        print(x_points)
        print(y_points)
        pathpoints = []
        for xp, yp in zip(x_points, y_points):
            pathpoints.append((xp, yp))
        cordinates, index = cls.find_nearest_coordinates(x, y, pathpoints)
        index = int(index)
        print(cordinates, index)
        print(pathpoints[1519])
        x, y = pathpoints[index]
        future_x, future_y = cls.find_next_1m(index, pathpoints)
        print(future_x, future_y)
        print(cls.get_angle(x, y, future_x, future_y))

    @classmethod
    def find_nearest(cls, array, value):
        array = np.asarray(array)-5.30242673317159
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    @classmethod
    def find_nearest_coordinates(cls, x, y, pathpoints):
        tree = spatial.KDTree(pathpoints)
        result = tree.query([(x, y)])
        return result

    @classmethod
    def find_next_1m(cls, index, pathpoints):
        future_cord = pathpoints[index + 10]
        return future_cord

    @classmethod
    def get_angle(cls, x, y, future_x, future_y):
        


if __name__ == '__main__':
    dr = DrivingRope(-5, 66)
