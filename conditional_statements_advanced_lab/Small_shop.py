product = input()
city = input()
quantity = float(input())
if product == 'coffee':
    if city == 'Sofia':
        price = quantity * 0.50
        print(price)
    elif city == 'Plovdiv':
        price = quantity * 0.40
        print(price)
    elif city == 'Varna':
        price = quantity * 0.45
        print(price)
if product == 'water':
    if city == 'Sofia':
        price = quantity * 0.80
        print(price)
    elif city == 'Plovdiv':
        price = quantity * 0.70
        print(price)
    elif city == 'Varna':
        price = quantity * 0.70
        print(price)
if product == 'beer':
    if city == 'Sofia':
        price = quantity * 1.20
        print(price)
    elif city == 'Plovdiv':
        price = quantity * 1.15
        print(price)
    elif city == 'Varna':
        price = quantity * 1.10
        print(price)
if product == 'sweets':
    if city == 'Sofia':
        price = quantity * 1.45
        print(price)
    elif city == 'Plovdiv':
        price = quantity * 1.30
        print(price)
    elif city == 'Varna':
        price = quantity * 1.35
        print(price)
if product == 'peanuts':
    if city == 'Sofia':
        price = quantity * 1.60
        print(price)
    elif city == 'Plovdiv':
        price = quantity * 1.50
        print(price)
    elif city == 'Varna':
        price = quantity * 1.55
        print(price)