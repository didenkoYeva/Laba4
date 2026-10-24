word = input("Введіть слово: ").strip()
n = len(word)
for i in range(n):
    suffix = word[i:]
    if suffix == suffix[::-1]:
        quantity = i
        break
print(quantity)

