def gen():
#    a=b=1
    for i in c:
        yield i
#        a,b = b,a + b
#for item in gen(11):
#    print(item)
a=range(10)
print(a)
a=list(a)
a.append(2)
a=set(a)
print(a)
b={x for x in a}
print(b)
c=[a,b]
c=list(map(list,c))
d=[]
for x in gen():
    d.extend(x)
print(d)



for i in range(10):
    if i==4:pass
    print(i)
