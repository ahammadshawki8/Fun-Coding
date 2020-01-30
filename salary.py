user=input()
m,n=user.split(" ")
m=int(m)
n=int(n)
dictionary=dict()
if m<1000 and n< 100:
    for i in range(m):
        given=input()
        a,b=given.split(" ")
        b=int(b)
        dictionary[a]=b
totallist=[]
number=0
while number != n:
    total=0
    des=input()
    final=des
    while final.count(".")<1:
        des=input()
        final=final+" "+des
        if final.count(".")==1:
            break
    for key,value in dictionary.items():
        if key in final:
            k=final.count(key)
            total+=value*k
    totallist.append(total)
    number+=1
for i in totallist:
    print(int(i))




                



