from stringifier import Stringifier
from parser import Parser

__all__ = ['parse', 'stringify', 'to_file']


def parse(jsonstr):
    """
    Parses a JSON string and returns a list or a dictionary
    """

    return Parser().parse(jsonstr)


def stringify(obj):
    """
    Returns a string with a valid JSON according to the
    object passed as argument. This object can be a list,
    tuple or dictionary.
    """

    return Stringifier().stringify(obj)


def to_file(file_name, obj):
    """
    Saves the object in a file in a JSON format

    @param file_name: The name of the file
    @param obj: The object to be stringified
    """

    with open(file_name, "w+") as f:
        f.write(stringify(obj))
