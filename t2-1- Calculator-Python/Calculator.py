
# Atousa niazi - python - simple calculator-os lambda
# python be tazegy switch case avorde ama ma inja ba elif minevisim

''' capability : sum-sub-div-mut-sin - cos - tan - cot - log
    functions in use : round,radians,sin,cos,tan,log
    Radians = 180/pi Degrees.
'''

import math

print ('\n welcome 🌼 👋 🌼')
while True: 
    print ('\n choose an operator:🚩 ')
    print('-----------')
    print('+,sum')
    print('-,sub')
    print('*,mut')
    print('/,div')
    print('s,sin')
    print('c,cos')
    print('t,tan')
    print('k,cot')
    print('l,log')
    print('e,exit')
    print('-----------\n')
    
    #to get operator:
    op=input()
    
    #for binary operator:
    if op=='+'or op=='-' or op=='*' or op=='/' or op=='l':
        if op=='l':
            print('log')
            a=int(input())
            print('Base')
            b=int(input())
            print('\n log = ',math.log(a,b))
        elif op!='l':
            print('enter 2 num :')
            a=int(input())
            b=int(input())
            if op=='+':
                print (a,'+',b,'=' , a+b)
            elif op=='-':
                print (a,'-',b,'=',a-b)
            elif op=='*':
                print (a,'*',b,'=',a*b)
            elif op=='/':
                if b!=0:
                    print (a,'/',b,'=',round((a/b),2))
                elif b==0:
                    print('❌ cannot div by zero! ❌ ' )


    #for Unique operator:
    elif op=='s'or op=='c'or op=='t'or op=='k':
        print('enter a degree :')
        c=int(input())
        c= math.radians(c)
        if op=='s':
            print('sin(',c,') =',round(math.sin(c),2))
        if op=='c':
            print('cos(',c,') =',round(math.cos(c),2))
        if op=='t':
            print('1) tan(',c,') =',round(math.tan(c),2))
        if op=='k':
            # since math library doesn't have a cot method we use mathematical formula
            cot=1/(math.tan(c))
            print('cot(',c,') =',round(cot,2))
 
    #for end of calculator:
    elif op=='exit' or  op=='e':
        print('good luck ! 🌼 🌼  👋 ')
        break

    #for wrong operator:
    else :
        print( 'try again!!⚠🧐')

