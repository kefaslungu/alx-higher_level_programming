#!/usr/bin/python3
"""A script that takes in a URL using sys.argv, Sends a request to the URL,
And displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers.get('X-Request-Id')

print(x_request_id)
