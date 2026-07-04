import random


computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice: ")
youDect = {"s":1,"w":-1,"g":0}
reverseDect = {-1:"water",0:"gun",1:"snak"}
you = youDect[youstr]

print(f"you chose {reverseDect[you]}/n computer chose{reverseDect[computer]}")

if (computer == you):
    print("its a draw")

else:
    if(computer ==-1 and you == 1):
        print("you win")

    elif(computer == 1 and you == 0):
        print("you loss")
            

    elif(computer == 1 and you == -1):
        print("you loss")
            

    elif(computer == 1 and you == 0):
        print("you win")
            

    elif(computer == 0 and you == -1):
        print("you win")
            

    elif(computer == 0 and you == 1):
        print("you loss")

    else:
        print("something want rong")    
            