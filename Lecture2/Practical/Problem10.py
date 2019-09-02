import datetime
import time
import calendar
print("Current year: ", datetime.datetime.now().year, "Current time: ", datetime.datetime.now().time())
print("Current year: ", datetime.date.today().year)
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
print("Current month: ", months[datetime.date.today().month-1])
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("Current weekday: ", weekdays[datetime.date.today().weekday()])
currentdate=datetime.datetime.today()
date1=currentdate-datetime.timedelta(days=5)
print("Current date -2 days: ", date1)

currenttime=datetime.datetime.now()
delta=datetime.timedelta(seconds=5)
timedelta=currenttime-delta
print("Current time -5 seconds: ", timedelta.time())