#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        return None
