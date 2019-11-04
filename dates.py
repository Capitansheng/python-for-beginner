# from datetime import datetime,timedelta
# today = datetime.now()
# print('today is: ' + str(today))
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print('yesterday was: ' + str(yesterday))
# from datetime import datetime
# current_date = datetime.now()
# print('day: ' + str(current_date.day))
# print('month: ' + str(current_date.month))
# print('year: ' + str(current_date.year))
from datetime import datetime
birthday = input('When is your birthday(dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday,'dd/mm/yyyy')
print('birthday: ' + str(birthday_date))