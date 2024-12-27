import datetime as dt

day = dt.date(2024, 12, 24)

print(day.strftime("%Y")) #2024
print(day.strftime("%m")) #12
print(day.strftime("%B")) #December
print(day.strftime("%d")) #24
print(day.strftime("%A")) #Tuesday
print(day.strftime("%H:%M:%S")) #00:00:00