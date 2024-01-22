f = open('26.txt')
a, b = f.readline().split()
d = []
s = 0
count = 0
for i in f:
    if 210 <= int(i) <= 220:
        s += int(i)
        count += 1
    else:
        d.append(int(i))
d.sort()
d2 = []
i = 0
while sum(d2) + d[i] <= int(b) - s:
    count += 1
    d2.append(d[i])
    i += 1
k = len(d) - 1
while i > 0:
    while k >= 0:
        if sum(d2) - d2[i-1] + d[k] <= int(b) - s and d[k] != 0:
            d2[i-1] = d[k]
            d[k] = 0
            i -= 1
            break
        else:
            k -= 1
print(s)
s += sum(d2)
print(count, s)