budget = int(input())
season = input()
fishermen = int(input())
rental_cost = 0
if season == 'Spring':
    rental_cost = 3000
elif season == 'Summer':
    rental_cost = 4200
elif season == 'Autumn':
    rental_cost = 4200
elif season == 'Winter':
    rental_cost = 2600
if fishermen <= 6:
    rental_cost *= 0.9
elif fishermen <= 11:
    rental_cost *= 0.85
else:
    rental_cost *= 0.75
if fishermen % 2 == 0 and season != 'Autumn':
    rental_cost *= 0.95
money_balance = abs(budget - rental_cost)
if budget >= rental_cost:
    print(f"Yes! You have {money_balance:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_balance:.2f} leva.")