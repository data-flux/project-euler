#!/usr/bin/env python3.6
"""
PROBLEM: 019
AUTHOR:  Dirk Meijer
STATUS:  done
EXPLANATION:
    not difficult, just annoying
"""

from Euler.tictoc import *
leapyear = lambda x: (x%400==0) or ((x%100!=0) and (x%4==0))

def first_sundays_in_year(year,weekday):
    if leapyear(year):
        days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    s = int(weekday==0)
    for month,days in enumerate(days_in_month):
        weekday = (weekday+days)%7
        if month==11: #january of next year
            return (s,weekday)
        s += int(weekday==0)
        

if __name__=="__main__":
    tic()
    _, weekday = first_sundays_in_year(1900,1)
    S = 0
    for year in range(1901,2001):
        s, weekday = first_sundays_in_year(year,weekday)
        S += s

    print(S)

    toc()
    exit()
