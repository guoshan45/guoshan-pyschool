def time24hr(tstr):
    time_list = tstr[:-2].split(':')
    time_int = [int(x) for x in time_list]
    am_pm = tstr[-2:]
    hours = time_int[0]
    minutes = time_int[1]
    if am_pm == 'am':
        if hours < 12:
            hours = hours + 12
            return "%02d%02dhr" % (hours, minutes)
        else:
            return "00%2dhr" % (minutes)
    else:
        if hours < 12:
            hours = hours + 12
            return "%02d%02dhr" % (hours, minutes)
        else:
            return "%02d%02dhr" % (hours, minutes)
