from itertools import product
p=0
def makeTwoMinMax(num):
    _list = []
    for k in product(str(num), repeat=2):
        if k[0] == '0' or (k[0] == k[1] and str(num).count(k[0]) ==1):
            continue
        _list.append(int("".join(k)))

    return min(_list), max(_list)

for i in range(500, 601):
    _min, _max = makeTwoMinMax(i)

    if (_max - _min ==10):
        p +=i
print(p)
