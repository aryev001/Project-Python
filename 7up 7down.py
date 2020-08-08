import random
print("Welcome to 7 up 7 down!")
credit=int(input("Enter your bidding amount:- "))
print("----------------------------------------")
print("1:7 Up");
print("2:Equals 7");
print("3:7 Down");
print("----------------------------------------")
rand1=random.randint(1,6)
rand2=random.randint(1,6)
c=rand1+rand2
num=int(input("Enter Your Choice:- "))
print("Waiting for Number")
print("The answer is: ",c)
if(num==1):
     if(c>7):
      credit=credit*2
      print("Congrats! You win")
     else:
      credit=0
      print("You Lost,Better luck next time")

elif(num==2):
     if(c==7):
      credit=credit*20
      print("Congrats! You win")
     else:
      credit=0
      print("You Lost,Better luck next time")


elif(num==3):
     if(c<7):
      credit=creditcredit*2
      print("Congrats! You win")
     else:
      credit=0
      print("You Lost,Better luck next time")

else:
        print("Sorry the number isn't an option")
print("Your balance is: ",credit)
