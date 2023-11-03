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
    next_date = dict()

    if day in range(28, 32):
        if month == 2:
            leap_year = is_leap_year(year)
            
            if leap_year == True:
                if day == 29:
                    next_date["month"] = month + 1
                    next_date["day"] = 1
                    next_date["year"] = year
                else:
                    next_date["month"] = month
                    next_date["day"] = day + 1
                    next_date["year"] = year
            else:
                next_date["month"] = month + 1
                next_date["day"] = 1
                next_date["year"] = year
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day == 30:
                next_date["month"] = month + 1
                next_date["day"] = 1
                next_date["year"] = year
            else:
                next_date["month"] = month
                next_date["day"] = day + 1
                next_date["year"] = year
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day == 31:
                if month == 12:
                    next_date["month"] = 1
                    next_date["day"] = 1
                    next_date["year"] = year + 1
                else:
                    next_date["month"] = month + 1
                    next_date["day"] = 1
                    next_date["year"] = year
            else:
                next_date["month"] = month
                next_date["day"] = day + 1
                next_date["year"] = year
    else:
        next_date["month"] = month
        next_date["day"] = day + 1
        next_date["year"] = year

    return next_date


def get_previous_day(month, day, year):
    """ Gets the previous date from a given date """
    previous_date = dict()