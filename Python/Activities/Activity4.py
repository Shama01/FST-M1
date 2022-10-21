from ast import Pass, Raise


u1= input("What is player 1 name")
u2= input("What is player 2 name")
u1_choice= input(u1+" "+"Choose rock, paper or scissor")
u2_choice= input(u2+" "+"Choose rock, paper or scissor")
while True:
    if u1_choice=='rock' and u2_choice=='scissor':
        print(u1+" "+" wins")
    elif u1_choice=='scissor' and u2_choice=='rock':
        print(u2+" "+" wins")
    elif u1_choice=='scissor' and u2_choice=='paper':
        print(u1+" "+" wins")
    elif u1_choice=='paper' and u2_choice=='scissor':
        print(u2+" "+" wins")
    elif u1_choice=='paper' and u2_choice=='rock':
        print(u1+" "+" wins")
    elif u1_choice=='rock' and u2_choice=='paper':
        print(u2+" "+" wins")
    elif u1_choice==u2_choice:
        print("The game is tie")
    else:
        print("Wrong input")
    u_play= input("Do you want to play another round- Yes/No")
    if u_play=="yes":
        Pass
    elif u_play=="no":
        raise SystemExit
    else:
        print("Wrong input, exiting")
        raise SystemExit