
#Atousa-Niazi-Abkoh-98440127-OSLab--t2-3-Game{palam,polom,pilich}-Python


import random

#choice [ u,Up and d,down]
a=['u','d']
pi=0
c1i=0
c2i=0
l=[0,0,0]
t=1
j=0
while True:
    ui=0
    di=0
    print('Game : ',t)
    print('choose az :')
    print('| u,Up | ')
    print('|d,down| ')
    print('|e,exit| ')
    p=input()
    c1=random.choice(a)
    c2=random.choice(a)

    # exit game
    if p=='e':
        print('end of game.')
        break
    #playing 
    elif p in a :
       
        print('-------------')
        print(" user = ",p )
        print(" computer 1 = ",c1 )
        print(" computer 2 = ",c2 )
        print('-------------')
        result_list = [p,c1,c2]
        # Result from count matches with result from len()
        result = result_list.count(result_list[0]) == len(result_list)
        #All the elements are Equal
        if (result):
            print('no loser !')
            t+=1
        #Elements are not equal
        else:
            for j in range(3):
                if j<3:
                    if result_list[j]=='u':
                        ui+=1
                        l[j]=0
                    elif result_list[j]=='d':
                        di+=1
                        l[j]=1
                else :
                    break
            print('ui',ui,'di',di)
            if di!=1:
                if l[0]==0:
                    t+=1
                    print('the loser is user !')
                    pi+=1
                elif l[1]==0:
                    t+=1
                    print('the loser is Computer1 !!')
                    c1i+=1
                elif l[2]==0:
                    t+=1
                    print('the loser is Computer2 !!!')
                    c2i+=1
            elif di==1 :
                if l[0]==1:
                    t+=1
                    print('the loser is user !')
                    pi+=1
                elif l[1]==1:
                    t+=1
                    print('the loser is Computer1 !!')
                    c1i+=1
                elif l[2]==1:
                    t+=1
                    print('the loser is Computer2 !!!')
                    c2i+=1
                else :
                    print('di 0 , 1  is wrong')
            else :
                print('di is wrong')
            print('~~~~~~~~~~~~~~')
            print('~~~~~~~~~~~~~~')
        # wrong choice you have to try again
    #wrong choice
    else :
        print('try again.!')

print('\n=====================')
print('=====================')
print('  the game is over.  ')
print('  you have play for',t,"time's and total results are (lossing times) : ")
print('\tuser :',pi,'\t computer1  :',c1i,'\t Computer2 :',c2i)
print('\n   the winner is : ')
x = min(pi,c1i,c2i)
if pi==c1i and pi==c2i :
    print('      no one .')
if x==pi :
    if pi==c1i:
        print('      user and computer1')
    elif pi==c2i:
        print('      user and Computer2')
    else:
        print('      user')
elif x==c1i :
    if c1i==c2i:
        print('      computer1 and Computer2')
    else:
        print('      computer1')
elif x==c2i :
        print('      Computer2')
print('=====================')
print('=====================')