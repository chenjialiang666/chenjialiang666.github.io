import os
pos=int(input("Please input already get:"))+1
last=0
while True:
	a=input()
	for i in range(len(a)):
		if a[i]=='/':
			last=i
	print(last)
	b=''
	for i in range(last+1,len(a)):
		b=b+a[i]
	print(b)
	os.system("wget "+a)
	os.rename(b,str(pos)+'.jpg')
	pos=pos+1
