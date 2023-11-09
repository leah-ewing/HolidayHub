""" Controller operations """

from datetime import date
import crud, random


def get_date_suffix(number):
    """ Gets the suffix for a given date ('st', 'nd', 'rd', or 'th') """

    num = int(number[-1])

    if num == 1:
        if int(number) == 11:
            suffix = 'th'
        else:
            suffix = 'st'
    elif num == 2:
        if int(number) == 12:
            suffix = 'th'
        else:
            suffix = 'nd'
    elif num == 3:
        if int(number) == 13:
            suffix = 'th'
        else:
            suffix = 'rd'
    else:
        suffix = 'th'

    return suffix


def is_leap_year(year):
    """ Checks if a given year is a leap year """

    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 or year % 100 == 0 and year % 400 % 100 == 0:
        return True


def get_next_day(month, day, year):
    """ Gets the next date to a given date """

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
    """ Gets the previous date to a given date """

    previous_date = dict()

    if day == 1:
        if month == 1:
            previous_date["month"] = 12
            previous_date["day"] = 31
            previous_date["year"] = year - 1
        else:
            if month - 1 == 2:
                leap_year = is_leap_year(year)
                if leap_year == True:
                    previous_date["month"] = month - 1
                    previous_date["day"] = 29
                    previous_date["year"] = year
                else:
                    previous_date["month"] = month - 1
                    previous_date["day"] = 28
                    previous_date["year"] = year
            elif month - 1 == 4 or month - 1 == 6 or month - 1 == 9 or month - 1 == 11:
                previous_date["month"] = month - 1
                previous_date["day"] = 30
                previous_date["year"] = year
            elif month - 1 == 1 or month - 1 == 3 or month - 1 == 5 or month - 1 == 7 or month - 1 == 8 or month - 1 == 10:
                previous_date["month"] = month - 1
                previous_date["day"] = 31
                previous_date["year"] = year
    else:
        previous_date["month"] = month
        previous_date["day"] = day - 1
        previous_date["year"] = year

    return previous_date


def get_current_date():
    """ Returns the current date """

    current_date = str(date.today()).split('-')
    month_string = crud.get_month_by_number(int(current_date[1]))
    
    today = {
        "month": month_string,
        "day": int(current_date[2]),
        "year": int(current_date[0])
    }

    return today


def check_for_valid_email(email):
    """ Checks if a given email is valid """

    if "@" in email.lower() and "." in email.lower():
        return True
    else:
        return False
    

def get_random_salutation():
    """ Returns a random salutation from a list of salutations """
    salutations = ["Hi there, ", 
                   "Howdy, ",
                   "Well hello, ",
                   "Good day, ",
                   "Hi, ",
                   "Hey, ",
                   "Hey there, ",
                   "Greetings, "]
    
    return random.choice(salutations)


def get_random_today_is_statement():
    """ Returns a random 'today is...' statement from a list of statements """
    statements = ["Today is ",
                  "It is ",
                  "Today happens to be ",
                  "Today's date is "]
    
    return random.choice(statements)


def get_random_it_is_also_statement():
    """ Returns a random 'it is also...' statement from a list of statements """
    statements = ["But it's also... ",
                  "But did you know it's also... ",
                  "But wait! It's also... ",
                  "But it ALSO happens to be... ",
                  "But did you know it ALSO happens to be... "]
    
    return random.choice(statements)