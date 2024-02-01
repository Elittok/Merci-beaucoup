#------------------------1й способ-----------------
#s = open('24_10105 (2).txt').readline()
#s = s.split('T')
#m = 10000
#for i in range(len(s) - 100):
#    c = 'T'.join(s[i:i+101])
#    m = min(m, len(c) - len(s[i])-len(s[i+100]))
#print(m)
#-------------------------min(100)-----------------
#s = open('24_10105 (2).txt').readline()
#s = s.split('T')
#m = 0
#for i in range(len(s) - 100):
#    c = 'T'.join(s[i:i+101])
#    m = max(m, len(c))
#print(m)
#-------------------------max(133)-----------------
#-----------------------2й способ------------------
#s = open('24_10105 (2).txt').readline()
#s = s.split('T')
#m = 10000
#for i in range(len(s) - 100):
#    c = 'T'.join(s[i:i+99])
#    c = 'T'+str(c)+'T'
#    m = min(m, len(c))
#print(m)
#--------------------------------------------------
#s = open('24_10105 (2).txt').readline()
#s = s.split('T')
#m = 0
#for i in range(len(s) - 100):
#    c = 'T'.join(s[i:i+99])
#    c = 'T'+str(c)+'T'
#    m = max(m, len(c))
#print(m)
#----------------------------ЯНВАРСКИЙ ВАРИАНТ-------
#s = open('24.txt').readline()
#counter = 1
#ct = 0
#res = 0
#for i in range(len(s)-1):
#    if(s[i]<s[i+1]):
#        if((s[i] == 'A') or (s[i] == 'E') or (s[i] == 'I') or (s[i] == 'O') or (s[i] == 'U') or (s[i] == 'Y')):
#            if ct>=2:
#                ct = 1
#                counter = 1
#            else:
#                ct +=1
#                counter += 1
#                res = max(res, counter)
#        else:
#            counter += 1
#            res = max(res, counter)
#    else:
#        counter = 1
#print(res)
#-------------------------------№ 12476 PRO100 ЕГЭ 29.12.23 (Уровень: Сложный)-------------------
s = open('24_12476.txt').readline()
