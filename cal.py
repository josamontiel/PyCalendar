import calendar


print(calendar.weekheader(1))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2022, 5))

print(calendar.monthcalendar(2022, 5))

print(calendar.calendar(2022))

day_of_the_week = calendar.weekday(2022, 5, 26)
print(day_of_the_week) # 0 is Monday

is_leap = calendar.isleap(2022) # Check for leap year
print(is_leap)

how_many_leap_days = calendar.leapdays(2000, 2022)

print(how_many_leap_days)
