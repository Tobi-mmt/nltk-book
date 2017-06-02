# -*- coding: utf-8 -*-
# 11, 13, 15, 17, 27, 34, 36, 39, 40, 43

##################
# 13 - We can use a dictionary to specify the values to be substituted into a formatting string.
# Read Python's library documentation for formatting strings http://docs.python.org/lib/typesseq-strings.html
# and use this method to display today's date in two different formats.
##################
from datetime import date

today = {
    'day': date.today().day,
    'month': date.today().month,
    'year': date.today().year
}

print('{day}.{month}.{year}'.format(**today))
print('{year}-{month}-{day}'.format(**today))
