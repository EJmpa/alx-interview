#!/usr/bin/python3
"""Log Parsing"""

import sys

# Define a dictionary to keep track of status codes and their counts
status_codes = (
        {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
            }
        )
total_size = 0  # Initialize total file size
line_count = 0  # Initialize line count


def print_metrics():
    """
    Print the metrics including total file size and status code counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code])

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 7:
                file_size = int(parts[-1])
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1
            if line_count % 10 == 0:
                print_metrics()
        except Exception:
            pass
except KeyboardInterrupt:
    pass
finally:
    print_metrics()
