import turtle as t


def ex_2():
    def f_1(x, y, w, z):
        if ((x and not(y)) or (y == z) or not(w)) == 1:
            return 1
        else:
            return 0

    print('w x y z  f1')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    print(w, x, y, z, ' ', f_1(x, y, z, w))


def ex_5():
    w1 = []
    for n in range(100):
        s = bin(n)[2:]
        s = str(s)
        if n % 3 == 0:
            s += s[-3:]
        else:
            k = (n % 3) * 3
            s += bin(k)[2:]
        r = int(s, 2)
        if r > 151:
            w1.append(r)
    print(min(w1))


def ex_6():
    k = 25
    t.speed = 1000
    t.left(90)
    for i in range(7):
        t.forward(10 * k)
        t.right(120)
    t.up()
    t.speed = 1000
    for x in range(-1, k + 2):
        for y in range(-5, 15):
            t.goto(x * k, y * k)
            t.dot('red')


def ex_8():
    w1 = ['а', 'в', 'е', 'с', 'т']
    kol = 0
    count = 0
    for i in range(1, 8):
        for y in range(8):
            for z in range(8):
                for d in range(8):
                    for q in range(8):
                        s1 = str(i) + str(y) + str(z) + str(d) + str(q)
                        if '1' not in s1:
                            if (s1[0] != s1[1] and
                                s1[0] != s1[2] and
                                s1[0] != s1[3] and
                                s1[0] != s1[4] and
                                s1[1] != s1[2] and
                                s1[1] != s1[3] and
                                s1[1] != s1[4] and
                                s1[2] != s1[3] and
                                s1[2] != s1[4] and
                                s1[3] != s1[4]):
                                for v in range(4):
                                    if int(s1[v]) % 2 == 0 and int(s1[v + 1]) % 2 != 0:
                                        count += 1
                                    elif int(s1[v]) % 2 != 0 and int(s1[v + 1]) % 2 == 0:
                                        count += 1
                                    else:
                                        break
                                if count == 4:
                                    print(s1, count)

                                    kol += 1
                        count = 0
    print(kol) 

def ex_9():
    f = open('69914.txt')
    a = []
    count = 0
    for i in f:
        a = [int(j) for j in i.split()]
        s,p,k = 0,0,0
        for i in a:   
            if a.count(i) == 1:
                s += i
                k += 1
            if a.count(i) == 3: p = i
        if p != 0 and k == 3:
            if p >= (s/3):
                count += 1 
    print(count)


def ex_12():
    for i in range(1000, 3, -1):
        kol = 0
        s1 = '5' + ('2' * i)
        while '52' in s1 or '2222' in s1 or '1122' in s1:
            if '52' in s1:
                s1 = s1.replace('52', '11', 1)
            if '2222' in s1:
                s1 = s1.replace('2222', '5', 1)
            if '1122' in s1:
                s1 = s1.replace('1122', '25', 1)
        for x in s1:
            kol += int(x)
        if kol == 64:
            print(i, s1)
            break


def ex_14():
    for i in '0123456789ABCDEFGHI':
        r = int('98897' + i + '21', 19) + int('2' + i + '923', 19)
        if r % 18 == 0:
            print(r // 18)

    x = 3 * (3125 ** 8) + 2 * (625 ** 7) - 4 * (625 ** 6) + 3 * (125 ** 5) - 2 * (25 ** 4) - 2024
    s1 = ''
    while x != 0:
        s1 += str(x % 25)
        x //= 25
    s1 = s1[::-1]
    print(s1.count("0"))


def ex_15():
    for i in range(0, 300):
        kol = 0
        for x in range(0, 300):
            for y in range(0, 300):
                if (x + 2 * y < i) or (y < x) or (y > 60):
                    kol += 1
        if kol == 90000:
            print(i)
            break
def ex_16():

    def F(n):
        if n > 2024:
            return n
        return n * F(n + 1)

    print(F(2022) // F(2024))

def ex_17():
    f = open('17_2024.txt')
    s = f.readlines()
    for i in range(len(s)):
        s[i] = int(s[i])
    count = 0
    maxi = 0
    maxsum = 0
    for i in range(len(s)):
        if abs(s[i]) % 100 == 13:
            maxi = max(maxi, s[i])
    for i in range(2, len(s)):
        k1 = 0
        k2 = 0
        k3 = 0
        c1 = abs(s[i - 2])
        c2 = abs(s[i - 1])
        c3 = abs(s[i])
        while c1 > 0:
            k1 += 1
            c1 //= 10
        while c2 > 0:
            k2 += 1
            c2 //= 10
        while c3 > 0:
            k3 += 1
            c3 //= 10
        if (k1 == 3 and k2 == 3 and k3 != 3) or (k1 == 3 and k2 != 3 and k3 == 3) or (k1 != 3 and k2 == 3 and k3 == 3):
            if s[i - 2] + s[i - 1] + s[i] <= maxi:
                count += 1
                maxsum = max(maxsum, s[i - 2] + s[i - 1] + s[i])
    print(count, maxsum)


def ex_19(x, y, h):
    if h == 3 and x + y >= 45:
        return 1
    elif h == 3 and x + y < 45:
        return 0
    elif x + y >= 45 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return ex_19(x + 1, y, h + 1) or ex_19(x, y + 1, h + 1) or ex_19(x * 3, y, h + 1) or ex_19(x, y * 3, h + 1)
        else:
            return ex_19(x + 1, y, h + 1) or ex_19(x, y + 1, h + 1) or ex_19(x * 3, y, h + 1) or ex_19(x, y * 3, h + 1)

for x in range(1, 40):
    if ex_19(x, 4, 1) == 1:
        print("Задача 19: ", x)
        break


def ex_20(x, h):
    if h == 4 and x >= 50:
        return 1
    elif h == 4 and x < 50:
        return 0
    elif x >= 50 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return ex_20(x + 1, h + 1) or ex_20(x + 3, h + 1) or ex_20(x * 2, h + 1)   # стратегия победителя
        else:
            return ex_20(x + 1, h + 1) and ex_20(x + 3, h + 1) and ex_20(x * 2, h + 1)  # сратегия проигравшего

for x in range(1, 50):
    if ex_20(x, 1) == 1:
        print("Задача 20: ", x)



def ex_21a(x, y, h):
    if (h == 3 or h == 5) and x + y <= 20:
        return 1
    elif h == 5 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return ex_21b(x - 1, y, h + 1) or ex_21b(x, y - 1, h + 1) or ex_21b(x / 2, y, h + 1) or ex_21b(x, y / 2, h + 1)
        else:
            return ex_21b(x - 1, y, h + 1) and ex_21b(x, y - 1, h + 1) and ex_21b(x / 2, y, h + 1) and ex_21b(x, y / 2, h + 1)
def ex_21b(x, y, h):
    if h == 3 and x + y <= 20:
        return 1
    elif h == 3 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return ex_21b(x - 1, y, h + 1) or ex_21b(x, y - 1, h + 1) or ex_21b(x / 2, y, h + 1) or ex_21b(x, y / 2, h + 1)
        else:
            return ex_21b(x - 1, y, h + 1) and ex_21b(x, y - 1, h + 1) and ex_21b(x / 2, y, h + 1) and ex_21b(x, y / 2, h + 1)

for x in range(10, 100):
    if ex_21a(x, 10, 1) == 1:
        print("Задача 21: ", x)
print("====")
for x in range(10, 100):
    if ex_21b(x, 10, 1) == 1:
        print("Задача 21: ", x)
