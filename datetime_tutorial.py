import datetime
import pytz
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
today_utc = datetime.datetime.now(tz=pytz.UTC)
birthday = datetime.date(1971, 11, 25)

days_alive = (today - birthday).days
days_till_birthday = (datetime.date(2020, 11, 25) - today).days
years_alive = relativedelta(today, birthday)

print()
print(f'Time now is {today_utc} Zulu')
print(f'Time now is {datetime.datetime.now()} Local')

print(f'Today\'s date is {today.strftime("%B %d ,%Y")}')
print(f'I was born on {birthday.strftime("%B %d, %Y")}')
print(f'You are {years_alive.years} years old')
print(f'You have been alive for {days_alive} days')
print(f'There is {days_till_birthday} days till your birthday')
