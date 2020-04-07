t=int(input())
l=[]
for i in range(t):
	a,b=map(int,input().split())
	l.append([a,b])
for k in l:
	n=k[0]
	x=k[1]
	d=0
	for z in range(n):
		m=d
		for c in range(x+1):
			d+=c
		d=d-m
		x=d
	print(d)