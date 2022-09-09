import json
import keyword
from town_map import TownMap

object_list = []
classes_list = []

town_map = TownMap("json_map.json")


def iterate_json(value: dict):
    """
    This iterator traverse json dictionary branch by branch.
    It will not go to another branch until current branch will be traversed completely
    :param value:
    :return:
    """
    keys_list = []
    if isinstance(value, dict):
        if value.keys():
            for key in value.keys():
                # At this point we got keys of json.
                keys_list.append(key)
                # extract_object(key, value[key])
                extract_object(var_name=key, class_name=key, value=value[key])
                iterate_json(value[key])
    elif isinstance(value, list):
        for index in value:
            iterate_json(index)
    else:
        pass
        # print(value)


def extract_object(class_name, value, var_name):
    parameters = []
    list_parameter = []
    if not isinstance(value, list):
        if not isinstance(value, (str, type(None))):
            for data in value:
                if isinstance(value[data], list):
                    # parameters.append(f"{data}_list = {data}s")
                    parameters.append([data, data + "s"])
                elif isinstance(value[data], (str, type(None))):
                    # parameters.append(f"{data} = {value[data]}")
                    parameters.append([data, data])
                else:
                    # parameters.append(f"{data} = {data}")
                    parameters.append([data, data])

            # object_temp = f"{var_name.lower()} = {class_name.capitalize()}({parameters})"
            object_list.insert(0, [var_name.lower(), class_name.capitalize(), parameters])
    if isinstance(value, list):
        for index in range(len(value)):
            # list_parameter.append(f"{class_name}{index}")
            list_parameter.append(class_name+str(index))
        # object_temp = f"{class_name}s = [{','.join(list_parameter)}]"
        object_list.insert(0,[class_name+"s",list_parameter])
        # object_list.insert(0, object_temp)
        index = 0
        for data in value:
            extract_object(var_name=f"{class_name}{index}", class_name=class_name, value=data)
            index += 1


def create_object():
    pass
def write_object(objects_list):
    with open("odr_map.py", "w") as python_file:
        map_object = "\n".join(objects_list)
        python_file.write(map_object)


def main():
    with open("json_map.json") as json_file:
        json_data = json.load(json_file)
        iterate_json(json_data)
        # write_object(object_list)
        for line in object_list:
            print(line)

        # for line in classes_list:
        #     print(line)


if __name__ == '__main__':
    main()
