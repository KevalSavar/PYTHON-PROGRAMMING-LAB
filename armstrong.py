x=input('enter the number to be evaluated : ')
n=len(x)
sum=0
for i in range(0,n):
	sum+=int(x[i])**n
if int(x)==sum:
	print('armstrong no. : ')
else:
	print('not')


