num = float(input())
metric_type_input = str(input()) # mm, cm, m
metric_type_output = str(input()) # mm, cm, m
if metric_type_input == 'mm':
    if metric_type_output == 'mm':
        print(f'{num:.3f}')
    elif metric_type_output == 'cm':
        num = num / 10
        print(f'{num:.3f}')
    elif metric_type_output == 'm':
        num = num / 1000
        print(f'{num:.3f}')
elif metric_type_input == 'cm':
    if metric_type_output == 'cm':
        print(f'{num:.3f}')
    elif metric_type_output == 'mm':
        num = num * 10
        print(f'{num:.3f}')
    elif metric_type_output == 'm':
        num = num / 100
        print(f'{num:.3f}')
elif metric_type_input == 'm':
    if metric_type_output == 'm':
        print(f'{num:.3f}')
    elif metric_type_output == 'mm':
        num = num * 1000
        print(f'{num:.3f}')
    elif metric_type_output == 'cm':
        num = num * 100
        print(f'{num:.3f}')

