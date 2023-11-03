""" Controller operations """

def get_date_suffix(num):
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