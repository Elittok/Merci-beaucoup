work = True
act = ''
def summa(a,b):
    c=a+b
    return c
def raznost(a,b):
    n=a-b
    return n
def proiz(a,b):
    d=a*b
    return d
def step(a,b):
    e=a**b
    return e
def dele(a,b):
    f=a/b
    return f
while work == True:
    data = input("ВВЕДИТЕ ПРИМЕР/ВВЕДИТЕ 0 ЧТОБЫ ВЫЙТИ: ")
    if data!='0':
        st=data.split()
        a=float(st[0])
        b=float(st[2])
        if st[1] == '+':
            print(f'{a} + {b} = {summa(a,b)}')
        if st[1] == '-':
            print(f'{a} - {b} = {raznost(a,b)}')
        if st[1] == '*':
            print(f'{a} * {b} = {proiz(a,b)}')
        if st[1] == '**':
            print(f'{a} ** {b} = {step(a,b)}')
        if st[1] == '/':
            print(f'{a} / {b} = {dele(a,b)}')
    else:
        work = False
