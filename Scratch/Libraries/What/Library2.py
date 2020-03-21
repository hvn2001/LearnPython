from datetime import date

# Now we only have the methods of the date class
date_today = date.today()  # Current date
print(date_today)

# These won't work
# time_today = datetime.datetime.now()
# print (time_today.strftime("%H:%M:%S"))# Current time
