day = input()
week_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend_list = ['Saturday', 'Sunday']
if day in week_days_list:
    print('Working day')
elif day in weekend_list:
    print('Weekend')
else:
    print('Error')