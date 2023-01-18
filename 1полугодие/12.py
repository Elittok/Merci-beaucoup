def g(n):
    l = True
    for d in range(2,n):
        if n % d ==0:
            l = False
            break
    return l
f= 117
while not g(f):
    f += 4
p=(f-117)//4
print(p)
