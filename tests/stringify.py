# -*- coding: utf-8 -*-
"""Tests for the stringify method of the lib"""

from nose.tools import assert_equals, assert_in

import pyjson


class TestStringify(object):

    def test_empty_list(self):
        json = []

        assert_equals(pyjson.stringify(json), "[]")

    def test_number_list(self):
        json = [1, 2, 3, 2.5, 10e1]

        assert_equals(pyjson.stringify(json),
            "[1, 2, 3, 2.5, 100.0]")

    def test_simple_string_list(self):
        json = ["str1", "2", "yeah"]

        assert_equals(pyjson.stringify(json),
            '["str1", "2", "yeah"]')

    def test_true_false_null(self):
        json = [True, False, None]

        assert_equals(pyjson.stringify(json),
            "[true, false, null]")

    def test_mixed_list(self):
        json = [None, "abc", 1]

        assert_equals(pyjson.stringify(json), '[null, "abc", 1]')

    def test_list_within_list(self):
        json = [[1, 2, 3], [4, 5, 6]]

        assert_equals(pyjson.stringify(json), '[[1, 2, 3], [4, 5, 6]]')

    def test_tuple_to_array(self):
        json = (1, 2, 3)

        assert_equals(pyjson.stringify(json), "[1, 2, 3]")

        json = (1, (1, 2), ())

        assert_equals(pyjson.stringify(json), "[1, [1, 2], []]")

    def test_simple_dict(self):
        json = pyjson.stringify({
            "string": "value",
            "number": 1,
            "float": 2.5,
            "nullkey": None,
            "boolt": True,
            "boolf": False
        })

        assert_equals(json[0], "{")
        assert_equals(json[-1], "}")
        assert_in('"string": "value"', json)
        assert_in('"boolf": false', json)
        assert_in('"number": 1', json)
        assert_in('"boolt": true', json)
        assert_in('"nullkey": null', json)
        assert_in('"float": 2.5', json)
        assert_equals(json.count(","), 5)

    def test_complex_json(self):
        my_data = {
            "my_array": [[0, 0], [1, 2]],
            "is_something": True,
            "this_is": None,
            "dict": {
                "name": "pedrochaves",
                "another_list": ["my_string"]
            }
        }

        json = pyjson.stringify(my_data)

        assert_in('"my_array": [[0, 0], [1, 2]]', json)
        assert_in('"is_something": true', json)
        assert_in('"this_is": null', json)
        assert_in('"dict": {', json)

    def test_special_chars(self):
        json = ["a\nb\t"]
        assert_equals(pyjson.stringify(json),
            '["a\\nb\\t"]')

        json = ['a"bc"']
        assert_equals(pyjson.stringify(json),
            '''["a\\"bc\\""]''')

        json = ['a\"bc\"']
        assert_equals(pyjson.stringify(json),
            '''["a\\\"bc\\\""]''')

        assert_equals(pyjson.stringify([u"àbcdêfghígklmñopqrstu"]),
            '["\\u00e0bcd\\u00eafgh\\u00edgklm\\u00f1opqrstu"]')
