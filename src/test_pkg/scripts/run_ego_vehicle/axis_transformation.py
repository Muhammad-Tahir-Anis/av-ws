from math import atan, sin, cos


class AxisTransformation:
    def __init__(self, x, y, x_origin, y_origin, heading, curvature, s_value):
        if curvature != 0:
            radius_of_curvature = 1 / curvature
            print("Radius: ", radius_of_curvature)
            # Translating Origin of axis to the starting point on road where s is initially 0
            self.x_prime, self.y_prime = self.__axis_translation(x, y, x_origin, y_origin)
            print("Translation Curv: ", self.x_prime, self.y_prime)
            # Rotating axis along the direction of the road.
            self.x_double_prime, self.y_double_prime = self.__axis_rotation(self.x_prime, self.y_prime, heading)
            print("Rotation Curv: ", self.x_double_prime, self.y_double_prime)
            # Translating axis to the center of curvature
            self.adjacent, self.opposite = self.__axis_translation(self.x_double_prime, self.y_double_prime,
                                                                   0, radius_of_curvature)
            # To calculate original angle values we use
            # tan(theta) = adjacent / opposite
            # theta = tan_inverse(adjacent / opposite)
            print("Adjacent & Opposite: ", self.adjacent, self.opposite)
            if self.opposite != 0:
                angle_in_degree = atan(abs(self.adjacent) / abs(self.opposite))
                print("Angle: ", angle_in_degree)
            else:
                angle_in_degree = 0
            # To calculate S and T we use S = r*angle
            # For this purpose we use radius of curvature of the road.
            self.s: float = abs(radius_of_curvature * angle_in_degree)+s_value
            # To get displacement of vehicle from origin which would be hypotenuse
            # self.t: float = radius_of_curvature - math.sqrt(self.opposite ^ 2 + self.adjacent ^ 2)
            self.t: float = 0
        else:
            x_translated, y_translated = self.__axis_translation(x, y, x_origin, y_origin)
            self.s, self.t = self.__axis_rotation(x_translated, y_translated, heading)
            self.s = self.s+s_value

    @classmethod
    def __axis_translation(cls, x, y, x_origin, y_origin):
        x_translation = (x - x_origin)
        y_translation = (y - y_origin)
        return x_translation, y_translation

    @classmethod
    def __axis_rotation(cls, x_translated, y_translated, heading):
        s = x_translated * cos(heading) + y_translated * sin(heading)
        t = y_translated * cos(heading) - x_translated * sin(heading)
        # print(s, t)
        return s, t

    @property
    def s_t_axis(self):
        return self.s, self.t