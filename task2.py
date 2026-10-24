M_expression = input("Введіть вираз: ").strip()
if '+' in M_expression:
    sign = '+'
elif '-' in M_expression:
    sign = '-'
elif '*' in M_expression:
    sign = '*'
else:
    print("Помилка: невідомий або відсутній знак операції!")
    exit() 
A_str, B_str = M_expression.split(sign)
A = int(A_str)
B = int(B_str)
if sign == '+':
    print(A + B)
elif sign == '-':
    print(A - B)
elif sign == '*':
    print(A * B)

