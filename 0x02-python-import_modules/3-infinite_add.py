#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_v = sys.argv[1:]
    arg_c = len(arg_v)
    int_array = list(map(int, arg_v))
    i = 1
    result = 0
    while i < arg_c:
        result = sum(int_array)
        i += 1
    print(result)
