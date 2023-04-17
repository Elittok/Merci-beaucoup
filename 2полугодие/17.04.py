with open ('27_B.txt') as f:
    s=[x for x in f]
    s.pop(0)
    d=[]
    m=[]
    l=0
    for i in s:
        d.append(list(map(int, i.split())))
    for i in d:
        if i[1] % 36 == 0: i[1] = i[1] // 36
        if i[1] % 36!=0: i[1] = i[1] // 36 + 1
    for i in range(549840,  549860, 1):
        b=d[i][0]
        for y in d:
            l=l+abs(y[0]-b)*y[1]
        m.append(l)
        print(l, i)
        l=0
    print()
    print(len(d))
    print(min(m), m.index(min(m))+1)
    #print(min(m), m.index(min(m))) -27_A
    
