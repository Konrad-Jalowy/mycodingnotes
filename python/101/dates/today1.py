from datetime import datetime

today = datetime.today()

print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")

print(f"Time: {today.hour}:{today.minute}:{today.second}")