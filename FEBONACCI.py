# making a function which can display febonacci series.
def febonacci(n):
        if n==1 or n==2:
                return 1
        return febonacci(n-1)+febonacci(n-2)
for i in range(1,10):
        print(febonacci(i))