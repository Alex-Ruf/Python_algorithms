def sieve_1(n):
    t = []
    for i in range(2, n + 1):
        c = 0
        for a in range(2, i - 1):
            if i % a == 0:
                c += 1
        if c >= 1:
            c = 0
        else:
            t.append(i)
    return t

def gen_1(num):
    n = 15*num
    while len(sieve_1(n)) < num:
        n += 10*num
    return sieve_1(n)[num - 1]


def sieve_2(num):
    sieve = [i for i in range(num)]
    a = []
    sieve[1] = 0
    for i in range(2, num):
        if sieve[i] != 0:
            j = i + i
            while j < num:
                sieve[j] = 0
                j += i

    for i in sieve:
        if i != 0:
            a.append(i)
    return a


def gen_2(num):
    n = 15*num
    while len(sieve_2(n)) < num:
        n += 10* num
    return sieve_2(n)[num - 1]


print(gen_2(10))
print(gen_1(10))

