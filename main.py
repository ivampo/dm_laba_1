from itertools import product


def generate_functions(n):
    return product([0, 1], repeat=2 ** n) # через yield сделать

def count_t0(functions):
    count = 0
    for i in functions:
        if i[0] == 0:
            count += 1
    return count

def count_t1(functions):
    count = 0
    for i in functions:
        if i[-1] == 1:
            count += 1
    return count

def count_m(functions):
    count = 0
    for f in functions:
        flag = True
        for a, b in product(range(2 ** n), repeat=2):
            if (a & b) == a and f[a] > f[b]:
                flag = False
                break
        if flag:
            count += 1
    return count

def count_s(functions):
    count = 0
    for i in functions:
        l, r = i[:len(i) // 2], i[len(i) // 2:]
        flag = True
        for j in range(len(i) // 2):
            if l[j] == r[j]:
                flag = False
                break
        if flag: count += 1
    return count

def count_l(functions):
    # делаем полином жегалкина
    count = 0
    for i in functions:
        states = [i]
        while len(states[-1]) != 1:
            state = []
            for j in range(len(states[-1]) - 1):
                state.append(states[-1][j] ^ states[-1][j + 1])
            states.append(state)
        polinom = [i[0] for i in states]
        flag = True
        for ind, val in enumerate(polinom):
            if val == 1 and ind.bit_count() != 1:
                flag = False
                break
        if flag:
            count += 1
    return count

def calculate_post_classes(n):
    a = list(generate_functions(n))
    print('Количество функций сохраняющих 0:', count_t0(a))
    print('Количество функций сохраняющих 1:', count_t0(a))
    print('Количество линейных функций :', count_l(a))
    print('Количество монотонных:', count_m(a))
    print('Количество самодвойственных функций:', count_s(a))



calculate_post_classes(4)