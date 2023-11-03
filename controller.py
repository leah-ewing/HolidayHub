""" Controller operations """


def get_date_suffix(num):
    """ Gets the suffix for a given date ('st', 'nd', 'rd', or 'th')"""
    num = int(num[-1])

    if num == 1:
        suffix = 'st'
    elif num == 2:
        suffix = 'nd'
    elif num == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    return suffix


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 or year % 100 == 0 and year % 400 % 100 == 0:
        return True
    else:
        return False


def get_next_day(month, day, year):
    """ Gets the next date from a given date """
    next_date = dict()

# 28/29 => february (check if leap year)
# 30 => september, april, june, november
# 31 => january, march, may, july, august, october, december

def get_previous_day(month, day, year):
    """ Gets the previous date from a given date """
    previous_date = dict()