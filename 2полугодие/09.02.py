from itertools import product
count=0
for i in range(2,25):
    b=product('12',repeat=i)
    for n in b:
        a=10
        if n.count('2')>1:continue
        for x in n:
            if x=='1': a+=1
            else:a*=2
            if a==17:break
        if a==35:count+=1
print(count)
