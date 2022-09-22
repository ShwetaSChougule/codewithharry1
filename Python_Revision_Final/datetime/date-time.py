# datetime Final
# In python there are no data types as date and time,
# but there is a module named datetime.
# Classes in datetime module are,date,time,datetime,timedelta

# 1 Date class:
# constructor syntax  - datetime.date(year,month,date)
#1
# from datetime import date
# my_date = date(1992,1,23)
# print(my_date)
# if value passed to date() are not int then TypeError is there,if values are out of range then
# ValueError occurs.

#2Get current date:
# from datetime import date
# t = date.today()
# p = t.strftime("%m/%d/%Y")    #to get date in string format
# p = t.strftime("%Y/%d/%m")    #to get date in string format
# print(p)
# print(type(p))
# print(t)

#Accessing individually
# y = t.year
# print(y)
# m = t.month
# print(m)
# d = t.day
# print(d)


# 3 To get date from timestamp:
# timestamp is number of seconds from 1 jan 1970
# from datetime import datetime
# d_t = datetime.fromtimestamp(123456)
# print(d_t)

# Time class:
# syntax - datetime.time(hour,minute,seconds)

#To get current time:
# from datetime import datetime
#
# today = datetime.now()
# print(today)
# print(today.strftime("%H:%M:%S"))
# print(today.strftime("%Y/%m/%d"))

# DATETIME class:
from datetime import datetime
t = datetime.now()
print(t)
print(t.year)
# syntax  - datetime.datetime(year,month,day,hour,minute,second)


# TIMEDELTA CLASS
#1 Difference between 2 date and time:
# strptime



