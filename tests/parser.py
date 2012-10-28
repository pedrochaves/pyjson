"""Tests for the lib's JSON parser"""

from nose.tools import assert_equals, assert_in

import pyjson


class TestListParser(object):

    def test_empty_list(self):
        json = pyjson.parse("[]")

        assert_equals(json, [])

    def test_numbers_list(self):
        assert_equals(pyjson.parse("[1, 20, 300]"),
            [1, 20, 300])

        assert_equals(pyjson.parse("[1.5, 20.5, 300.78, 10e1, 20E2]"), 
            [1.5, 20.5, 300.78, 100.0, 2000.0])

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
