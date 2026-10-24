sign = input("Введіть символ для малювання літери M: ")
if len(sign) != 1:
    sign = '*'
m = 7
for i in range(m):
    for j in range(m):
        if j == 0 or j == m - 1 or (i == j and i <= m // 2) or (i + j == m - 1 and i <= m // 2):
            print(sign, end="")
        else:
            print(" ", end="") 
    print() 
