budget = float(input())
season = input()
vac_place = ''
destination = ''
# summer -> camping
# winter -> hotel
# europe -> always hotel
if budget <= 100: # Bulgaria
    destination = 'Bulgaria'
    if season == 'summer':
        budget *= 0.3
    elif season == 'winter':
        budget *= 0.7
elif budget <= 1000: # Balkans
    destination = 'Balkans'
    if season == 'summer':
        budget *= 0.4
    elif season == 'winter':
        budget *= 0.8
elif budget > 1000: # Europe
    destination = 'Europe'
    budget *= 0.9
if season == 'summer' and budget < 1000:
    vac_place = 'Camp'
elif season == 'winter' or budget > 1000:
    vac_place = 'Hotel'
print(f'Somewhere in {destination}')
print(f'{vac_place} - {budget:.2f}') # Camp / Hotel - Money spent

