def f5():
    for N in range(516):
        b=f'{N:b}'
        if N % 2 == 0:
            b+= '10'
        else:
            b = '1' + b + '01'
        if int(b,2)>516:
            print(N)
            break
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f6():
    from turtle import *
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(5)
    done()
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from itertools import product
def f(x,y,z):
    count=0
    for i in range(1,z):
        b=product('12',repeat=i)
        for pr in b:
            a=x
            if x==10 and pr.count('2')>1:continue
            for com in pr:
                if a==17: break 
                if com=='1':a+=1
                else:a*=2
            if a==y: count+=1
    return count             
print(f(10,35,25)*f(1,10,10))

            for x in nn:
                if x in numb:
                    sp.append(x)
            if not sp:
                k+=1
    print(k)
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f9():
    # загрузка текста из txt
    text=t.split(";")
    #result = [int(item) for item in text]
    result = list(map(int, text))
    x=0
    y=x+6
    counter=double_num=0

    while True:
        n=0
        res6=result[x:y]
        for element in res6:
            if res6.count(element)>2:
                for yy in range(res6.count(element)): res6.remove(element) 
                # удаление значений больше 2 штук
            if res6.count(element)==2:
                n+=2   
                double_num=element 
                res6.remove(element)
                res6.remove(element)

        if n==2 and len(res6)==4:  
            if (sum(res6)/len(res6))<=(double_num*2): counter+=1

        print(counter)
        if y>=len(result):break         
        x=x+6
        y=x+6
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f12:
    sp=[]
    for num in range(1, 1000):
        if all(num%x!=0 for x in range(2,num-1)):
            sp.append(num)
    print (sp)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f14():
    a = ("0123456789abcde")
    for x in a:
        f = int(f'123{x}5',15) + int(f'1{x}233',15)
        if f%14==0:
            print(x,f//14)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def f15():
    for a in range(1, 1000):
        if all (((x%2==0) <= (x%3!=0)) or (x+a>=100)for x in range (1, 100)):
            print(a)
            break
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        b=product('12',repeat=i)
        for pr in b:
            a=x
            if x==10 and pr.count('2')>1:continue
            for com in pr:
                if a==17: break 
                if com=='1':a+=1
                else:a*=2
            if a==y: count+=1
    return count             
print(f23(10,35,25)*f23(1,10,10))
