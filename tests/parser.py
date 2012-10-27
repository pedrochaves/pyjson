"""Tests for the lib's JSON parser"""

from nose.tools import assert_equals, assert_in

from pyjson import parse


class TestListParser(object):

    def test_empty_list(self):
        json = parse("[]")

        assert_equals(json, [])

    def test_integer_list(self):
        json = parse("[1, 20, 300]")

        assert_equals(json, [1, 20, 300])

    def test_float_list(self):
        json = parse("[1.5, 20.5, 300.78, 10e1, 20E2]")

        assert_equals(json, [1.5, 20.5, 300.78, 100.0, 2000.0])

    def test_negative_number_list(self):
        json = parse("[-1, -2.5, -1.0e1, -5]")

        assert_equals(json, [-1, -2.5, -10.0, -5])

    def test_mixed_number_list(self):
        json = parse("[1, 2.5, 3.5, 5]")

        assert_equals(json, [1, 2.5, 3.5, 5])

    def test_bool_values(self):
        json = parse("[false, true, null]")

        assert_equals(json, [False, True, None])
