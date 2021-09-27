year_type = input() # leap / npormal
holiday_days = int(input())
weekends_hometown = int(input()) # h
# plays only weekends and holidays
# plays in Sofia every saturday (if not at work, or in hometown)
# plays 2/3 of holiday days
# plays every sunday when in hometown
# goes to hometown 'h' times a year and plays on Sundays
# works 1/4 of all weekends in Sofia
# in a leap year he plays 15 % more volleyball
# year has 48 weekends
# How many days he played?
weekends_num = 48
weekends_sofia = weekends_num - weekends_hometown
weekends_sofia_play = 3/4 * weekends_sofia
weekends_play = weekends_sofia_play + weekends_hometown
holiday_days_play = holiday_days * 2/3
days_of_play = weekends_play + holiday_days_play
if year_type == 'leap':
    days_of_play *= 1.15
from math import floor
print(floor(days_of_play))

