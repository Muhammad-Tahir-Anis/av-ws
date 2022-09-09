from src.test_pkg.town_map.header import Header
from src.test_pkg.town_map.road import Road
from typing import List
from src.test_pkg.town_map.controller import Controller
from src.test_pkg.town_map.junction import Junction


class Opendrive:
    def __init__(self, header, road_list, controller_list, junction_list):
        self.header: Header = header
        self.road_list: List[Road] = list()
        self.controller_list: List[Controller] = list()
        self.junction_list: List[Junction] = list()
