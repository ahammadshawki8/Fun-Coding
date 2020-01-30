def factor(n):
    factorlist=[]
    for i in range(2,n):
        if n%i==0:
            factorlist.append(i)
    return factorlist

user=int(input())
userlist=[]
while user>0:
    userlist.append(user)
    user=int(input())
for i in userlist:
    factorlist=factor(i)
    final=[]
    if len(factorlist)==0:
        final.append(i)
    else:    
        while len(factorlist)>2:
            final.append(factorlist[0])
            factorlist=factor(factorlist[-1])
        final.append(factorlist[0])
        final.append(factorlist[-1])
    print(final)



