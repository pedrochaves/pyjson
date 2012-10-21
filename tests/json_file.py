"""Tests for the file manipulating bit of the lib"""

from nose.tools import assert_equals

import pyjson

class TestFileWriter(object):

    def test_save_file(self):
        my_data = range(0, 10)

        pyjson.to_file("test.json", my_data)

        with open("test.json") as json:
            assert_equals(json.read().strip(),
                "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
