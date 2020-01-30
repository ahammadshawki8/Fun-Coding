# SOLVED BY __proRajukians__
# LANGUAGE --> python 3.7.5
# COMPILER --> VISUAL STUDIO CODE

# ICPC 2018 <1>
name=input()
print(name[-1::-1])

# ICPC 2018 <2>
line=int(input())
box=[]
for i in range(line):
    sides=input()
    box.append(sides)

def area(i):
    a,b,c=i.split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    if (a+b)<=c or (b+c)<=a or (a+c)<=b:
        return "Oh, No!"
    else:
        import math
        s=(a+b+c)/2
        value=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return "%.2f"% round(value,2)
a=list(map(area,box))
for i in a:
    print(i)
       
# ICPC 2018 <3>
for i in range (10,0,-1):
    print(i)          

# ICPC 2018 <4>
dx=input()
dy =input()
for i in range(dx):
    while len(input())<=dy:
        maze=input()
