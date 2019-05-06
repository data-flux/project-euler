#!/usr/bin/env python3.6

from os import listdir
import re
import urllib.request
from html import unescape

LATEST_PROBLEM=668

print("# Project Euler\n")
print(f"|Problem|{'Title':60}|{'Status':15}|")
print(f"|------:|{'-'*60}|{'-'*15}|")

files = [f for f in sorted(listdir('.')) if "projecteuler" in f and "000" not in f]
for i in range(1,LATEST_PROBLEM+1):
    status = None
    fn = ""
    for f in [f for f in files if f"{i:03d}" in f]:
        fn = f
        with open(f,'r') as F:
            try:
                contents = "\n".join(F.readlines())
                status = re.search(r'STATUS:\s+(\S+)\n',contents)[1]
            except:
                status = "done"
    if status == None:
        status = "not-attempted"

    http = str(urllib.request.urlopen(f"https://projecteuler.net/problem={i}").read())
    title = unescape(re.search(r'<h2>(.+)</h2>',http)[1])
    if status == "not-attempted":
        print(f"|{i}|[{title}](https://projecteuler.net/problem={i})|{status}|")
    else:
        print(f"|{i}|[{title}](https://projecteuler.net/problem={i})|[{status}](./{fn})|")
