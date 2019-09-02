import datetime
import time
import calendar
bday=datetime.date(1992, 11, 8)
print("\n","My birthday:", bday, "\n",
"Year:", bday.year, "\n",
"Month:", bday.month, "\n",
"Day:", bday.day, "\n",)
weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("I was born on", weekdays[bday.weekday()])
tday=datetime.date.today()
nextbday=datetime.date(2019,11,8)
print("Until my next birthday", nextbday-tday)


print("\n",calendar.month(2017,5))

yesterday=tday-datetime.timedelta(days=1)
today=datetime.datetime.now()
print("\n","Yesterday: ",yesterday,"\n","Today: ",today)

newdate=yesterday+datetime.timedelta(days=2)
print("\n","Yesterday+2",newdate)
new_date=yesterday+datetime.timedelta(days=-3)
print("\n","Yesterday-3",new_date)