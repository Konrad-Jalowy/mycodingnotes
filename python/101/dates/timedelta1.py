import datetime as dt

today = dt.datetime.today()
timedelta = dt.timedelta(days=7)

week_later = today + timedelta
week_ago = today - timedelta

print(week_ago.strftime('%Y-%m-%d')) #2024-12-20
print(today.strftime('%Y-%m-%d')) #2024-12-27
print(week_later.strftime('%Y-%m-%d')) #2025-01-03
