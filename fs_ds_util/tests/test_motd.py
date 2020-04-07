# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from .. import res
from fs_ds_util import motd as m




class TestMotd(unittest.TestCase):
    def _read_motd_file(self, file_name: str):
        with pkg_resources.open_text(res, file_name) as file:
            data_list = []
            line = file.readline()

            while line:
                data_list.append(line)
                line = file.readline().rstrip()
        file.close()

        return data_list

    def setUp(self):
        self.BOFH_EXCUSES = set(self._read_motd_file("bofh_excuses"))

    def test_print_bofh(self):
        excuse = m.get(catalog="bofh_excuses")
        self.assertTrue(excuse in self.BOFH_EXCUSES)


if __name__ == '__main__':
    unittest.main()

