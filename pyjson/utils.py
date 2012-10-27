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
        '\"': '\\"',
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
        "\b": "\\b",
        "\u": "\\u"
    }

    for search, replace in to_escape.items():
        string = string.replace(search, replace)

    return string

def to_unicode(string):
    token = ""
    for char in string:
        try:
            token += char.decode("utf-8")
        except UnicodeEncodeError:
            unicode_token = "%x" % ord(char)
            token += "\u%s" % (unicode_token.zfill(4))

    return token
