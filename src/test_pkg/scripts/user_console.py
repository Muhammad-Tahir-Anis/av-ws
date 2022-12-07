from src.test_pkg.scripts.run_ego_vehicle.set_destination import Destination


def main():
    print("_______________AV________________")
    is_destination = False
    while not is_destination:
        print("_____=> Enter Destination <=_____")
        road_id = input("=> Enter Road ID: ")
        lane_id = input("=> Enter Lane ID: ")

        destination = Destination(road_id=road_id, lane_id=lane_id)
        is_destination = destination.is_destination
        if is_destination:
            print("______Valid Destination______")
        else:
            print("_____Invalid Destination_____")


if __name__ == '__main__':
    main()
