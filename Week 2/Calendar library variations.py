import calendar

print(calendar.month(2021, 8))

'''

    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

'''

# print(calendar.calendar(2021)) will print entire 2021 calendar


from calendar import *

print(month(2021, 8))
'''

    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

'''

from calendar import month

print(month(2021, 8))
'''

    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

'''

# print(calendar(2021)) will give error

from calendar import month, calendar

# print(calendar(2021)) will not give error now

# Another thing we can do is

import calendar as c

print(c.month(2021, 10))  # instead of calendar.month(2021,10)

'''

    October 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

'''
