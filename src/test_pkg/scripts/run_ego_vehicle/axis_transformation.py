import math
from math import atan, sin, cos
from logs import Log


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
            # print("translated: ", x_translated, y_translated, heading)
            self.s, self.t = self.__axis_rotation(x_translated, y_translated, heading)
            # print("rotated : ", self.s, self.t)
            self.s = self.s + s_value

    @classmethod
    def handle_curvature(cls, x, y, x_origin, y_origin, heading, curvature, s_value):
        # radius_of_curvature = 1 / curvature
        # # print("Radius: ", radius_of_curvature)
        # log.radius_of_curvature = radius_of_curvature
        #
        # # Translating Origin of axis to the starting point on road where s is initially 0
        # x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)
        # # print("Translating to Curvature road: ", self.x_prime, self.y_prime)
        # log.translated_axis = [x_prime, y_prime]
        #
        # # Rotating axis along the direction of the road.
        # x_double_prime, y_double_prime = cls.__axis_rotation(x_prime, y_prime, heading)
        # # print("Rotating up to Curvature road heading / angle: ", self.x_double_prime, self.y_double_prime)
        # log.rotated_axis = [x_double_prime, y_double_prime]
        #
        # # Translating axis to the center of curvature
        # curvature_x_origin = 0
        # # When Curvature is positive
        # if curvature > 0:
        #     curvature_y_origin = radius_of_curvature
        # # When Curvature is negative
        # else:
        #     curvature_y_origin = -radius_of_curvature
        # x_curvature, y_curvature = cls.__axis_translation(x_double_prime, y_double_prime,
        #                                                   curvature_x_origin, curvature_y_origin)
        # #
        # print("Translating to Curvature Origin: ", self.x_curvature, self.y_curvature)
        # log.translated_axis_to_curvature_origin = [x_curvature, y_curvature]
        x_curvature, y_curvature = cls.forward_transformation(x, y, x_origin, y_origin, heading, curvature)
        # # Again Rotating the axis as the starting of curvature becomes in First Quadrant
        # x_prime_curvature, y_prime_curvature = cls.__axis_rotation(x_curvature, y_curvature,
        #                                                            math.radians(-90))
        # # print("Rotating axis to normal: ", self.x_prime_curvature, self.y_prime_curvature)
        # # log.rotated_axis_toward_curvature = [x_prime_curvature, y_prime_curvature]
        #
        # # Define the adjacent and opposite of triangle to find angle and hypotenuses.
        # adjacent = y_prime_curvature
        # opposite = x_prime_curvature
        # # print("Adjacent & Opposite: ", self.adjacent, self.opposite)
        # log.adjacent = adjacent
        # log.opposite = opposite
        #
        # # To calculate the angle values we use
        # # tan(theta) = adjacent / opposite
        # # theta = tan_inverse(adjacent / opposite)
        # if opposite == 0:
        #     angle_in_radian = 0
        # else:
        #     angle_in_radian = atan(adjacent / opposite)
        #     # print("Pre_angle: ", angle_in_radian)
        #     log.angle_before_normalization = angle_in_radian
        #
        #     # Finding total angle
        #     angle_in_radian = cls.normalize_angle(adjacent, opposite, angle_in_radian)
        #
        # # print("Angle: ", angle_in_radian)
        # log.angle_in_radian = angle_in_radian
        #
        # # To calculate S and T we use S = r*angle
        # # For this purpose we use radius of curvature of the road.
        # # print("Radius of curva: ", radius_of_curvature, " s_value: ", s_value)
        # # log.radius_of_curvature = radius_of_curvature
        # print(x_curvature, y_curvature)
        adjacent, opposite, angle_in_radian = cls.get_triangle_data(x_curvature, y_curvature, curvature)
        # radius always be positive
        radius_of_curvature = abs(1 / curvature)
        s: float = abs(radius_of_curvature * angle_in_radian) + s_value
        # print("s_value: ", s_value)

        # To get displacement of vehicle from origin which would be hypotenuse
        hypotenuse = math.sqrt(abs(pow(opposite, 2)) + abs(pow(adjacent, 2)))
        # print("hypotenuse: ", hypotenuse, "radius_of_curvature : ", radius_of_curvature)
        if curvature > 0:
            t: float = radius_of_curvature - hypotenuse
        else:
            t: float = hypotenuse - radius_of_curvature
        # print("st: ", s, t)
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
        if t == -0.0:
            t = 0
        if s == -0.0:
            s = 0
        # print("st: ",s, t)
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
        # print("Rotating axis to normal: ", x_prime_curvature, y_prime_curvature)
        # log.rotated_axis_toward_curvature = [x_prime_curvature, y_prime_curvature]

        # Define the adjacent and opposite of triangle to find angle and hypotenuses.
        adjacent = x_prime_curvature
        # print(y_prime_curvature)
        # opposite = round(y_prime_curvature)
        opposite = y_prime_curvature
        # print("Adjacent & Opposite: ", adjacent, opposite)

        # To calculate the angle values we use
        # tan(theta) = adjacent / opposite
        # theta = tan_inverse(adjacent / opposite)
        if opposite == 0:
            angle_in_radian = 0
        else:
            angle_in_radian = atan(opposite / adjacent)
            # angle_in_radian = round(angle_in_radian, 3)
            # if angle_in_radian == -0.0:
            #     angle_in_radian = 0
            # print("Pre_angle: ", angle_in_radian)

            # Finding total angle
            angle_in_radian = cls.normalize_angle(adjacent, opposite, angle_in_radian, curvature)
            # print("after angle: ", angle_in_radian)
        return adjacent, opposite, angle_in_radian

    @classmethod
    def forward_transformation(cls, x, y, x_origin, y_origin, heading, curvature):
        # curvature = float(curvature)
        # print(x, y, x_origin, y_origin, heading, curvature)
        if curvature != 0:
            # radius always be positive
            radius_of_curvature = abs(1 / curvature)
            # print("Radius: ", radius_of_curvature)

            # Translating Origin of axis to the starting point on road where s is initially 0
            x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)
            # print("Translating to Curvature road: ", x_prime, y_prime)

            # Rotating axis along the direction of the road.
            x_double_prime, y_double_prime = cls.__axis_rotation(x_prime, y_prime, heading)
            # print("Rotating up to Curvature road heading / angle: ", x_double_prime, y_double_prime)

            # Translating axis to the center of curvature
            curvature_x_origin = 0
            # When Curvature is positive
            if curvature > 0:
                curvature_y_origin = radius_of_curvature
            # When Curvature is negative
            else:
                curvature_y_origin = -radius_of_curvature

            # print("oc: ", curvature_x_origin, curvature_y_origin)
            x_curvature, y_curvature = cls.__axis_translation(x_double_prime, y_double_prime,
                                                              curvature_x_origin, curvature_y_origin)
            # print("co : ", x_curvature, y_curvature)

            # adjacent, opposite, angle_in_radian = cls.get_triangle_data(x_curvature, y_curvature, heading)

            # To calculate the angle values we use
            # tan(theta) = adjacent / opposite
            # theta = tan_inverse(adjacent / opposite)
            # print(opposite)
            # if opposite == 0:
            #     angle_in_radian = 0
            # else:
            #     # angle_in_radian = atan(adjacent / opposite)
            #     angle_in_radian = atan(opposite / adjacent)
                # print("Pre_angle: ", angle_in_radian)

                # Finding total angle
                # angle_in_radian = cls.normalize_angle(adjacent, opposite, angle_in_radian)

            s, t = x_curvature, y_curvature
            return s, t
        else:
            x_prime, y_prime = cls.__axis_translation(x, y, x_origin, y_origin)
            # print("txty : ", x_prime, y_prime)
            s, t = cls.__axis_rotation(x_prime, y_prime, heading)
            return s, t

    # @classmethod
    # def get_triangle_sides(cls, x_curvature, y_curvature):
    #     # Again Rotating the axis as the starting of curvature becomes in First Quadrant
    #     x_prime_curvature, y_prime_curvature = cls.__axis_rotation(x_curvature, y_curvature,
    #                                                                math.radians(-90))
    #     # print("Rotating axis to normal: ", self.x_prime_curvature, self.y_prime_curvature)
    #
    #     # Define the adjacent and opposite of triangle to find angle and hypotenuses.
    #     adjacent = y_prime_curvature
    #     opposite = x_prime_curvature
    #     # print("Adjacent & Opposite: ", self.adjacent, self.opposite)
    #     return adjacent, opposite

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
            x_prime, y_prime = cls.__axis_rotation(s, t, -heading)
            x, y = cls.__axis_translation(x_prime, y_prime, -x_origin, -y_origin)
            return x, y

    def get_boundaries(self, max_t, min_t, geometry_length, curvature):
        if curvature != 0:
            curvature_x_origin, curvature_y_origin = self.forward_transformation(self.x, self.y, self.x_origin, self.y_origin, self.heading,
                                               self.curvature)
            s = self.s
            t = self.t
            # print("gl : ", geometry_length)
            # print("st : ", s, t)
            print("mtmt: ",max_t, min_t)
            print(1/curvature)

            # adjacent, opposite, point_angle_in_radian = self.get_triangle_data(s, t, self.heading)
            adjacent, opposite, point_angle_in_radian = self.get_triangle_data(curvature_x_origin, curvature_y_origin, self.curvature)

            radius_of_curvature = abs(1 / curvature)
            min_radius = radius_of_curvature - max_t
            max_radius = radius_of_curvature - min_t
            # Hypotenuse is also a radius of a circle which follows by our point (Vehicle)
            point_radius = math.sqrt(pow(opposite, 2) + pow(adjacent, 2))
            print("Min rad : ", min_radius, "Point_rad : ", point_radius, "Max rad : ", max_radius)

            # if self.curvature > 0:
            if min_radius < point_radius < max_radius:
                is_vehicle_in_circle = True
                print(True)
            else:
                is_vehicle_in_circle = False
            # while curvature is negative than origin of curvature is on right so inner lanes are negative and vise versa
            # else:
            #     if min_radius < point_radius < max_radius:
            #         is_vehicle_in_circle = True
            #         print(True)
            #     else:
            #         is_vehicle_in_circle = False

            # if curvature > 0:
            #     min_radius = t - min_t
            #     max_radius = t - max_t
            # else:
            #     min_radius = t + min_t
            #     max_radius = t + max_t


            # point_angle_in_radian = self.ang
            # print("ap: ",adjacent, opposite)
            # radius always be positive
            # print(curvature)
            radius_of_curvature = abs(1 / curvature)
            min_angle = 0
            max_angle = geometry_length / radius_of_curvature
            print("max, point, min : ", max_angle, point_angle_in_radian, min_angle)
            if min_angle <= point_angle_in_radian <= max_angle:
                is_point_in_sector = True
                print(True)
            else:
                is_point_in_sector = False
            x, y = self.reverse_transformation(curvature_x_origin, curvature_y_origin, self.x_origin, self.y_origin, self.heading, self.curvature)

            if is_point_in_sector and is_vehicle_in_circle:
                is_point_on_road = True
                # print(True)
            else:
                is_point_on_road = False
            return x, y, abs(min_radius), abs(max_radius), is_point_on_road

        else:
            s, t = self.forward_transformation(self.x, self.y, self.x_origin, self.y_origin, self.heading,
                                               self.curvature)
            # print("gl : ", geometry_length)
            # print("st : ", s, t)
            # print("mtmt: ", max_t, min_t)
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

# log = Log()
# axis = AxisTransformation(0, 0, float("1.0468000030517578e+2"), float("9.3699998855590820e+0"), float("1.5639764844735413e+0"), 0, 0, log)
# print(axis.s_t_axis)
# print(axis.forward_transformation(0, 0, float("1.0468000030517578e+2"), float("9.3699998855590820e+0"), float("1.5639764844735413e+0")))
# print(axis.reverse_transformation(0, 0, float("1.0468000030517578e+2"), float("9.3699998855590820e+0")))
