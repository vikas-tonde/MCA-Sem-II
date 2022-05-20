import datetime
import calendar

print("Yesterday: ",datetime.datetime.now().date().__sub__(datetime.timedelta(1)))
print("Tomorrow: ",datetime.datetime.now().date().__add__(datetime.timedelta(1)))
print("Today: ",datetime.datetime.now().date())
print("Calendar", calendar.calendar(datetime.datetime.now().year))