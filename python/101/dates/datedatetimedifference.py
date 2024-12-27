import datetime as dt

today = dt.date.today()
new_year = dt.date(today.year+1, 1, 1)

till_new_year = new_year - today
print(till_new_year) #5 days, 0:00:00

today2 = dt.datetime.today()
new_year2 = dt.datetime(today2.year+1, 1, 1)

till_new_year2 = new_year2 - today2
print(till_new_year2) #4 days, 11:56:08.422919