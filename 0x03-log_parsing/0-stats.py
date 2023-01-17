#!/usr/bin/python3
"""
Module 0-stats
script that reads stdin line by line and computes metrics
"""
import sys
import re

# sample_line = '36.196.190.72 - [2022-04-26 07:59:21.687812] '\
#        '"GET /projects/260 HTTP/1.1" 500 878'

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

while True:
    try:
        line = input()
        match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            total_size += int(match.group(3))
            status_code = int(match.group(2))
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for status_code in sorted(status_codes):
                if status_codes[status_code] != 0:
                    print("{}: {}".format(status_code, status_codes[status_code]))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))