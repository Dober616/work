def create_dict(data):
    template = {}
    if isinstance(data, dict):
        return data
    elif isinstance(data, int) or isinstance(data, str) or isinstance(data, float):
        template[data] = data
        return template


my_string = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
new_list = []


def data_preparation(new_list):
    for element in my_string:
        if create_dict(element):
            new_list.append(create_dict(element))
    return new_list


print(data_preparation(new_list))
