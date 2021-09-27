ticket_type = input()
row = int(input())
column = int(input())
seats = row * column
income = 0
if ticket_type == 'Premiere':
    income = seats * 12
elif ticket_type == 'Normal':
    income = seats * 7.50
elif ticket_type == 'Discount':
    income = seats * 5
print(f'{income:.2f} leva')