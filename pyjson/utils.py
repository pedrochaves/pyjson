def is_number(token):
    return type(token) in [int, float]


def is_json_array(token):
    return type(token) in [list, tuple]


def is_string(token):
    return type(token) in [str, unicode]


def is_dict(token):
    return type(token) == dict
