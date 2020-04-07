def factor(n):
    factorlist=[]
    for i in range(1,n):
        if n%i==0:
            factorlist.append(i)
    return factorlist

def perfecto(n):
    f_list=factor(n)
    sum_f=sum(f_list)
    if sum_f==n:
        return True
    else:
        return False

