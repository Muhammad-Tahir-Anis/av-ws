import math
from math import atan, sin, cos
from logs import Log


class AxisTransformation:
    def __init__(self, x, y, x_origin, y_origin, heading, curvature, s_value, log:Log):
        if curvature != 0:
            radius_of_curvature = 1 / curvature
            # print("Radius: ", radius_of_curvature)
            log.radius_of_curvature = radius_of_curvature

            # Translating Origin of axis to the starting point on road where s is initially 0
            self.x_prime, self.y_prime = self.__axis_translation(x, y, x_origin, y_origin)
            # print("Translating to Curvature road: ", self.x_prime, self.y_prime)
            log.translated_axis = [self.x_prime,self.y_prime]

            # Rotating axis along the direction of the road.
            self.x_double_prime, self.y_double_prime = self.__axis_rotation(self.x_prime, self.y_prime, heading)
            # print("Rotating up to Curvature road heading / angle: ", self.x_double_prime, self.y_double_prime)
            log.rotated_axis = [self.x_double_prime, self.y_double_prime]

            # Translating axis to the center of curvature
            curvature_x_origin = 0
            # When Curvature is positive
            if curvature > 0:
                curvature_y_origin = radius_of_curvature
            # When Curvature is negative
            else:
                curvature_y_origin = -radius_of_curvature
            self.x_curvature, self.y_curvature = self.__axis_translation(self.x_double_prime, self.y_double_prime,
                                                                         curvature_x_origin, curvature_y_origin)

            # print("Translating to Curvature Origin: ", self.x_curvature, self.y_curvature)
            log.translated_axis_to_curvature_origin = [self.x_curvature,self.y_curvature]

            # Again Rotating the axis as the starting of curvature becomes in First Quadrant
            self.x_prime_curvature, self.y_prime_curvature = self.__axis_rotation(self.x_curvature, self.y_curvature,
                                                                                  math.radians(-90))
            # print("Rotating axis to normal: ", self.x_prime_curvature, self.y_prime_curvature)
            log.rotated_axis_toward_curvature = [self.x_prime_curvature, self.y_prime_curvature]

            # Define the adjacent and opposite of triangle to find angle and hypotenuses.
            self.adjacent = self.y_prime_curvature
            self.opposite = self.x_prime_curvature
            # print("Adjacent & Opposite: ", self.adjacent, self.opposite)
            log.adjacent = self.adjacent
            log.opposite = self.opposite

            # To calculate the angle values we use
            # tan(theta) = adjacent / opposite
            # theta = tan_inverse(adjacent / opposite)
            if self.opposite == 0:
                angle_in_radian = 0
            else:
                angle_in_radian = atan(self.adjacent / self.opposite)
                # print("Pre_angle: ", angle_in_radian)
                log.angle_before_normalization = angle_in_radian

                # Finding total angle
                angle_in_radian = self.normalize_angle(self.adjacent, self.opposite, angle_in_radian)

            # print("Angle: ", angle_in_radian)
            log.angle_in_radian = angle_in_radian

            # To calculate S and T we use S = r*angle
            # For this purpose we use radius of curvature of the road.
            # print("Radius of curva: ", radius_of_curvature, " s_value: ", s_value)
            log.radius_of_curvature = radius_of_curvature
            self.s: float = abs(radius_of_curvature * angle_in_radian) + s_value

            # To get displacement of vehicle from origin which would be hypotenuse
            self.hypotenuse = math.sqrt(pow(self.opposite, 2) + pow(self.adjacent, 2))
            self.t: float = radius_of_curvature - self.hypotenuse
            # self.t: float = 0
        else:
            x_translated, y_translated = self.__axis_translation(x, y, x_origin, y_origin)
            self.s, self.t = self.__axis_rotation(x_translated, y_translated, heading)
            self.s = self.s + s_value

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

    @property
    def s_t_axis(self):
        return self.s, self.t
