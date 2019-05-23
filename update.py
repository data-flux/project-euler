#!/usr/bin/env python3.6
from os import listdir
import re
import urllib.request
import urllib.parse
from html import unescape
import sys
import os
import time
import csv

try:
    with open('problems.csv','r') as problemfile:
        reader = csv.reader(problemfile,delimiter=',',quotechar='"')
        *_,last = reader
        http = urllib.request.urlopen(f"https://projecteuler.net/problem={int(last[0])+1}").read().decode('utf8')
        title = unescape(re.search(r'<h2>(.+)</h2>',http)[1])
        outdated = (title != "Problems Archives")
except Exception as e:
    print(e)
    outdated = True
if outdated:
    problems = {}
    print("Problem definitions outdated, updating...",end='')
    with open("problems.csv","w",newline='') as problemfile:
        writer = csv.writer(problemfile, delimiter=',', quotechar='"')
        for i in range(1,100000):
            if i%10==0:
                print('.',end='')
                sys.stdout.flush()
            http = urllib.request.urlopen(f"https://projecteuler.net/problem={i}").read().decode('utf8')
            title = unescape(re.search(r'<h2>(.+)</h2>',http)[1])
            if title == "Problems Archives":
                last = i-1
                break
            writer.writerow([i,title])
            problems[i]=title
    print()
else:
    with open('problems.csv','r') as problemfile:
        reader = csv.reader(problemfile,delimiter=',',quotechar='"')
        problems = {}
        for r in reader:
            problems[int(r[0])] = r[1]
        last = int(r[0])

with open('README.md','w') as file:
    file.write("# Project Euler\n\n")
    file.write(f"|Problem|{'Title':60}|{'Status':15}|\n")
    file.write(f"|------:|{'-'*60}|{'-'*15}|\n")
    
    files = [f for f in sorted(listdir('.')) if "projecteuler" in f and "000" not in f]
    for i in range(1,last+1):
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
        if status == "not-attempted":
            file.write(f"|{i}|[{problems[i]}](https://projecteuler.net/problem={i})|{status}|\n")
        else:
            file.write(f"|{i}|[{problems[i]}](https://projecteuler.net/problem={i})|[{status}](./{fn})|\n")
    
from subprocess import call
if len(sys.argv)>0:
    message = " ".join(sys.argv[1:])
    call(["/usr/bin/env", "git", "add", "--all", "."],stdout=sys.stderr)
    call(["/usr/bin/env", "git", "commit", "-a", "-m", f'{message}'],stdout=sys.stderr)
    call(["/usr/bin/env", "git", "push"],stdout=sys.stderr)
