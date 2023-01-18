a=[]
st=int(5)
Itogo=int()
ss=int(input("Введите показатель системы счисления >>> "))
x=int(input("Введите число в восьмеричной системе счисления >>> "))
a=list(str(x))
print(a)
for i in range(6):
    (a[i])*(ss**st)
    Itogo=Itogo+(int(a[i]))*(8**st)
    st=st-1
print(f"Число {x} в восьмеричной системе счисления при переводе в десятичную будет равно {Itogo} ")

      
