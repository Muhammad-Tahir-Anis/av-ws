from src.map_parser_pkg.scripts.odr_map_obj import opendrive


def spawn_at_road(road_number: int):
    roads = opendrive.road_list
    for road in roads:
        if f"Road {road_number}" == road.name:
            print(road.name)


def main():
    spawn_at_road(1)


if __name__ == '__main__':
    main()
