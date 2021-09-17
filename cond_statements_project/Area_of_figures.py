figure_type = input()
from math import pi
if figure_type == 'square':
    side = float(input())
    area = side **2
    print(f'{area:.3f}')
elif figure_type == 'circle':
    radius = float(input())
    area = pi * radius **2
    print(f'{area:.3f}')
elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_b * side_a
    print(f'{area:.3f}')
elif figure_type == 'triangle':
    base = float(input())
    height = float(input())
    area = base * height / 2
    print(f'{area:.3f}')