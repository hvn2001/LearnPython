import datetime as dt

date_today = dt.date.today()  # Current date
print(date_today)

time_today = dt.datetime.now()
print(time_today.strftime("%H:%M:%S"))  # Current time
