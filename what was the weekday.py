# how to find a date's day of the week?
import datetime
userdate=input("Hello!enter a valid date.\n-->(dd/mm/yyyy)")
date=datetime.datetime.strptime(userdate,"%d/%m/%Y").date()
day_week=date.strftime("%A")
print(day_week)
