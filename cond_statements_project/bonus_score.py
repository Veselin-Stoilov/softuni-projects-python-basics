num = int(input())
if num <= 100:
    num_bonus = num + 5
    if num % 2 == 0:
        num_bonus += 1
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
    elif num % 5 == 0:
        num_bonus += 2
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
    else:
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
elif num > 1000:
    num_bonus = num * 1.1
    if num % 2 == 0:
        num_bonus += 1
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
    elif num % 5 == 0:
        num_bonus += 2
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
    else:
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
else:
    num_bonus = num * 1.2
    if num % 2 == 0:
        num_bonus += 1
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
    elif num % 5 == 0:
        num_bonus += 2
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
    else:
        bonus = num_bonus - num
        print(bonus)
        print(num_bonus)
