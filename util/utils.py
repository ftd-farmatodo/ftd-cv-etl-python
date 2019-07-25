# -*- coding: utf-8 -*-
def int_to_boolean(element):
    # noinspection PyBroadException
    try:
        value = int(float(element))
        if value == 0:
            return False
        if value == 1:
            return True
    except Exception:
        return False


def str_to_boolean(element):
    # noinspection PyBroadException
    try:
        if element == "true":
            return True
        elif element == "false":
            return False
    except Exception:
        return False


def to_string(element):
    # noinspection PyBroadException
    try:
        if not element or element == 'None' \
                or element is None or element == 'null' or element == 'NULL' or element == 'Null':
            return None
        return str(element)
    except Exception:
        return None


def to_int(element):
    # noinspection PyBroadException
    try:
        return int(float(element.strip()))
    except Exception:
        return 0
