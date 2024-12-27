import datetime as dt

christmas_eve = dt.date(2024, 12, 24)
new_year = dt.date(2024, 12, 31)

delta = new_year - christmas_eve

print(delta) #7 days, 0:00:00
print(delta.days) #7

delta2 = christmas_eve - new_year
print(delta2) #-7 days, 0:00:00
print(delta2.days) #-7