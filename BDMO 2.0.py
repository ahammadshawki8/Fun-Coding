
def isprime(x):
    p=0
    for n in range (2,x):
        if x%n==0:
            p +=1
    if p>=1:
        return False
    else:
        return True

n=int(input("how many primes you want to print?\n-->"))
primesList=[]
f=2
primes=0
while primes!=n:
    for x in range (f,f*2):
        if isprime(x):
            primes +=1
            primesList.append(x)
            if primes == n:
                break
    f *=2 
print(primesList)

