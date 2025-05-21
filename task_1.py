def Adithya(x,y,z):
	a=0
	b=1
	if x%2==0 and y%2==0 and z%2==0:
		a=x+y+z
		print("a:",a)
	elif x%2!=0 and y%2!=0 and z%2!=0:
		b=x*y*z
		print("b :",b)
	elif x%2!=0 and y%2!=0 and z%2==0:
		c=x+y-z
		print("c :",c)
	elif x%2==0 and y%2==0 and z%2!=0:
		d=x-y+z
		print("d :",d)
		return a,b,d
Adithya(12,14,16)
Adithya(11,13,15)
Adithya(13,25,22)
Adithya(12,14,25)
