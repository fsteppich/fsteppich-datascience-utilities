"""
Message of the Day (motd) to add a pinch of salt...

Motd help to cheer you up on a long day or even to get the started in the first place.
"""

from random import randint

# https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import res  # relative-import the *package* containing the templates


def _read_motd_file(file_name: str):
    with pkg_resources.open_text(res, file_name) as file:
        data_list = []
        line = file.readline()

        while line:
            data_list.append(line)
            line = file.readline().rstrip()
    file.close()

    return data_list


def get(catalog="bofh_excuses"):
    messages = _read_motd_file(catalog)
    line_index = randint(0, len(messages)-1)

    return messages[line_index]

