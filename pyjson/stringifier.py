from utils import *


def stringify(obj):
    """
    Returns a string with a valid JSON according to the
    object passed as argument. This object can be a list,
    tuple or dictionary.
    """

    return Stringifier().stringify(obj)


class Stringifier(object):
    """
    Class responsible for taking an object (list, tuple or dict) and
    stringify it to a valid JSON format
    """

    def __init__(self):
        self._tokens = []
        self._obj = None

    def stringify(self, obj):
        self._obj = obj

        if is_json_array(obj):
            self._read_json_array()
        elif is_dict(obj):
            self._read_dict()

        return "".join(self._tokens)

    def _read_json_array(self, obj=None):
        items = self._obj if obj is None else obj
        items_size = len(items)

        self._append_token("[")
        for i, value in enumerate(items):
            self._append_token_by_type(value)

            if i != items_size - 1:
                self._append_comma()

        self._append_token("]")

    def _read_dict(self, obj=None):
        obj = self._obj if obj is None else obj
        items = obj.items()
        items_size = len(items)

        self._append_token("{")
        for i, item in enumerate(items):
            key, value = item

            self._append_key(key)
            self._append_token_by_type(value)

            if i != items_size - 1:
                self._append_comma()

        self._append_token("}")

    def _append_token(self, token):
        self._tokens.append(token)

    def _append_key(self, key_name):
        self._append_token('"')
        self._append_token(key_name)
        self._append_token('": ')

    def _append_comma(self):
        self._append_token(", ")

    def _append_token_by_type(self, value):
        if is_string(value):
            self._append_string(value)
        elif is_number(value):
            self._append_number(value)
        elif value is None:
            self._append_null()
        elif value == True:
            self._append_true()
        elif value == False:
            self._append_false()
        elif is_json_array(value):
            self._read_json_array(value)
        elif is_dict(value):
            self._read_dict(value)

    def _append_string(self, string):
        self._append_token('"')
        self._append_token(string)
        self._append_token('"')

    def _append_number(self, number):
        self._append_token(str(number))

    def _append_null(self):
        self._append_token("null")

    def _append_true(self):
        self._append_token("true")

    def _append_false(self):
        self._append_token("false")    
