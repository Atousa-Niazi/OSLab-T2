#Atousa-Niazi-Abkoh-98440127-OSLab--t2-2 - Game{Rock,Paper,Scissors}-Python


import random

#choice [ r=Rock,p=Paper,s=Scissors ]
c=['r','p','s']
ui=0
mi=0
#it count from 0 to 4
for i in range(5):
    print('\n 🔆 choose az : r,Rock | p,Paper | s,Scissors ')
    u=input()
    print('\n-------------')
    print(" user = ",u )
    m=random.choice(c)
    print(" computer = ",m )
    print('-------------\n')

    if m in c and u in c :
        if m==u:
            print('🌼 both user and computer are winner 🌻 \n')
            i+=1
        #else if m!=u :
        else :
            if u=='r':
                i+=1
                if m=='p':
                    print("winner is computer 🌻 " ) 
                    mi+=1
                elif m=='s':
                    ui+=1
                    print("winner is user 🌼 " ) 
            elif u=='p':
                i+=1
                if m=='r':
                    print("winner is user 🌼 " ) 
                    ui+=1
                elif m=='s':
                    print("winner is computer 🌻 " ) 
                    mi+=1
            elif u=='s':
                i+=1
                if m=='p':
                    print("winner is user 🌼 " )
                    ui+=1
                elif m=='r':
                    print("winner is computer 🌻 " ) 
                    mi+=1
print('\n\n 🔥 🔥 🔥  the game is over 🔥 🔥 🔥 ')
print('              you have play for ',i,"time's  and results are 🧐 : ")
print('\t\t\t\tuser 😎 :',ui,'\t computer  🤖 :',mi)
print('\n  🌟🌟 the winner is : 🌟🌟')
if ui > mi :
    print("\t\t🌼 user 🌼 " ) 
elif ui < mi :
    print("\t\t🌻 computer 🌻 ")  
else :
    print('\t\t🌼 both user and computer 🌻 ')