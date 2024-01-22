f = open('27886.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
kol = 0
for count in range(0, len(data)):
    if summa + data[count] > s:
        kol = count
        print(kol)
        break
    summa += data[count]
zapas = s - summa
itog = 0
for i in range(kol, len(data)):
    if (data[i] - data[kol - 1]) <= zapas:
        itog = data[i]
print(itog)