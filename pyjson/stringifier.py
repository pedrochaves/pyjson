from utils import *


def stringify(obj):
    return Stringifier().stringify(obj)


class Stringifier(object):

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

            self._append_token('"')
            self._append_token(key)
            self._append_token('"')
            self._append_token(': ')

            self._append_token_by_type(value)

            if i != items_size - 1:
                self._append_comma()

        self._append_token("}")

    def _append_token_by_type(self, value):
        if is_string(value):
            self._append_token('"')
            self._append_token(value)
            self._append_token('"')
        elif is_number(value):
            self._append_token(value.__str__())
        elif value is None:
            self._append_token("null")
        elif value == True:
            self._append_token("true")
        elif value == False:
            self._append_token("false")
        elif is_json_array(value):
            self._read_json_array(value)
        elif is_dict(value):
            self._read_dict(value)

    def _append_token(self, token):
        self._tokens.append(token)

    def _append_comma(self):
        self._append_token(",")
        self._append_token(" ")
