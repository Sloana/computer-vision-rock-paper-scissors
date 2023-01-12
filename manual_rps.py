import random

rps=["Rock","Paper","Scissors"]


def get_computer_choice():
   choice=random.choice(rps)
   return choice


def get_user_choice():
    user_choice=input("Enter a choice")
    return user_choice
