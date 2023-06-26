#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as e:
        print("Exception:", e, file=sys.stderr)
        return None
