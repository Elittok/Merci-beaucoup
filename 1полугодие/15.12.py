def f ():
    N10=int(input(f"Введите число в десятичной системе счисления >>> "))
    Np=int(0)
    k=int(1)
    p=int(input(f"Введите основание системы счисления, в которую нужно перевести число >>> "))
    while N10!=0:
        Np=Np+(N10%p)*k
        k=k*10
        N10=N10//p
    print(f"Число {N10} в {p}-ичной системе счисления равно {Np}")
    
def g():
    a='0123456789'
    nums=list(a)
    print(nums)
    b='0000000 0001111 0010110 0011001 000101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    print(hem)
    for i in range(len(hem)):
      hem[i]=int(hem[i])
    print(hem)
    def distance(x,y):
      k=7
      for i in range(7):
        if x%10==y%10:
          k=k-1
        x=x//10
        y=y//10
      return k  
    cod=int(input("код"))     
    min=distance(cod,hem[0])
    imin=0
    for i in range(10):
      D=distance(cod,hem[i])
      if D:
        if min==0:
            print(f"код верный: символ {nums[imin]}")
        elif min==1:
            print(f"код исправлен: символ {nums[imin]}")
        else:print("Код неверный")

def j():
    a='abwgdevzijklmnoprstufhcqx'
    abc=list(a)
    print(abc)
    b='.- -... .-- -.. . ...- --.. .. .--- -.- .-..  -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-'
    abcm = b.split()
    indm=str()
    print(abcm)
    tekst=input("Введите текстдля перевода в морзянку(агл.алфавит)")
    for i in range (len (tekst)):
        ind = abc.index(tekst[i])
        indm = indm+abcm[ind]+' '
    print(f"Морзянка = {indm}")

def t():
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

gora=int(input("1 - из 10 в любую\n2 - heming\n3 - морзянка\n4 - таблица умножения в 8 чке\n"))
if gora == 1:
    f()
if gora == 2:
    g()
if gora == 3:
    j()
if gora == 4:
    t()
