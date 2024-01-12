#                       24 - 10105

with open('24_10105.txt') as f:
    s = f.readline()
    a = 0
    pos = [x for x in range(len(s)) if s[x] == 'T']
    for i in range(len(pos)-101):
        a = max(pos[i + 101] - pos[i] - 1, a)
    print(a)


#                        24 - 10724
#import re
#with open('24_10724.txt') as f:
#    d = [len(x) for x in re.findall(r"[1-9ABCDEF]+[0-9ABCDEF]*", f.readline())]
#    print(max(d))

    
#f = open('24_10724.txt')
#s = f.readline()
#alf16 = ('0123456789ABCDEF')
#maxl = 0
#l = 0
#for x in s:
#    if x in alf16:
#        if x != '0':
#            l+=1
#        else:
#            if l != 0:
#                l += 1
#    else:
#        l = 0
#    maxl = max(maxl, l)
#print(maxl)
#-------------------------------------------------------------------------------    
