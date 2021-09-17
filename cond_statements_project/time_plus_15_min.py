hour_input = int(input())
minutes_input = int(input())

hour_output = hour_input
minutes_output = minutes_input + 15
if minutes_output >= 60:
    hour_output = hour_input + 1
    minutes_output = minutes_output - 60
    if minutes_output < 10:
        if hour_output < 24:
            print(f'{hour_output}:0{minutes_output}')
        elif hour_output >= 24:
            hour_output = hour_output - 24
            print(f'{hour_output}:0{minutes_output}')

    else: # minutes_output >= 10
        if hour_output < 24:
            print(f'{hour_output}:{minutes_output}')
        elif hour_output >= 24:
            hour_output = hour_output - 24
            print(f'{hour_output}:{minutes_output}')
else: # minutes < 60
    if minutes_output < 10:
        print(f'{hour_output}:0{minutes_output}')
    else: # minutes >= 10
        print(f'{hour_output}:{minutes_output}')
