vacation_money = float(input())
puzzles_num = int(input())
dolls_num = int(input())
teddy_bears_num= int(input())
minions_num = int(input())
toy_trucks_num = int(input())
puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
toy_truck_price = 2
gross_income = puzzles_num * puzzle_price + \
                dolls_num * doll_price + \
                teddy_bears_num * teddy_bear_price + \
                minions_num * minion_price + \
                toy_trucks_num * toy_truck_price
all_toys_sum = puzzles_num + dolls_num + teddy_bears_num + \
                minions_num + toy_trucks_num
if all_toys_sum >= 50:
    net_income = gross_income * 0.75 * 0.9
    money_needed = vacation_money - net_income
    if net_income >= vacation_money:
        money_left = net_income - vacation_money
        print(f'Yes! {money_left:.2f} lv left.')
    else:
        print(f'Not enough money! {money_needed:.2f} lv needed.')
else:
    net_income = gross_income * 0.9
    money_needed = vacation_money - net_income
    if net_income >= vacation_money:
        print(f'Yes! {net_income:.2f} lv left.')
    else:
        print(f'Not enough money! {money_needed:.2f} lv needed.')