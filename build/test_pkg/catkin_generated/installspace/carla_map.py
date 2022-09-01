import json
from types import SimpleNamespace
def main():
    with open('json_map') as map_data:
        carla_map = json.load(map_data, object_hook=lambda d: SimpleNamespace(**d))


if __name__ == '__main__':
    main()
