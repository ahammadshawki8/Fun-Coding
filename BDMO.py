# def tt(i):
#     if i==1:
#         return 3
#     elif i==2:
#         return 6
#     else:
#         ans=tt(i-1)-tt(i-2)+1011
#         return ans
# print(tt(1))
# print(sum(range(253,277)))

def isprime(x):
    p=0
    for n in range (2,x):
        if x%n==0:
            p +=1
    if p>=1:
        return False
    else:
        return True
def df(i):
    x=23*i+7
    if isprime(x):
        return True
    False
print(df(32))