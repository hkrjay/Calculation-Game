# ===== Calculation Game =======
# In this you have to solve different mathmatical operations(+,-,/,%) number ranging from (1-50) and earn score as much as possible
# 1 score for Correct answer 


import random

def calgame():
    print("\tCALCULATION GAME \t".center(50,'*'))
    count=0
    l=['*','+','-','%']
    while True:
        a=random.randint(1,50)
        b=random.randint(1,50)
        random_cal=random.choice(l)
        print(a , random_cal , b , '=' ,end=' ')
        usr=int(input())
        if random_cal=='+':
            if a+b==usr:
                print("Correct")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
        elif random_cal=='-':
            if a-b==usr:
                print("Correct")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
        elif random_cal=='*':
            if a*b==usr:
                print("Correct")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
        elif random_cal=='%':
            if a%b==usr:
                print("Correct")
                count+=1
            else:
                print('\t:( Wrong :(')
                break
    
    print('Total Score = ', count)

calgame()