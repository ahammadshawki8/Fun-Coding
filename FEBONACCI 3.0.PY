# displaying fibonacci series using while loop
first=0
second=1
while first<10000:
    print(first)
    temp=first
    first=second
    second=temp+second
