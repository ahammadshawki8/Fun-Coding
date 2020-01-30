# printing out the co-prime number
def factor(n):
    factorlist=[]
    for i in range(2,n):
        if n%i==0:
            factorlist.append(i)
    return factorlist

user=input()
inputlist=[]
while user !="0":
    user=int(user)
    if user<1000000000:
        inputlist.append(user)
    user=input()

for x in inputlist:
    z=factor(x)
    final=[]
    for i in range(2,x):
        k=0
        for m in z:
            if i%m==0:
                k+=1
        if k==0:
            final.append(i)
    print(len(final))

