num_1 = int(input())
num_2 = int(input())
operator = input()
result = 0
even_odd = ''
if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
elif operator == '/' and num_2 != 0:
    result = num_1 / num_2
elif operator == '%' and num_2 != 0:
    result = num_1 % num_2
if result % 2 == 0:
    even_odd = 'even'
else:
    even_odd = 'odd'
if operator in ('/', '%') and num_2 == 0:
    print(f'Cannot divide {num_1} by zero')

if operator in ('+', '-', '*'):
    print(f'{num_1} {operator} {num_2} = {result} - {even_odd}')
elif operator == '/' and num_2 != 0:
    print(f'{num_1} / {num_2} = {result:.2f}')
elif operator == '%' and num_2 != 0:
    print(f'{num_1} % {num_2} = {result}')

