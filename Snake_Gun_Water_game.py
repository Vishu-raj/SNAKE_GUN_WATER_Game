import random
'''1 for snake
-1 for water
0 for gun'''
computer = random.choice([1,-1,0])
youstr = input("enter your choice : ")
youDict = {"s":1, "w":-1,"g":0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = (youDict[youstr])

#By now we have two numbers (variables), You and Computer

print(f"You choice : {reverseDict[you]}\nComputer choice : {reverseDict[computer]}")

if(you==computer):
    print("its a Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Win")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==1 and you==-1):
        print("Computer Win")
    elif(computer==0 and you==1):
        print("Computer Win")
    elif(computer==0 and you==-1):
        print("Computer Win")
    else:
        print("Something went wrong!")