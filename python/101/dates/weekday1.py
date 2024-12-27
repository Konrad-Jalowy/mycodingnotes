from datetime import datetime
import calendar

dt = datetime.now()

print(dt.weekday()) #4
print(dt.isoweekday()) #5
print(dt.strftime('%A')) #Friday
print(calendar.day_name[dt.weekday()]) #Friday