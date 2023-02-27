sp=[1, 3, 4, 9, 5, 9, 2, 8, 9, 1, 7, 7, 8, 6, 2, 3, 1, 3, 3, 8]
print(sp)
b=len(sp)
sp = sp+sp
print(sp)
spl=sp[7:27]
a=0
for i in range(20):
    if i>10:
        a=a + (20-i)*spl[i]
    else:
        a = a + spl[i]*i
print(a)

