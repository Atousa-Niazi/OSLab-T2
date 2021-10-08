#Atousa-Niazi-Abkoh-98440127-OSLab--t2-3-time to second -Python
# i didn't use time functions since it wasn't mentioned if i can

print ('welcome')
st=0
print('enter time :')
print('hour:')
h=int(input())
print('minute:')
m=int(input())
print('second:')
s=int(input())
st=h*60**2
st=m*60+st
st=s+st
print('the answer is : ',st,'seconds')
