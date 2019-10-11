# displaying febonacci series using for loop
first=0
second=1
n=int(input("enter how many numbers you want in this series: "))
for i in range(n):
        print(first)
        temp=first
        first=second
        second=temp+second