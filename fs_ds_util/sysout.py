"""
Collection of sysout debugging functions.

Sysout debugging functions helps to write strings stdout
"""
from inspect import getframeinfo, stack


def error(message: str, writer=print):
    """
    Write an error message

    :param message: Message to be displayed
    :param writer: Function to write the formatted message (default: print())
    :return: Nothing
    """
    caller = getframeinfo(stack()[1][0])
    writer("[X] {}:{} - {}".format(caller.filename, caller.lineno, message))


def info(message, writer=print):
    """
    Write an info message

    :param message: Message to be displayed
    :param writer: Function to write the formatted message (default: print())
    :return: Nothing
    """
    writer("[*] {}".format(message))


def warn(message: str, writer=print):
    """
    Write an warning message

    :param message: Message to be displayed
    :param writer: Function to write the formatted message (default: print())
    :return: Nothing
    """
    writer("[!] {}".format(message))


def section_begin(section: str, writer=print):
    """
    Write the beginning of a section (header line and header)

    :param section: Title of the section
    :param writer: Function to write the formatted message (default: print())
    :return: Nothing
    """
    writer("-" * 80)
    writer(section)


def section_end(writer=print):
    """
    Write the end of a section (footer line)

    :param writer: Function to write the formatted message (default: print())
    :return: Nothing
    """
    writer("-" * 80)
    writer()


def value_counts(header: str, val_counts, writer=print):
    """
    Write each entry of a given value_counts-Series (pandas) giving their
    Index / value, count and relative count.

    :param header: Header of value column
    :param val_counts: Pandas Series containing value counts
    :param writer: Function to write the formatted message (default: print())
    :return: Nothing
    """
    width_first_column = len(header)
    count_sum = val_counts.sum()

    writer("{} | Freq. | Rel. Freq.".format(header))
    writer("-" * width_first_column + "-|-------|-----------")
    format_string = "{:" + str(width_first_column) + "} |{:6} |{:6} %"
    for value, count in val_counts.iteritems():
        percent = round((count * 100 / count_sum), 3)
        writer(format_string.format(value, count, percent))
    writer("-" * width_first_column + "---------------------")

