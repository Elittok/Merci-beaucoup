x=int(input("Введите основание степени >>> "))
y=int(input("Введите показатель степени >>> "))
Itogo=int(1)
for i in range(y):
    Itogo=Itogo*x
    print(f"{Itogo}")
print(f"Основание степени {x} в степени {y} равно {Itogo}")    
