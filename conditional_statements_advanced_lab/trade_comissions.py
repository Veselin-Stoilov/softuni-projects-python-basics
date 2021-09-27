city = input()
sales = float(input())
comission = 0
city_list = ['Sofia', 'Varna', 'Plovdiv']
if 0 <= sales <= 500:
    if city == 'Sofia':
        comission = sales * 0.05
    elif city == 'Varna':
        comission = sales * 0.045
    elif city == 'Plovdiv':
        comission = sales * 0.055
elif 500 < sales <= 1000:
    if city == 'Sofia':
        comission = sales * 0.07
    elif city == 'Varna':
        comission = sales * 0.075
    elif city == 'Plovdiv':
        comission = sales * 0.08
elif 1000 < sales <= 10000:
    if city == 'Sofia':
        comission = sales * 0.08
    elif city == 'Varna':
        comission = sales * 0.1
    elif city == 'Plovdiv':
        comission = sales * 0.12
elif sales > 10000:
    if city == 'Sofia':
        comission = sales * 0.12
    elif city == 'Varna':
        comission = sales * 0.13
    elif city == 'Plovdiv':
        comission = sales * 0.145
if sales < 0 or city not in city_list:
    print('error')
else:
    print(f'{comission:.2f}')