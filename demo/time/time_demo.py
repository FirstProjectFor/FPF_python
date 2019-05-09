import datetime
import time
import calendar
import pprint

f = '%Y-%m-%d %H:%M:%S'
# time
print('time -----------------------------------')
print(time.time())
print(time.ctime(0))

print('GM time: {}'.format(time.gmtime(time.time())))
print('Local time" {}'.format(time.localtime(time.time())))
print((time.gmtime(time.time())).tm_year)
print((time.gmtime(time.time())).tm_mon)
print((time.gmtime(time.time())).tm_mday)
print((time.gmtime(time.time())).tm_hour)
print((time.gmtime(time.time())).tm_min)
print((time.gmtime(time.time())).tm_sec)

# 格式化时间
print('{}'.format(time.strftime(f, time.gmtime())))

print()
print('date time:------------------')
# date time 由日期和时间组成
now = datetime.datetime.now()
print(now)
dt = datetime.datetime.fromtimestamp(time.time())
print('date time: {}'.format(dt))
print('date: {}'.format(dt.date()))
print('time: {}'.format(dt.time()))
print('datetime max: {}'.format(dt.max))
print('datetime min: {}'.format(dt.min))
print(dt.year)
print(dt.day)

print(datetime.date(2019, 2, 3))
print(datetime.time(1, 2, 3))

# 时间单位
one_day = datetime.timedelta(days=1)
print(one_day)
print(one_day.total_seconds())
print(dt - one_day)
#
print(dt.strftime(f))
print(datetime.datetime.strptime(dt.strftime(f), f))

print('{:%Y-%m-%d %H:%M:%S}'.format(now))

text_calendar = calendar.TextCalendar(calendar.MONDAY)
text_calendar.prmonth(2019, 5)
text_calendar.pryear(2019)
