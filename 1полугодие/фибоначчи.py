s=()
n1=int(1)
n2=int(1)
n=int(input(f"Введите конечный номер числа ряда >>> "))
for i in range (2,n):
    n1, n2 = n2, n1+n2
    print(n2)
