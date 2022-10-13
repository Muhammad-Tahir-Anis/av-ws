import pandas as pd


class Log:
    def __init__(self):
        self.x: float = 0
        self.y: float = 0
        self.path_index: int = 0
        self.road_id: int = 0
        self.s_axis: float = 0
        self.heading: float = 0
        self.radius_of_curvature: float = 0
        self.is_curvature: bool = False
        self.translated_axis: list = []
        self.rotated_axis: list = []
        self.translated_axis_to_curvature_origin: list = []
        self.rotated_axis_toward_curvature: list = []
        self.adjacent: float = 0
        self.opposite: float = 0
        self.angle_before_normalization: float = 0
        self.angle_in_radian: float = 0
        self.hypotenuse: float = 0
        self.s: float = 0
        self.t: float = 0

        # self.data, self.column_names = self.set_log(self.x, self.y, self.path_index, self.road_id, self.s_axis,
        #                                             self.heading, self.radius_of_curvature, self.is_curvature
        #                                             , self.translated_axis, self.rotated_axis,
        #                                             self.translated_axis_to_curvature_origin
        #                                             , self.rotated_axis_toward_curvature, self.adjacent, self.opposite
        #                                             , self.angle_before_normalization, self.angle_in_radian,
        #                                             self.hypotenuse, self.s, self.t)

    def set_log(self):
        data = [[self.x], [self.y], [self.path_index], [self.road_id], [self.s_axis], [self.heading], [self.radius_of_curvature], [self.is_curvature], [self.translated_axis],
                [self.rotated_axis], [self.translated_axis_to_curvature_origin], [self.rotated_axis_toward_curvature], [self.adjacent], [self.opposite],
                [self.angle_before_normalization], [self.angle_in_radian], [self.hypotenuse], [self.s], [self.t]]

        column_names = ["x", "y", "path_index", "road_id", "s_axis", "heading", "radius_of_curvature", "is_curvature",
                        "translated_axis", "rotated_axis", "translated_axis_to_curvature_origin",
                        "rotated_axis_toward_curvature", "adjacent", "opposite", "angle_before_normalization",
                        "angle_in_radian", "hypotenuse", "s", "t"]

        df = pd.DataFrame(data)
        df.columns = column_names
        print(df)
        # return data, column_names

    # def print_log(self):
    #     pass
