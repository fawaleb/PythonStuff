import calendar

print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.weekday(1971, 11, 25))
print(calendar.month(2020, 9, w=3))
print(calendar.monthcalendar(2020, 9))
print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 9, 24)
print(day_of_the_week)
print(calendar.isleap(2020))
print(calendar.leapdays(1971, 2021, ))
