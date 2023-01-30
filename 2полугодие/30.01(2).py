a=[['c','m',[60,80,82]],
  ['b','f',[10,20,5]],
  ['a','m',[70,90,100]]]
b=[(name,"получит" if sum(scores)/len(scores)>=50 else "HET")
   for name,gendor,scores in a if gendor=='m']
a.sort(key=lambda x:x[1])
print([[name,gendor] for name,gendor,scores in a])
#print(b)
