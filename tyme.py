x=int(input('enter time in seconds : '))
day=x//86400
x=x%86400
hour=x//3600
x=x%3600
minute=x//60
second=x%60
print('days :',day,'hours :',hour,'minutes :',minute,'second :',second)



