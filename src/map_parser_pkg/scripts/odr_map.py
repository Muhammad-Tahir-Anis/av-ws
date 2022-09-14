from src.map_parser_pkg.scripts.odr_map_obj import odr_map


class OdrMap:
    def __init__(self):
        self.opendrive = odr_map()


def main():
    carla_map = OdrMap()
    print(carla_map.opendrive.road_list[0].junction)


if __name__ == '__main__':
    main()
