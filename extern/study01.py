# 日期
import datetime as dt

d1 = dt.date(2020,1,20)
print(d1)
print(d1.strftime("%m/%y/%d-%a"))
print(dt.date.today())

t1 =dt.time(15,23,36,20)
print(t1)

print(dt.datetime.now())