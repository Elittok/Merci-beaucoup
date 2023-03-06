mini=10**20
with open ('27-B.txt') as f:
    s=[int(x) for x in f]
    s.pop(0)
    print(s[:10])
    b=len(s)
    s=s+s
    start=0
    fin=1000000
    st=50000
    while True:
        
        for i in range(start, fin, st):
            spl=s[i:i+b]
            a=0
            for x in range(b):
                if x>=b//2:
                    a=a+(b-x)*spl[x]
                else:
                    a=a+spl[x]*x
            print(i, a)
            if a<mini:
                mini=a
                minx=i
        print()
        print(minx, mini)

        start=minx-st
        fin=minx+st
        st=st//10
        if st==0:
            st=1

        print(start, fin, st)
        input()

  
