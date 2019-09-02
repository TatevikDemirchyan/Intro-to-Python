import argparse
import datetime
import calendar
import time
date1=datetime.datetime.today()
parser=argparse.ArgumentParser()
parser.add_argument("--num_d" , type=int)
parser.add_argument("--num_y" , type=int)
args = parser.parse_args()
print("Current date: ", date1)
if args.num_y:
    date2=date1+datetime.timedelta(days=args.num_y*365)
    print("Given years:", args.num_y)
else:
    date2=date1
    print("Given years: not given")

if args.num_d:
 date3=date2+datetime.timedelta(days=args.num_d)
 print("Given days:", args.num_d)
else:
    date3=date2
    print("Given days: not given")

print("Final date: ", date3)