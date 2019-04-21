def fab():
	b=0
	print(b,end=",")
	c=1
	print(c,end=",")
	d=b+c
	for i in range(1,a):
		print(d,end=",")
		b=c
		c=d
		d=b+c
				
		
a=int(input("number"))
fab()
