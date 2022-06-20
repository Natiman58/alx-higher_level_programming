#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as exe:
        print("Exception: {}".format(exe), file=sys.stderr)
        return False
