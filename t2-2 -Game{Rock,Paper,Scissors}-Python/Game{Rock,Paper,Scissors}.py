#Atousa-Niazi-Abkoh-98440127-OSLab--t2-2 - Game{Rock,Paper,Scissors}-Python


import random

#choice [ r=Rock,p=Paper,s=Scissors ]
c=['r','p','s']
ui=0
mi=0
#it count from 0 to 4
for i in range(5):
    print('\n š choose az : r,Rock | p,Paper | s,Scissors ')
    u=input()
    print('\n-------------')
    print(" user = ",u )
    m=random.choice(c)
    print(" computer = ",m )
    print('-------------\n')

    if m in c and u in c :
        if m==u:
            print('š¼ both user and computer are winner š» \n')
            i+=1
        #else if m!=u :
        else :
            if u=='r':
                i+=1
                if m=='p':
                    print("winner is computer š» " ) 
                    mi+=1
                elif m=='s':
                    ui+=1
                    print("winner is user š¼ " ) 
            elif u=='p':
                i+=1
                if m=='r':
                    print("winner is user š¼ " ) 
                    ui+=1
                elif m=='s':
                    print("winner is computer š» " ) 
                    mi+=1
            elif u=='s':
                i+=1
                if m=='p':
                    print("winner is user š¼ " )
                    ui+=1
                elif m=='r':
                    print("winner is computer š» " ) 
                    mi+=1
print('\n\n š„ š„ š„  the game is over š„ š„ š„ ')
print('              you have play for ',i,"time's  and results are š§ : ")
print('\t\t\t\tuser š :',ui,'\t computer  š¤ :',mi)
print('\n  šš the winner is : šš')
if ui > mi :
    print("\t\tš¼ user š¼ " ) 
elif ui < mi :
    print("\t\tš» computer š» ")  
else :
    print('\t\tš¼ both user and computer š» ')