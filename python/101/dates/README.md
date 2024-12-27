# Python -> 101 -> dates
notes on dates in Python

## Weekday
```python
from datetime import datetime
import calendar

dt = datetime.now()

print(dt.weekday()) #4
print(dt.isoweekday()) #5
print(dt.strftime('%A')) #Friday
print(calendar.day_name[dt.weekday()]) #Friday
```

## Basic operations
```python
from datetime import datetime

today = datetime.today()

print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")

print(f"Time: {today.hour}:{today.minute}:{today.second}")
```