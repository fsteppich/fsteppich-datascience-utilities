# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

import pandas as pd

from fs_ds_util import sysout as so
import re


class StringWriter :
    def __init__(self):
        self.string = ""

    def write(self, string: str = ""):
        self.string += string + "\n"
        pass


class TestSysout(unittest.TestCase):
    def setUp(self):
        self.MESSAGE = "Hello World"

    def test_info(self):
        stringwriter = StringWriter()

        so.info(self.MESSAGE, writer=stringwriter.write)
        self.assertEqual(stringwriter.string, "[*] {}\n".format(self.MESSAGE), 'invalid INFO format')

    def test_warn(self):
        stringwriter = StringWriter()

        so.warn(self.MESSAGE, writer=stringwriter.write)
        self.assertEqual(stringwriter.string, "[!] {}\n".format(self.MESSAGE), 'invalid INFO format')

    def test_error(self):
        errorRegex = re.compile("\[X\] .+:\d{2} - Hello World\n")
        stringwriter = StringWriter()

        so.error(self.MESSAGE, writer=stringwriter.write)
        self.assertTrue(errorRegex.fullmatch(stringwriter.string) is not None, "invalid ERROR format")

    def test_section_begin(self):
        stringwriter = StringWriter()

        so.section_begin(self.MESSAGE, writer=stringwriter.write)
        self.assertEqual(stringwriter.string, "{}\n{}\n".format("-"*80, self.MESSAGE), 'invalid SECTION_BEGIN format')

    def test_section_end(self):
        stringwriter = StringWriter()

        so.section_end(writer=stringwriter.write)
        self.assertEqual(stringwriter.string, "{}\n\n".format("-"*80), 'invalid SECTION_END format')


    def test_value_counts(self):
        stringwriter = StringWriter()

        data = {'a' : 50, 'b' : 25, 'c' : 25}
        vcs = pd.Series(data)

        expectedString = """Foo | Freq. | Rel. Freq.
----|-------|-----------
a   |    50 |  50.0 %
b   |    25 |  25.0 %
c   |    25 |  25.0 %
------------------------
"""
        so.value_counts("Foo", vcs, writer=stringwriter.write)
        self.assertEqual(stringwriter.string, expectedString, 'invalid SECTION_END format')


if __name__ == '__main__':
    unittest.main()

