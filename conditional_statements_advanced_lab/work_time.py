hour = int(input())
day = input()
if day == 'Sunday' or hour not in range(10,19):
    print('closed')
else:
    print('open')