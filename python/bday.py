#!/usr/bin/env python2
import datetime
import os
import sys
today = datetime.date.today()

daysInMonth = 30



def dayOfYear(month, day):
    return month * daysInMonth + day
    

def isBDay(date):
    return {
        dayOfYear(5, 25): True
        , dayOfYear(7, 15): True
        , dayOfYear(7, 17): True
        , dayOfYear(8, 2): True
        , dayOfYear(11, 14): True
        , dayOfYear(2, 24): True
        , dayOfYear(9, 21): True
        , dayOfYear(8, 31): True
        , dayOfYear(8, 12): True
    }.get(date, False)

day_of_year = dayOfYear(today.month, today.day)
if isBDay(day_of_year):
    os.execv("play-bday", sys.argv)

