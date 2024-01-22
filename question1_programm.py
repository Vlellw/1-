f = open('26 (2).txt')	# считывание входных данных
maxsum = int(f.readline().replace('\n','').split(' ')[1])
l = f.readlines()
f.close()

ll = []
for i in l:
	ii = i.replace('\n','').split(' ')
	ii[0] = int(ii[0])
	ll.append(ii)

# создаём отдельные массивы для изделий a и b, и сортируем все 3 массива
alist = [k[0] for k in ll if k[1] == 'A']
blist = [k[0] for k in ll if k[1] == 'B']

alist.sort()
blist.sort()
ll.sort(key=lambda k: k[0])
# считаем максимальное количество изделий
msum = 0
maxc = 0

for i in ll:
	if msum + i[0] <= maxsum:
		msum += i[0]
		maxc += 1
	else:
		break
# "закупаем" максимальное количество изделий A
ba = []
for i in alist:
	if len(ba) >= maxc:
		break
	if sum(ba) + i <= maxsum:
		ba.append(i)
	else:
		break

# докупаем изделия B, при необходимости удаляя изделия A, пока не доберём до максимального значения
bb = []

for i in blist:
	if len(ba) + len(bb) >= maxc:
		break
	if sum(ba) + sum(bb) + i <= maxsum:
		bb.append(i)
	else:
		while sum(ba) + sum(bb) + i > maxsum:
			del ba[-1]
		bb.append(i)

# вывод ответа
print(len(ba))
print(maxsum - (sum(ba) + sum(bb)))