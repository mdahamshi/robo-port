#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import datetime
import os
import sys
import speak
today = datetime.date.today()

daysInMonth = 30



def dayOfYear(month, day):
    return month * daysInMonth + day
    

def isBDay(date):
    return {
        dayOfYear(5, 25): "كُلُّ عام وأَنتِ بخير يا سَيِّدَة انوارَ"
        , dayOfYear(7, 15): "كُلُّ عام وأَنتَ بخير يا سَيِّدْ محمد"
        , dayOfYear(7, 17): "كُلُّ عام وأَنتَ بخير يا سَيِّدْ موسَى"
        , dayOfYear(8, 2): "كُلُّ عام وأَنتَ بخير يا سَيِّدْ خالد"
        , dayOfYear(11, 14): "كُلُّ عام وأَنتَ بخير يا سَيِّدْ أبو محمد"
        , dayOfYear(2, 24): "كُلُّ عام وأَنتَ بخير يا سَيِّدْ جمال"
        , dayOfYear(9, 21): "كُلُّ عام وأَنتِ بخير يا سَيِّدَة أُمُ محمد"
        , dayOfYear(8, 31): "كُلُّ عام وأَنتَ بخير يا سَيِّدْ قُصَيْ"
        , dayOfYear(8, 12): "كُلُّ عام وأَنتِ بخير يا سَيِّدَة سِراج"
    }.get(date, False)

day_of_year = dayOfYear(today.month, today.day)
result = isBDay(day_of_year)
if result:
    speak.speakHelper(result,'speak')
    os.execv("/usr/bin/play-bday", sys.argv)

