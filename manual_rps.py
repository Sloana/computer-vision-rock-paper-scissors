import random
def get_computer_choice():
   rps=["Rock","Paper","Scissors"]
   choice=random.choice(rps)
   return choice


def get_user_choice():
    user_choice=input("Enter a choice")
    return user_choice
