'''
You are given the following information, but you may prefer to do some research for yourself.

 - 1 Jan 1900 was a Monday.
 - Thirty days has September,
   April, June and November.
   All the rest have thirty-one,
   Saving February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

 How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

from datetime import date as dt

def problem_0019(start_date, end_date):                                  # dates are inclusive

    curr_date = start_date
    sunday_count = 0

    while curr_date <= end_date:
        if curr_date.strftime("%A") == 'Sunday':
            sunday_count += 1

        next_year = curr_date.year if curr_date.month < 12 else curr_date.year + 1
        next_month = curr_date.month + 1 if curr_date.month < 12 else 1
        next_date = dt(next_year, next_month, 1)
        curr_date = next_date

    return sunday_count


print(problem_0019(dt(1901, 1, 1), dt(2000, 12, 31)))   
