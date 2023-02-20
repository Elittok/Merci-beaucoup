n=int(input())
x=input()
x=x.split()
x=(list(map(lambda a:int(a),x)))
maxy=x.index(max(x))
miny=x.index(min(x))
if x[maxy]/x[miny]>1:
    print(miny+1,maxy+1)
else:print(0, 0)
    
if maxy<miny:
