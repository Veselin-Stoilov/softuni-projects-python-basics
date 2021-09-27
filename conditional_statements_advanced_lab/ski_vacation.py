days = int(input())
room_type = input()
review = input()
nights = days - 1
final_price = 0
single_room_price = 18 # price per night
apartment_price = 25 # price per night
royal_suite_price = 35 # price per night
if 0 < days < 10:
    apartment_price *= 0.7 # 30% discount
    royal_suite_price *= 0.9 #10% dicount
elif days > 15:
    apartment_price *= 0.5
    royal_suite_price *= 0.8
else:
    apartment_price *= 0.65
    royal_suite_price *= 0.85
if room_type == 'room for one person':
    if review == 'positive':
        final_price = single_room_price * nights * 1.25
    elif review == 'negative':
        final_price = single_room_price * nights * 0.9
elif room_type == 'apartment':
    if review == 'positive':
        final_price = apartment_price * nights * 1.25
    elif review == 'negative':
        final_price = apartment_price * nights * 0.9
elif room_type == 'president apartment':
    if review == 'positive':
        final_price = royal_suite_price * nights * 1.25
    elif review == 'negative':
        final_price = royal_suite_price * nights * 0.9
print(f'{final_price:.2f}')
