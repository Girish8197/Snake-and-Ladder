import random

def dice_throw():
        no1=random.randint(1,6)
        if(no1==0):
            print("\t\t---------")
            print("\t\t[       ]")
            print("\t\t[       ]")
            print("\t\t[       ]")
            print("\t\t---------")
        elif(no1==1):
            print("\t\t---------")
            print("\t\t[       ]")
            print("\t\t[   0   ]")
            print("\t\t[       ]")
            print("\t\t---------")
        elif(no1==2):
            print("\t\t---------")
            print("\t\t[ 0     ]")
            print("\t\t[       ]")
            print("\t\t[     0 ]")
            print("\t\t---------")
        elif(no1==3):
            print("\t\t---------")
            print("\t\t[ 0     ]")
            print("\t\t[   0   ]")
            print("\t\t[     0 ]")
            print("\t\t---------")
        elif(no1==4):
            print("\t\t---------")
            print("\t\t[ 0   0 ]")
            print("\t\t[       ]")
            print("\t\t[ 0   0 ]")
            print("\t\t---------")
        elif(no1==5):
            print("\t\t---------")
            print("\t\t[ 0    0]")
            print("\t\t[   0   ]")
            print("\t\t[0    0 ]")
            print("\t\t---------")
        elif(no1==6):
            print("\t\t---------")
            print("\t\t[ 0   0 ]")
            print("\t\t[ 0   0 ]")
            print("\t\t[ 0   0 ]")
            print("\t\t---------")
        return no1
    
def snake(sum):
    if sum==16:
        print("\n\tSnake bite you\n")
        sum=sum-3
        print("\tYou are returned back from 16 to ",sum,"\n")
        return sum
    elif sum==31:
        print("\tSnake bite you")
        sum=sum-27
        print("\tYou are returned back from 31 to ",sum,"\n")
        return sum
    elif sum==47:
        print("\tSnake bite you")
        sum=sum-22
        print("\tYou are returned back from 47 to ",sum,"\n")
        return sum
    elif sum==66:
        print("\tSnake bite you")
        sum=sum-14
        print("\tYou are returned back from 66 to ",sum,"\n")
        return sum
    elif sum==63:
        print("\tSnake bite you")
        sum=sum-3
        print("\tYou are returned back from 63 to ",sum,"\n")
        return sum
    elif sum==97:
        print("\tSnake bite you")
        sum=sum-22
        print("\tYou are returned back from 97 to ",sum,"\n")
        return sum
    else:
        return sum
    
def ladder(sum):
    if sum==3:
        print("\n\tyou got a ladder\n")
        sum=sum+36
        print("\tyou went from 3 to ",sum,"\n")
        return sum
    elif sum==10:
        print("\n\tyou got a ladder\n")
        sum=sum+2
        print("\tyou went from 10 to ",sum,"\n")
        return sum
    elif sum==27:
        print("\n\tyou got a ladder\n")
        sum=sum+26
        print("\tyou went from 27 to ",sum,"\n")
        return sum
    elif sum==56:
        print("\n\tyou got a ladder\n")
        sum=sum+28
        print("\tyou went from 56 to ",sum,"\n")
        return sum
    elif sum==61:
        print("\n\tyou got a ladder\n")
        sum=sum+38
        print("\tyou went from 61 to ",sum,"\n")
        return sum
    elif sum==72:
        print("\n\tyou got a ladder\n")
        sum=sum+18
        print("\tyou went from 72 to ",sum,"\n")
        return sum
    else:
        return sum

def end(sum,x):
   if sum>100:
       sum=sum-x
       return sum
   else:
       return sum


print("\n****************************************")
print("\t\tSNAKE AND LADDER")
print("****************************************")

print("\nLadder is at\n3, 10, 27, 56, 61, 72\n")
print("\nSnake is at\n16, 31, 47, 66, 63, 97\n")

person1=input("Enter the name of player 1 : ")
person2=input("Enter the name of player 2 : ")

sum1=0
sum2=0
x='y'

while(x=='y'):
    if(sum1<100):
         print("*************************************")
         print("\n\t",person1,"your turn ")
         x=input("Enter y to throw the dice : ").lower()
         a=dice_throw()
         sum1=sum1+a
         sum1=snake(sum1)
         sum1=ladder(sum1)
         sum1=end(sum1,a)
         print("\n\t\tYou are at ",sum1,"\n")
         print("*************************************")
    else:
        print("\n***************************************")
        print("\t\t\t",person1,"is the winner")
        print("*************************************")
        break;
    if(sum2<100):
         print("*************************************")
         print("\n\t",person2,"your turn")
         x=input("Enter y to throw the dice : ").lower()
         b=dice_throw()
         sum2=sum2+b
         sum2=snake(sum2)
         sum2=ladder(sum2)
         sum2=end(sum2,b)
         print("\n\t\tYou are at ",sum2,"\n")
         print("*************************************")
    else:
        print("\n***************************************")
        print("\t\t\t",person2,"is the winner")
        print("*************************************")
        break;