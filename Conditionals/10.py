def LeapYear(yr):
    if yr % 4 == 0:
        if yr % 100 != 0:
            return True
        elif yr % 400 == 0:
            return False
    return False
