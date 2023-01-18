x=int(1)
y=int(1)
z=int()
p=int(input("Введите основание степени счисления >>> "))
print(f"{p}- ичная система счисления")
for x in range (1,p):
    for y in range (1,p):
        z=(x*y//p)*10+(x*y)%p
        print(z,end=' ')
    print()
