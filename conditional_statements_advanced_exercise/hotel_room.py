month = input() # May, June, July, August, September, October;
nights = int(input())
studio_rate = 0
apartment_rate = 0
if month in ('May', 'October'):
    studio_rate = 50
    apartment_rate = 65
    if 7 < nights <= 14:
        studio_rate *= 0.95
    elif nights > 14:
        studio_rate *= 0.7
elif month in ('June', 'September'):
    studio_rate = 75.20
    apartment_rate = 68.70
    if nights > 14:
        studio_rate *= 0.8
elif month in ('July', 'August'):
    studio_rate = 76
    apartment_rate = 77
if nights > 14:
    apartment_rate *= 0.9
studio_entire_stay = nights * studio_rate
apartment_entire_stay = nights * apartment_rate

print(f'Apartment: {apartment_entire_stay:.2f} lv.')
print(f'Studio: {studio_entire_stay:.2f} lv.')