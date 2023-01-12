import random

def get_computer_choice():
    rps=["Rock","Paper","Scissors"]
    choice=random.choice(rps)
    return choice


def get_user_choice():
    user_choice=input("Enter a choice")
    return user_choice

computer_choice=get_computer_choice()
user_choice=get_user_choice()
def get_winner(computer_choice,user_choice):

    if computer_choice=="Rock":
        if user_choice=="Scissors":
            winner="computer"
        elif user_choice=="Paper":
            winner="user"
        else:
            winner="tied"
    elif computer_choice=="Scissors":
        if user_choice=="Paper":
            winner="computer"
        elif user_choice=="Rock":
            winner="user"
        else:
             winner="tied"
    else:
        if user_choice=="Rock":
            winner="computer"
        elif user_choice=="Scissors":
            winner="user"
        else:
             winner="tied"
    if winner=="user":
        print("You won!")
    elif winner=="computer":
        print("You lost!")
    else:
        print("It is a tie!")

get_winner(computer_choice,user_choice)
