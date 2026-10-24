text = input("Введіть рядок: ")
total_chars = len(text)
upper_count = sum(1 for char in text if char.isupper())
lower_count = sum(1 for char in text if char.islower())
p_lower = (lower_count / total_chars) * 100
p_upper = (upper_count / total_chars) * 100
print(f"Відсоток малих і великих літер {p_lower:.2f} {p_upper:.2f}")
