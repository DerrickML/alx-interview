#!/usr/bin/python3
"""
Module 0-stats
script that reads stdin line by line and computes metrics
"""
import sys
import re

total_file_size = 0

# sample_line = '36.196.190.72 - [2022-04-26 07:59:21.687812] '\
#        '"GET /projects/260 HTTP/1.1" 500 878'

pattern = r'^([\d]{1,3}\.){3}([\d]{1,3})'
pattern += r'( - )(\[[\d]{4}-[\d]{2}-[\d]{2}'
pattern += r' [\d]{2}:[\d]{2}:[\d]{2}\.[\d]{1,}\])'
pattern += r'( "GET \/projects\/260 HTTP\/1\.1") '
pattern += r'([\d]{3}) ([\d]{1,4})$'


codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

no_of_lines = 0


def is_line_valid(line: str) -> bool:
    result = re.match(pattern, line)
    if result:
        return True
    return False


def generate_statistics(line: str) -> None:
    global total_file_size
    chars = line.split(' ')

    file_size = int(chars[-1].replace('\n', ''))
    try:
        status_code = int(chars[-2])
        if status_code in codes:
            codes[status_code] += 1
    except ValueError:
        pass

    total_file_size += file_size


def print_statistics() -> None:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

if __name__ == '__main__':
    try:
        for i, line in enumerate(sys.stdin, 1):
            # generate statistics only for a valid log
            if is_line_valid(line):
                generate_statistics(line)
            if not i % 10:
                print_statistics()
    except KeyboardInterrupt:
        print_statistics()
        raise
