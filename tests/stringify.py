"""Tests for the stringify method of the lib"""

from nose.tools import assert_equals, assert_in

from pyjson import stringify


class TestStringify(object):

    def test_just_an_empty_list(self):
        json = stringify([])

        assert_equals(json, "[]")

    def test_number_list(self):
        json = stringify([1, 2, 3, 2.5])

        assert_equals(json, "[1, 2, 3, 2.5]")

    def test_simple_string_list(self):
        json = stringify(["str1", "2", "yeah"])

        assert_equals(json, '["str1", "2", "yeah"]')

    def test_true_false_null(self):
        json = stringify([True, False, None])

        assert_equals(json, "[true, false, null]")

    def test_mixed_list(self):
        json = stringify([None, "abc", 1])

        assert_equals(json, '[null, "abc", 1]')

    def test_list_within_list(self):
        json = stringify([[1, 2, 3], [4, 5, 6]])

        assert_equals(json, '[[1, 2, 3], [4, 5, 6]]')

    def test_tuple_to_array(self):
        json = stringify((1, 2, 3))

        assert_equals(json, "[1, 2, 3]")

    def test_list_and_tuple(self):
        json = stringify((1, [1, 2], ()))

        assert_equals(json, "[1, [1, 2], []]")

    def test_simple_dict(self):
        json = stringify({
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

        json = stringify(my_data)

        assert_in('"my_array": [[0, 0], [1, 2]]', json)
        assert_in('"is_something": true', json)
        assert_in('"this_is": null', json)
        assert_in('"dict": {', json)

