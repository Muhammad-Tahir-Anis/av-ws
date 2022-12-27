import math

import numpy as np

from src.test_pkg.scripts.run_ego_vehicle.axis_transformation import AxisTransformation
from src.test_pkg.scripts.run_ego_vehicle.pathpoint import PathWayPoints

from scipy import spatial


class DrivingRope:
    def __init__(self):
        self.waypoints = PathWayPoints()

    def get_steering_angle(self, x, y, ego_heading):
        future_x, future_y = self.get_meter_point(self.waypoints.get_waypoints, x, y)
        angle = self.get_angle(x, y, future_x, future_y, ego_heading)
        print(angle, "angle")
        steering_angle = self.get_steering(angle)
        steering_angle = float(steering_angle)
        return steering_angle

    @classmethod
    def get_meter_point(cls, waypoints, x, y):
        x_points, y_points = waypoints
        # print(x_points)
        # print(y_points)
        pathpoints = []
        for xp, yp in zip(x_points, y_points):
            pathpoints.append((xp, yp))
        print(pathpoints)
        cordinates, index = cls.find_nearest_coordinates(x, y, pathpoints)
        index = int(index)
        print(cordinates, index)
        x, y = pathpoints[index]
        print(x, y)
        future_x, future_y = cls.find_next_1m(index, pathpoints)
        return future_x, future_y

    @classmethod
    def find_nearest(cls, array, value):
        array = np.asarray(array) - 5.30242673317159
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
        print(future_cord, 'fc')
        return future_cord

    @classmethod
    def get_angle(cls, x, y, future_x, future_y, ego_heading):

        print(future_x, future_y, 'fx,fy')
        angle = math.atan((future_y - y) / (future_x - x))
        print(angle)
        angle = angle - ego_heading

        # axis = AxisTransformation(future_x, future_y, x, y, ego_heading, 0, 0)
        # # axis = AxisTransformation(15, 15, 10, 10, 0, 0, 0)
        # perpendicular = abs(axis.s)
        # base = abs(axis.t)
        # print(axis.s, axis.t, 'st')
        # hypotenuses = abs(math.sqrt(math.pow(perpendicular, 2) + math.pow(base, 2)))
        # print(hypotenuses)
        # angle = math.asin(perpendicular/hypotenuses)
        # # print(angle)
        # # angle = 180-angle-90
        # print(angle)
        # print(np.rad2deg(angle))
        # angle = np.rad2deg(angle)
        # print(perpendicular, base, hypotenuses)
        return angle

    @classmethod
    def get_steering(cls, angle):
        # steering = np.linspace(0, 1, 70)
        steering = 1 / 70 * angle
        # steering = np.deg2rad(steering)
        print(steering)
        return steering


#
if __name__ == '__main__':
    dr = DrivingRope()
    print(dr.get_steering_angle(109.69749257264434, 5.415327227827523, 1.5639764844735438))
