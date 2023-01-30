a=[1,2,3,0]
#b=[n*2 for n in a if n<2]
#b=[[i,x] for i,x in enumerate(a)]
#enumerate-вытаскивает значение и его поицию
#b=[i+i for i,i in zip(a,a)]
#zip-скрещивание 2х объеков
#b=[("true" if n>2 else 'false') for n in a]
#b=[i+j for i in a for j in a]
#b=[[i*n for i in range(1,n+1)]for n in a]
#def b(n):
    #c=n**2
    #print(c)
#b(5)
#f=lambda x: 'true' if x else 'false'
#print(f(1))
#print('true' if any(a) else 'false')
#print(list(map(lambda x:str(x),a)))
#print(list(map(str(a),a)))-не работает
print(list(filter(lambda x: x%2==0,a))if a else 0)
