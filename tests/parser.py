"""Tests for the lib's JSON parser"""

from nose.tools import assert_equals

import pyjson


class TestListParser(object):

    def test_empty_list(self):
        json = pyjson.parse("[]")

        assert_equals(json, [])

    def test_numbers_list(self):
        assert_equals(pyjson.parse("[1, 20, 300]"),
            [1, 20, 300])

        assert_equals(pyjson.parse("[1.5, 20.5, 300.78, 10e1, 20.1E2]"),
            [1.5, 20.5, 300.78, 10e1, 20.1e2])

        assert_equals(pyjson.parse("[-1, -2.5, -1.0e1, -5]"),
            [-1, -2.5, -10.0, -5])

        assert_equals(pyjson.parse("[1, 2.5, 3.5, 5]"),
            [1, 2.5, 3.5, 5])

    def test_bool_values(self):
        json = pyjson.parse("[false, true, null]")

        assert_equals(json, [False, True, None])

    def test_strings(self):
        stringified = '["abc", "a"]'
        assert_equals(pyjson.parse(stringified),
            ["abc", "a"])

        stringified = '["a"bc"a"]'
        assert_equals(pyjson.parse(stringified),
            ['a"bc"a'])

        stringified = '["a\n\ta"]'
        assert_equals(pyjson.parse(stringified),
            ['a\n\ta'])

        stringified = '["a\u00eaa"]'
        assert_equals(pyjson.parse(stringified),
            ['a\u00eaa'])

        stringified = '''["Long text
Long text
Long text
Long text
Long text"]'''
        assert_equals(pyjson.parse(stringified),
            ["""Long text
Long text
Long text
Long text
Long text"""])

    def test_list_within_list(self):
        stringified = "[1, 2 ,3, [2, 3, 4]]"
        assert_equals(pyjson.parse(stringified),
            [1, 2, 3, [2, 3, 4]])

        stringified = "[[[], [], []], [[], [], []]]"
        assert_equals(pyjson.parse(stringified),
            [[[], [], []], [[], [], []]])


class TestDictParser(object):

    def test_empty_dict(self):
        assert_equals(pyjson.parse("{}"), {})

    def test_number_dict(self):
        assert_equals(pyjson.parse('{"mykey": 1}'), {"mykey": 1})

    def test_string_dict(self):
        assert_equals(pyjson.parse('{"mykey": "my string dict"}'),
            {"mykey": "my string dict"})

    def test_bool_dict(self):
        stringified = '''{
        "thisisfalse": false,
        "thisistrue": true,
        "thisisnull": null
        }'''

        expected = {
            "thisisfalse": False,
            "thisistrue": True,
            "thisisnull": None
        }

        assert_equals(pyjson.parse(stringified), expected)
