#!/usr/bin/python3
"""This is the base class module"""


class Base:
    """The Base class"""
    __nb_objects = 0

    
    def __init__(self, id=None):
        """Instantiate id vairable"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            type(self).id = type(self).__nb_objects