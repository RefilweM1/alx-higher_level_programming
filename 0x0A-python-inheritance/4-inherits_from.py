#!/usr/bin/python3
"""module inherits_form
finds if the object is an instance of a class that inherited
(directly/indirectly) from the speciefied class"""

def inherits_from(obj, a_class):
    """determines if obj is an instance of a class that inherited from a_class

    Args:
    -obj: object to look at
    -a_class: class to be evaluated

    Returns: True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
