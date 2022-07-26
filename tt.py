import random
from colorama import Fore,init
sets=1

score=0
    
while score<1:
    d=[1,2,3,4,5,6]
    v= random.choices(d,k=4)
    if v[0]==v[1] or v[0]==v[2] or v[0]==v[3] or v[1]==v[2] or v[1]==v[3] or v[2]==v[3] :
        pass
    else:
        score+=1
        # print(v)

while sets<12:
    
    init()
 

    print(Fore.MAGENTA+"* [blue=1 , green=2, black=3, red=4, white=5, yellow=6] *")
    print(Fore.GREEN+' set '+str(sets))
    print(Fore.LIGHTCYAN_EX)
    x=int(input("\n write1 ==>>>  "))
    y=int(input('\n write2 ==>>>  '))
    z=int(input('\n write3 ==>>>  '))
    n=int(input('\n write4 ==>>>  '))


    # 1=='blue'
    # 2=='green'
    # 3=='black'
    # 4=='red'
    # 5=='white'
    # 6=='yellow'

    num=0
    for i in range(1):
        if x==v[0] or x==v[1] or x==v[2] or x==v[3]:
         num+=1 
        if y==v[0] or y==v[1] or y==v[2] or y==v[3]:
         num+=1 
        if z==v[0] or z==v[1] or z==v[2] or z==v[3]:
         num+=1 
        if n==v[0] or n==v[1] or n==v[2] or n==v[3]:
         num+=1 
    print() 
    print(Fore.GREEN+' [+] '+str(num)+' color are in choice')
        

    cum=0
    for i in range(1):
        if x==v[0]:
         cum+=1 
        if y==v[1]:
         cum+=1 
        if z==v[2]:
         cum+=1 
        if n==v[3]:
         cum+=1 
    print()
    print(Fore.GREEN+' [+] '+str(cum)+' place are correct')

    if cum==4:
        print()
        print(Fore.YELLOW+' [+] The match finished! you are winned!')
        break


    sets+=1
    if sets==10:
        print()
        print(Fore.YELLOW+' [-] The match finished! you are losed!')
        break
















