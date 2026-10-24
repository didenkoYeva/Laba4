line = input("Введіть рядок: ")
letter = input("Введіть букву: ").lower()
index_1 = line.find(letter)
index_e = line.rfind(letter)
result = ""
for i in range(len(line)):
    if line[i] == letter and index_1 < i < index_e:
        result += line[i].upper() 
    else:
        result += line[i] 
print(result)

