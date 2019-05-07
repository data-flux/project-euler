#!/usr/bin/env python3.6
from os import listdir
import re
import urllib.request
from html import unescape
import sys

with open('README.md','w') as file:

    file.write("# Project Euler\n\n")
    file.write("## 1-100\n\n")
    file.write(f"|Problem|{'Title':60}|{'Status':15}|\n")
    file.write(f"|------:|{'-'*60}|{'-'*15}|\n")
    
    files = [f for f in sorted(listdir('.')) if "projecteuler" in f and "000" not in f]
    for i in range(1,1000000):
        if i%10==0:
            print('.',end='')
            sys.stdout.flush()
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
        if title == "Problems Archives":
            break
        if status == "not-attempted":
            file.write(f"|{i}|[{title}](https://projecteuler.net/problem={i})|{status}|\n")
        else:
            file.write(f"|{i}|[{title}](https://projecteuler.net/problem={i})|[{status}](./{fn})|\n")
        if i%100==0:
            file.write(f"\n\n## {i+1}-{i+100}\n\n")
            file.write(f"|Problem|{'Title':60}|{'Status':15}|\n")
            file.write(f"|------:|{'-'*60}|{'-'*15}|\n")
    print()
    
from subprocess import call
if len(sys.argv)>0:
    message = " ".join(sys.argv[1:])
    call(["/usr/bin/env", "git", "add", "."],stdout=sys.stderr)
    call(["/usr/bin/env", "git", "commit", "-a", "-m", f'{message}'],stdout=sys.stderr)
    call(["/usr/bin/env", "git", "push"],stdout=sys.stderr)
