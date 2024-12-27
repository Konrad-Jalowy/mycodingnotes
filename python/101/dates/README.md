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

## date and time formats
similar to other languages
```python
from datetime import datetime

today = datetime.today()

print(today.strftime('%Y-%m-%d')) #2024-12-27
print(today.strftime('%H:%M:%S')) #11:31:03
```

## timedelta - adding/substracting days
```python
import datetime as dt

today = dt.datetime.today()
timedelta = dt.timedelta(days=7)

week_later = today + timedelta
week_ago = today - timedelta

print(week_ago.strftime('%Y-%m-%d')) #2024-12-20
print(today.strftime('%Y-%m-%d')) #2024-12-27
print(week_later.strftime('%Y-%m-%d')) #2025-01-03
```

## strftime formats
```python
import datetime as dt

day = dt.date(2024, 12, 24)

print(day.strftime("%Y")) #2024
print(day.strftime("%m")) #12
print(day.strftime("%B")) #December
print(day.strftime("%d")) #24
print(day.strftime("%A")) #Tuesday
print(day.strftime("%H:%M:%S")) #00:00:00
```