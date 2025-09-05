import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

print("TZ:", now.tzname())

#Date formatting
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

#Date manipulation
future_date = now + datetime.timedelta(days=10)
print("Date after 10 days:", future_date)