from art import logo,vs
from game_data import data
import random
print(logo)

def print_screen(account):
    return f"{account['name']}, {account['description']}, from {account['country']}."

def check_result(a_followers,b_followers,guess):
    if(a_followers > b_followers):
        return guess == 'A'
    else:
        return guess == 'B'    

lose = 0
score = 0
B = random.choice(data)
while lose == 0 :
    A = B
    B = random.choice(data)
    while(A==B):
        B = random.choice(data)
    print(f"Compare A : {print_screen(A)} .")
    print(vs)
    print(f"Against B : {print_screen(B)} .")

    guess = input("who has more followers ? Type A or B : ").upper()

    is_correct = check_result(A['follower_count'],B['follower_count'],guess)
    
    if(is_correct):
        score+=1
        print(f"You 're Right! , Current score : {score}")

    else :
        lose = 1
        print(logo)      
        print(f"Sorry That's Wrong, Final Score : {score}")

