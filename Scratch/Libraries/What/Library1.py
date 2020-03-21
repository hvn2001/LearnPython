import datetime

date_today = datetime.date.today()  # Current date
print(date_today)

time_today = datetime.datetime.now()
print(time_today.strftime("%H:%M:%S"))  # Current time