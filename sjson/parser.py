"""
The dynamic streaming JSON parser
"""
import abc


class Parser(object):
    """
    Abstract class capable of parsing some subset of the JSON spec
    """
    __metaclass__ = abc.ABCmeta
    pass