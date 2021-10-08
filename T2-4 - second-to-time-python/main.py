#Atousa-Niazi-Abkoh-98440127-OSLab--t2-3- second to time-Python
# i didn't use time functions since it wasn't mentioned if i can

print ('welcome')
st=0
print('enter time az seconds :')
s=int(input())

# 1 d = 24 * 3600 s
rd = s % (24 * 3600)
d=s/(24*3600) - rd/(24 * 3600)
rh=rd % 3600
h = rd/(3600) - rh/3600
rm=rh%60
m = rh/60 - rm/60
rs=rm

print('days :',d)
print('hours:',h)
print('minutes:',m)
print('seconds:',rs)
print('or az :',d,':',h,':',m,':',s)