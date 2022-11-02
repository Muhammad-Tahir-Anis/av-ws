import math
from math import atan, sin, cos
from logs import Log


class AxisTransformation:
    def __init__(self, x, y, x_origin, y_origin, heading, curvature, s_value, log: Log):
        self.x = x
        self.y = y
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.heading = heading
        self.curvature = curvature
        self.s_value = s_value

        if curvature != 0:
            self.s, self.t = self.handle_curvature(x, y, x_origin, y_origin, heading, curvature, s_value, log)
        else:
            x_translated, y_translated = self.__axis_translation(x, y, x_origin, y_origin)
            self.s, self.t = self.__axis_rotation(x_translated, y_translated, heading)
            self.s = self.s + s_value

    @classmethod
    def handle_curvature(cls, x, y, x_origin, y_origin, heading, curvature, s_value, log: Log):
        radius_of_curvature = 1 / curvature
        # print("Radius: ", radius_of_curvature)
        log.radius_of_curvature = radius_of_curvature

        # Translating Origin of axis to the starting point on road where s is initially 0
        x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)
        # print("Translating to Curvature road: ", self.x_prime, self.y_prime)
        log.translated_axis = [x_prime, y_prime]

        # Rotating axis along the direction of the road.
        x_double_prime, y_double_prime = cls.__axis_rotation(x_prime, y_prime, heading)
        # print("Rotating up to Curvature road heading / angle: ", self.x_double_prime, self.y_double_prime)
        log.rotated_axis = [x_double_prime, y_double_prime]

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
        #
        # print("Translating to Curvature Origin: ", self.x_curvature, self.y_curvature)
        log.translated_axis_to_curvature_origin = [x_curvature, y_curvature]

        # Again Rotating the axis as the starting of curvature becomes in First Quadrant
        x_prime_curvature, y_prime_curvature = cls.__axis_rotation(x_curvature, y_curvature,
                                                                   math.radians(-90))
        # print("Rotating axis to normal: ", self.x_prime_curvature, self.y_prime_curvature)
        log.rotated_axis_toward_curvature = [x_prime_curvature, y_prime_curvature]

        # Define the adjacent and opposite of triangle to find angle and hypotenuses.
        adjacent = y_prime_curvature
        opposite = x_prime_curvature
        # print("Adjacent & Opposite: ", self.adjacent, self.opposite)
        log.adjacent = adjacent
        log.opposite = opposite

        # To calculate the angle values we use
        # tan(theta) = adjacent / opposite
        # theta = tan_inverse(adjacent / opposite)
        if opposite == 0:
            angle_in_radian = 0
        else:
            angle_in_radian = atan(adjacent / opposite)
            # print("Pre_angle: ", angle_in_radian)
            log.angle_before_normalization = angle_in_radian

            # Finding total angle
            angle_in_radian = cls.normalize_angle(adjacent, opposite, angle_in_radian)

        # print("Angle: ", angle_in_radian)
        log.angle_in_radian = angle_in_radian

        # To calculate S and T we use S = r*angle
        # For this purpose we use radius of curvature of the road.
        # print("Radius of curva: ", radius_of_curvature, " s_value: ", s_value)
        log.radius_of_curvature = radius_of_curvature
        s: float = abs(radius_of_curvature * angle_in_radian) + s_value

        # To get displacement of vehicle from origin which would be hypotenuse
        hypotenuse = math.sqrt(pow(opposite, 2) + pow(adjacent, 2))
        t: float = radius_of_curvature - hypotenuse
        # self.t: float = 0
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
        # print(s, t)
        return s, t

    @classmethod
    def normalize_angle(cls, adjacent, opposite, angle_in_radian):
        # First Quadrant
        if opposite > 0 and adjacent >= 0:
            pass

        # Second Quadrant
        elif opposite < 0 and adjacent >= 0:
            # here in 2nd quadrant angle is in negative, so we will use + sign to subtract from 180
            angle_in_radian = math.radians(180) + angle_in_radian

        # Third Quadrant
        elif opposite < 0 and adjacent < 0:
            angle_in_radian = math.radians(180) + angle_in_radian

        # Fourth Quadrant
        elif opposite > 0 and adjacent < 0:
            # here in 4th quadrant angle is in negative, so we will use + sign to subtract from 360
            angle_in_radian = math.radians(360) + angle_in_radian
        return angle_in_radian

    # def get_boundaries(cls, x, y, x_origin, y_origin, heading, curvature, geometry_length, max_t, min_t):

    @classmethod
    def forward_transformation(cls, x, y, x_origin, y_origin, heading, curvature):
        # curvature = float(curvature)
        if curvature != 0:
            radius_of_curvature = 1 / curvature
            # print("Radius: ", radius_of_curvature)

            # Translating Origin of axis to the starting point on road where s is initially 0
            x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)
            # print("Translating to Curvature road: ", self.x_prime, self.y_prime)

            # Rotating axis along the direction of the road.
            x_double_prime, y_double_prime = cls.__axis_rotation(x_prime, y_prime, heading)
            # print("Rotating up to Curvature road heading / angle: ", self.x_double_prime, self.y_double_prime)

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
            # translated from origin of curvature / circle to starting point of geometry
            x_prime, y_prime = cls.__axis_translation(0, 0, s, t)

            # rotating axis from road direction to main xy axis
            x_rotated, y_rotated = cls.__axis_rotation(x_prime, y_prime, -heading)
            # origin of curvature in xy global coordinates
            x, y = cls.__axis_translation(x_rotated, y_rotated, -x_origin, -y_origin)
            return x, y
        else:
            x_prime, y_prime = cls.__axis_rotation(s, t, heading)
            x, y = cls.__axis_translation(x_prime, y_prime, -x_origin, -y_origin)
            return x, y

    def get_boundaries(self, max_t, min_t, geometry_length, curvature):
        if curvature != 0:
            s, t = self.forward_transformation(self.x, self.y, self.x_origin, self.y_origin, self.heading,
                                               self.curvature)
            if curvature > 0:
                min_radius = t - min_t
                max_radius = t - max_t
            else:
                min_radius = t + min_t
                max_radius = t + max_t
            x, y = self.reverse_transformation(s,t, self.x_origin, self.y_origin, self.heading, self.curvature)
            return x, y, abs(min_radius), abs(max_radius)

        else:
            s, t = self.forward_transformation(self.x, self.y, self.x_origin, self.y_origin, self.heading, self.curvature)

            # There are total 4 sides of rectangle
            # i.e A,B,C,D
            rect_side_a = s, t + max_t
            rect_side_b = s, t + min_t

            # length of rectangle is defied by value of s
            s = s + geometry_length
            rect_side_c = s, t + min_t
            rect_side_d = s, t + max_t

            rect_side_a = self.reverse_transformation(rect_side_a[0], rect_side_a[1], self.x_origin, self.y_origin, self.heading, self.curvature)
            rect_side_b = self.reverse_transformation(rect_side_b[0], rect_side_b[1], self.x_origin, self.y_origin, self.heading, self.curvature)
            rect_side_c = self.reverse_transformation(rect_side_c[0], rect_side_c[1], self.x_origin, self.y_origin, self.heading, self.curvature)
            rect_side_d = self.reverse_transformation(rect_side_d[0], rect_side_d[1], self.x_origin, self.y_origin, self.heading, self.curvature)

            return rect_side_a, rect_side_b, rect_side_c, rect_side_d

    @property
    def s_t_axis(self):
        return self.s, self.t


# log = Log()
# axis = AxisTransformation(0, 0, float("1.0468000030517578e+2"), float("9.3699998855590820e+0"), float("1.5639764844735413e+0"), 0, 0, log)
# print(axis.s_t_axis)
# print(axis.forward_transformation(0, 0, float("1.0468000030517578e+2"), float("9.3699998855590820e+0"), float("1.5639764844735413e+0")))
# print(axis.reverse_transformation(0, 0, float("1.0468000030517578e+2"), float("9.3699998855590820e+0")))
