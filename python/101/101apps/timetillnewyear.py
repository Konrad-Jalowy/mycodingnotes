import datetime as dt
from time import strftime
from time import gmtime

today = dt.datetime.today()

new_year = dt.datetime(today.year+1, 1, 1)

till_new_year = new_year - today

if till_new_year.days == 0:
    time_remaining = strftime("%H:%M:%S", gmtime(till_new_year.seconds))
    print(f"Its almost New Year {today.year+1}. Time remaining: {time_remaining}")
else:
    hours = strftime("%H", gmtime(till_new_year.seconds))
    if hours == "00":
        hours = "0"
    elif len(hours) == 2:
        if hours[0] == "0":
            hours = hours[1]

    minutes = strftime("%M", gmtime(till_new_year.seconds)).lstrip("0")

    if minutes == "00":
        minutes = "0"
    elif len(minutes) == 2:
        if minutes[0] == "0":
            minutes = minutes[1]

    seconds = strftime("%S", gmtime(till_new_year.seconds))

    if seconds == "00":
        seconds = "0"
    elif len(seconds) == 2:
        if seconds[0] == "0":
            seconds = seconds[1]

    time_remaining = f"{hours} hours, {minutes} minutes, {seconds} seconds"
    print(f"To Next Year {today.year+1} there is roughly {till_new_year.days+1} days.")
    print(f"Its basically {till_new_year.days} days, {time_remaining}")