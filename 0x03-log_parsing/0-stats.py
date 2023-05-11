#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import sys


def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
count_liness = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        par_line = line.split()
        par_line = par_line[::-1]

        if len(par_line) > 2:
            count_liness += 1

            if count_liness <= 10:
                file_size += int(par_line[0])
                code = par_line[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (count_liness == 10):
                print_msg(codes, file_size)
                count_liness = 0

finally:
    print_msg(codes, file_size)

