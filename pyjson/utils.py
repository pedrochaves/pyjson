def is_number(token):
    return type(token) in [int, float]


def is_json_array(token):
    return type(token) in [list, tuple]


def is_string(token):
    return type(token) in [str, unicode]


def is_dict(token):
    return type(token) == dict


def escape(string):
    to_escape = {
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
        "\b": "\\b",
    }

    for search, replace in to_escape.items():
        string = string.replace(search, replace)

    return string
