def game():
    logic=[ [0,1,-1],
            [-1,0,1],
            [1,-1,0]]


    import random


    no_round=0
    no_of_wins=0
    no_of_draw=0
    no_of_loss=0
    while(no_round<6):
        print(f"*********Round {no_round+1}*********")
        user_chance=int(input("Enter 0 : Snake 1: Water 2: gun - "))
        computer_chance=random.randint(0,2)
        ans=logic[user_chance][computer_chance]
        print(f"you choosed {user_chance}")  # 1-win 0 - draw  -1 - lose
        print(f"Opponent choosed {computer_chance}")

        if(ans==1):
            no_of_wins+=1
            print("Congratulation you won the round!!")
        elif(ans==0):
            print("The round is Draw!!")
            no_of_draw+=1
        else:
            print("You losed this round!!")  
            no_of_loss+=1 

        no_round+=1    


    if(no_of_wins>no_of_loss):
        print(f"You won with {no_of_wins} points. Congratulations!!!")

    elif(no_of_wins==no_of_loss):    
        print(f"The match is draw with {no_of_wins} points each \n opponent points - {6-no_of_wins-no_of_draw}")

    else:
        print(f"You losed the match\n your points - {no_of_wins} \n opponent points - {6-no_of_wins-no_of_draw}")    


    choice=int(input("1: if you want to play again \n 0: if you don't want to play again\n Enter : "))
    if(choice==1):
        game()

print("**********Welcome to The Game**********")
game()
