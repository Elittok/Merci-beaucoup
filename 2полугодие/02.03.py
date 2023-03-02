with open('27_A.txt') as f:
    s=[x for x in f]
    s.pop(0)
    print(s)
    d=[]
    for i in s:
        d.append(i.split())
    print(d[0][1])
