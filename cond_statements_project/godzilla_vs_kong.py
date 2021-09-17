budget = float(input())
actors = int(input())
clothes_price = float(input())
decor = budget * 0.1
clothes_total = actors * clothes_price
if actors > 150:
    clothes_total *= 0.9
expenses = decor + clothes_total
if budget >= expenses:
    money_left = budget - expenses
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    money_short = expenses - budget
    print('Not enough money!')
    print(f'Wingard needs {money_short:.2f} leva more.')
