flower_type = input()
flower_count = int(input())
budget = int(input())
rose_price = 5.00
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50
final_cost = 0
if flower_type == 'Roses':
    if flower_count > 80:
        final_cost = flower_count * rose_price * 0.9
    else:
        final_cost = flower_count * rose_price
elif flower_type == 'Dahlias':
    if flower_count > 90:
        final_cost = flower_count * dahlia_price * 0.85
    else:
        final_ = flower_count * dahlia_price
elif flower_type == 'Tulips':
    if flower_count > 80:
        final_cost = flower_count * tulip_price * 0.85
    else:
        final_ = flower_count * tulip_price
elif flower_type == 'Narcissus':
    if flower_count < 120:
        final_cost = flower_count * narcissus_price * 1.15
    else:
        final_ = flower_count * narcissus_price
elif flower_type == 'Gladiolus':
    if flower_count < 80:
        final_cost = flower_count * gladiolus_price * 1.20
    else:
        final_ = flower_count * gladiolus_price
money_balance = abs(budget - final_cost)
if final_cost <= budget:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_balance:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_balance:.2f} leva more.")