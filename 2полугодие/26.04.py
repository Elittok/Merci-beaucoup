#22222222222222222222222222222222222222222222222222222222222
def is_unique(num):
    n=len(str(num))
    sum_digits=sum([int(digit)**n for digit in str(num)])
    return num==sum_digits
unique_sum=0
for num in range(10, 1000001):
    if is_unique(num):
        unique_sum+=num
print(unique_sum)
#33333333333333333333333333333333333333333333333333333333333
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
