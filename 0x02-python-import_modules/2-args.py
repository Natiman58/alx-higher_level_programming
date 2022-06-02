#!/usr/bin/python3
import sys
arg_v = sys.argv[1:]
arg_c = len(arg_v)
i = 1
if arg_c == 0:
    print(f"{arg_c} arguments.")
elif arg_c == 1:
    print(f"{arg_c} argument:")
    print(f"{arg_c}:", sys.argv[1])
else:
    while i <= arg_c:
        print(f"{i}: {sys.argv[i]}")
        i += 1
