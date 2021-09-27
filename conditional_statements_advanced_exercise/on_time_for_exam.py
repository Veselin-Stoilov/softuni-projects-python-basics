exam_time_hour = int(input())
exam_time_minutes = int(input())
arrival_time_hour = int(input())
arrival_time_minutes = int(input())
exam_time_minutes_sum = exam_time_hour * 60 + exam_time_minutes
arrival_time_minutes_sum = arrival_time_hour * 60 + arrival_time_minutes
if arrival_time_minutes_sum > exam_time_minutes_sum:
    print('Late')
elif arrival_time_minutes_sum < exam_time_minutes_sum - 30:
    print('Early')
else:
    print('On time')
if arrival_time_minutes_sum != exam_time_minutes_sum:
    if exam_time_minutes_sum < arrival_time_minutes_sum: # he is late
        minutes_difference = abs(arrival_time_minutes_sum - exam_time_minutes_sum)
        if minutes_difference < 60:
            print(f'{minutes_difference:0>2d} minutes after the start')
        elif minutes_difference >= 60:
            hours_difference = minutes_difference // 60
            minutes_difference = minutes_difference % 60

            print(f'{hours_difference}:{minutes_difference:0>2d} hours after the start')
    elif exam_time_minutes_sum > arrival_time_minutes_sum: # he is early
        minutes_difference = abs(arrival_time_minutes_sum - exam_time_minutes_sum)
        if minutes_difference < 60:
            print(f'{minutes_difference} minutes before the start')
        elif minutes_difference >= 60:
            hours_difference = minutes_difference // 60
            minutes_difference = minutes_difference % 60
            print(f'{hours_difference}:{minutes_difference:0>2d} hours before the start')