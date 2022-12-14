import math
from math import atan, sin, cos

import numpy as np


class AxisTransformation:
    def __init__(self, x, y, x_origin, y_origin, heading, curvature, s_value):
        self.x = x
        self.y = y
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.heading = heading
        self.curvature = curvature
        self.s_value = s_value

        if curvature != 0:
            self.s, self.t = self.handle_curvature(x, y, x_origin, y_origin, heading, curvature, s_value)
        else:
            x_translated, y_translated = self.__axis_translation(x, y, x_origin, y_origin)
            self.s, self.t = self.__axis_rotation(x_translated, y_translated, heading)
            self.s = self.s + s_value

    @classmethod
    def handle_curvature(cls, x, y, x_origin, y_origin, heading, curvature, s_value):
        x_curvature, y_curvature = cls.forward_transformation(x, y, x_origin, y_origin, heading, curvature)
        adjacent, opposite, angle_in_radian = cls.get_triangle_data(x_curvature, y_curvature, curvature)
        # radius always be positive
        radius_of_curvature = abs(1 / curvature)
        s: float = abs(radius_of_curvature * angle_in_radian) + s_value
        # To get displacement of vehicle from origin which would be hypotenuse
        hypotenuse = math.sqrt(abs(pow(opposite, 2)) + abs(pow(adjacent, 2)))
        if curvature > 0:
            t: float = radius_of_curvature - hypotenuse
        else:
            t: float = hypotenuse - radius_of_curvature
        return s, t

    @classmethod
    def __axis_translation(cls, x, y, x_origin, y_origin):
        x_translation = (x - x_origin)
        y_translation = (y - y_origin)
        return x_translation, y_translation

    @classmethod
    def __axis_rotation(cls, x, y, heading):
        s = x * cos(heading) + y * sin(heading)
        t = y * cos(heading) - x * sin(heading)
        if t == -0.0:
            t = 0
        if s == -0.0:
            s = 0
        return s, t

    @classmethod
    def normalize_angle(cls, adjacent, opposite, angle_in_radian, curvature):
        # opposite = Y ,  adjacent = X
        if curvature > 0:
            # First Quadrant
            if opposite >= 0 and adjacent >= 0:
                pass

            # Second Quadrant
            elif opposite >= 0 and adjacent < 0:
                # here in 2nd quadrant angle is in negative, so we will use + sign to subtract from 180
                angle_in_radian = math.radians(180) + angle_in_radian

            # Third Quadrant
            elif opposite < 0 and adjacent < 0:
                angle_in_radian = math.radians(180) + angle_in_radian

            # Fourth Quadrant
            elif opposite < 0 and adjacent > 0:
                # here in 4th quadrant angle is in negative, so we will use + sign to subtract from 360
                angle_in_radian = math.radians(360) + angle_in_radian
        else:
            # First Quadrant ## real quadrant = 2
            if opposite >= 0 and adjacent >= 0:
                # here in 2nd quadrant angle is in positive, so we will use - sign to subtract from 180
                angle_in_radian = math.radians(180) - angle_in_radian

            # Second Quadrant ## real quadrant = 1
            elif opposite >= 0 and adjacent < 0:
                # here it is first quadrant in my case but angle is in negative so we will make it positive
                angle_in_radian = abs(angle_in_radian)

            # Third Quadrant ## real quadrant = 4
            elif opposite < 0 and adjacent < 0:
                # here it is 4th quadrant in my case and angle is positive we use - sign to subtract from 360
                angle_in_radian = math.radians(360) - angle_in_radian

            # Fourth Quadrant ## real quadrant = 3
            elif opposite < 0 and adjacent > 0:
                # here it is 3rd quadrant in my case angle is in negative, so we will use - sign to add into 180
                angle_in_radian = math.radians(180) - angle_in_radian

        return angle_in_radian

    @classmethod
    def get_triangle_data(cls, x_curvature, y_curvature, curvature):
        # Again Rotating the axis as the starting of curvature becomes in First Quadrant
        x_prime_curvature, y_prime_curvature = cls.__axis_rotation(x_curvature, y_curvature,
                                                                   math.radians(-90))

        # Define the adjacent and opposite of triangle to find angle and hypotenuses.
        adjacent = x_prime_curvature
        opposite = y_prime_curvature

        # To calculate the angle values we use
        # tan(theta) = adjacent / opposite
        # theta = tan_inverse(adjacent / opposite)
        if opposite == 0:
            angle_in_radian = 0
        else:
            angle_in_radian = atan(opposite / adjacent)
            # Finding total angle
            angle_in_radian = cls.normalize_angle(adjacent, opposite, angle_in_radian, curvature)
        return adjacent, opposite, angle_in_radian

    @classmethod
    def forward_transformation(cls, x, y, x_origin, y_origin, heading, curvature):
        if curvature != 0:
            # radius always be positive
            radius_of_curvature = abs(1 / curvature)

            # Translating Origin of axis to the starting point on road where s is initially 0
            x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)

            # Rotating axis along the direction of the road.
            x_double_prime, y_double_prime = cls.__axis_rotation(x_prime, y_prime, heading)

            # Translating axis to the center of curvature
            curvature_x_origin = 0
            # When Curvature is positive
            if curvature > 0:
                curvature_y_origin = radius_of_curvature
            # When Curvature is negative
            else:
                curvature_y_origin = -radius_of_curvature

            x_curvature, y_curvature = cls.__axis_translation(x_double_prime, y_double_prime,
                                                              curvature_x_origin, curvature_y_origin)

            s, t = x_curvature, y_curvature
            return s, t
        else:
            x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)
            s, t = cls.__axis_rotation(x_prime, y_prime, heading)
            return s, t

    @classmethod
    def reverse_transformation(cls, s, t, x_origin, y_origin, heading, curvature):
        if curvature != 0:
            # radius of curvature
            radius = abs(1 / curvature)
            # angle in degree of s on curvature
            theta = np.rad2deg(s / radius)
            print(radius, curvature, theta)
            if curvature > 0:
                radius = radius - t
                adjacent, opposite = cls.get_angle_in_quadrant(curvature, theta, radius)
            else:
                radius = radius + t
                adjacent, opposite = cls.get_angle_in_quadrant(curvature, theta, radius)
            print(opposite, adjacent, radius)
            # x = opposite
            # y = adjacent
            # translate from origin of curvature / circle to starting point of geometry
            radius = abs(1 / curvature)
            if curvature > 0:
                x_prime, y_prime = cls.__axis_translation(opposite, adjacent, 0, -radius)
            else:
                x_prime, y_prime = cls.__axis_translation(opposite, adjacent, 0, radius)

            print(x_prime, y_prime)
            # rotating axis from road direction to main xy axis
            x_rotated, y_rotated = cls.__axis_rotation(x_prime, y_prime, -heading)
            print(x_rotated, y_rotated)
            # origin of curvature in xy global coordinates
            x, y = cls.__axis_translation(x_rotated, y_rotated, -x_origin, -y_origin)
            print(x,y)
            return x, y
        else:
            x_prime, y_prime = cls.__axis_rotation(s, t, -heading)
            x, y = cls.__axis_translation(x_prime, y_prime, -x_origin, -y_origin)
            return x, y

    @classmethod
    def get_angle_in_quadrant(cls, curvature, theta, radius):
        # Note: quadrants and signs of adjacent and opposites are decided on the basis of axis at origin of curvature
        ad, op = 0,0
        if curvature > 0:
            # 4th quadrant
            if theta <= 90:
                ad = -1
                op = 1
                pass
            # 1st quadrant
            elif 90 < theta <= 180:
                theta = 180 - theta
                ad = 1
                op = 1
            # 2nd quadrant
            elif 180 < theta <= 270:
                theta = theta - 180
                ad = 1
                op = -1
            # 3rd quadrant
            elif 270 < theta <= 360:
                theta = 360 - theta
                ad = -1
                op = -1
            theta = np.deg2rad(theta)
            adjacent = radius * np.cos(theta) * ad
            opposite = radius * np.sin(theta) * op
            return adjacent, opposite

        if curvature < 0:
            # 1st quadrant
            if theta <= 90:
                ad = 1
                op = 1
            # 4th quadrant
            elif 90 < theta <= 180:
                theta = 180 - theta
                ad = -1
                op = 1
            # 3rd quadrant
            elif 180 < theta <= 270:
                theta = theta - 180
                ad = -1
                op = -1
            # 2nd quadrant
            elif 270 < theta <= 360:
                theta = 360 - theta
                ad = 1
                op = -1
            theta = np.deg2rad(theta)
            adjacent = radius * np.cos(theta) * ad
            opposite = radius * np.sin(theta) * op
            return adjacent, opposite

    def get_boundaries(self, max_t, min_t, geometry_length, curvature):
        if curvature != 0:
            curvature_x_origin, curvature_y_origin = self.forward_transformation(self.x, self.y, self.x_origin,
                                                                                 self.y_origin, self.heading,
                                                                                 self.curvature)
            adjacent, opposite, point_angle_in_radian = self.get_triangle_data(curvature_x_origin, curvature_y_origin,
                                                                               self.curvature)

            radius_of_curvature = abs(1 / curvature)
            if curvature > 0:
                min_radius = radius_of_curvature - max_t
                max_radius = radius_of_curvature - min_t
            else:
                min_radius = radius_of_curvature + min_t
                max_radius = radius_of_curvature + max_t

            # Hypotenuse is also a radius of a circle which follows by our point (Vehicle)
            point_radius = math.sqrt(pow(opposite, 2) + pow(adjacent, 2))

            if min_radius < point_radius < max_radius:
                is_vehicle_in_circle = True
            else:
                is_vehicle_in_circle = False

            # while curvature is negative than origin of curvature is on right so inner lanes are negative and vise
            # versa else: if min_radius < point_radius < max_radius: is_vehicle_in_circle = True print(True) else:
            # is_vehicle_in_circle = False

            radius_of_curvature = abs(1 / curvature)
            min_angle = 0
            max_angle = geometry_length / radius_of_curvature
            if min_angle <= point_angle_in_radian <= max_angle:
                is_point_in_sector = True
            else:
                is_point_in_sector = False
            x, y = self.reverse_transformation(curvature_x_origin, curvature_y_origin, self.x_origin, self.y_origin,
                                               self.heading, self.curvature)

            if is_point_in_sector and is_vehicle_in_circle:
                is_point_on_road = True
            else:
                is_point_on_road = False
            return x, y, abs(min_radius), abs(max_radius), is_point_on_road

        else:
            s, t = self.forward_transformation(self.x, self.y, self.x_origin, self.y_origin, self.heading,
                                               self.curvature)
            # There are total 4 sides of rectangle
            # i.e A,B,C,D
            rect_side_a = s, t + max_t
            rect_side_b = s, t + min_t

            # length of rectangle is defied by value of s
            s = s + geometry_length
            rect_side_c = s, t + min_t
            rect_side_d = s, t + max_t

            rect_side_a = self.reverse_transformation(rect_side_a[0], rect_side_a[1], self.x_origin, self.y_origin,
                                                      self.heading, self.curvature)
            rect_side_b = self.reverse_transformation(rect_side_b[0], rect_side_b[1], self.x_origin, self.y_origin,
                                                      self.heading, self.curvature)
            rect_side_c = self.reverse_transformation(rect_side_c[0], rect_side_c[1], self.x_origin, self.y_origin,
                                                      self.heading, self.curvature)
            rect_side_d = self.reverse_transformation(rect_side_d[0], rect_side_d[1], self.x_origin, self.y_origin,
                                                      self.heading, self.curvature)

            return rect_side_a, rect_side_b, rect_side_c, rect_side_d

    @property
    def s_t_axis(self):
        return self.s, self.t
