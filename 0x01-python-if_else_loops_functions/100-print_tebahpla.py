#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i >= 96 and i <= 122 and i % 2 == 1):
        i = i - 32
    print("{:c}".format(i), end='')
