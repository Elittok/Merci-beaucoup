import random
card=['6', '7', '8', '9', '10', 'valet', 'queen', 'king', 'tuz']
suit=[' trefi', ' bubni', ' chervi', ' piki']
l=[]
for i in range (len(card)):
    for x in range (len(suit)):
        l.append(card[i]+suit[x])
a=len(l)
random.shuffle(l)
print(l)
print()
print(a)
print()
b=l[:6]
print(b)
print()
l=l[6::]
print(l)
print()
f=l[:6]
print(f)
l=l[6::]
print(l)
k=l[0]
l=l[1::]
l.append(k)
k=str(k)
print(l)
print(k)
k=k.split(" ")
k=k[1]
print(k)
