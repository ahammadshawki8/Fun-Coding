# Head_tail game
import time
import random
score_list=[1,2,3,4,5,6]
bat_ball=["batting","balling"]

def start(): 
    print("Hey I am computer8.08. But you can call me comp.")
    print("I am not interested in this class. So I want to play head_tails.")
    answer=input("Do you want to play with me?(yes/no): ")
    if answer=="yes":
        print("Great.\n")
        print("Its a T20 game. So, I think you know the rules.\n")
        toss()
        print("Thanks for playing this game")
        time.sleep(2)
        print("Creator -->Ahammad Shawki")
        time.sleep(4.5)
    else:
        print("Okay then I will play with Shawki.")
        time.sleep(3)
    

def toss():
    player_toss=input("heads or tails?\n")
    player_num=int(input("player toss: "))
    comp_number=random.choice(score_list)
    print("comp toss:",comp_number)

    if (player_num+comp_number)%2==0:
        real_toss="tails"
    else:
        real_toss="heads"
    print()
    if player_toss==real_toss:
        print("congrats you won the toss!")
        section=input("batting or balling?\n")
    else:
        print("sorry you lost the toss:(")
        section=random.choice(bat_ball) 
    if section=="batting":
        print("you are going to bat first")
        bat_part(section)
    else:
        print("you are going to ball first")
        ball_part(section)
    print()
    

def bat_part(section,comp_total=None):
    out=False
    player_total=0
    while not out:
        run=int(input("player bat: "))
        ball=random.choice(score_list)
        print("comp ball:",ball)
        if run in score_list:
            if run==ball:
                print("out")
                out=True
                print("your total run",player_total)
            else:
                player_total+=run
            if comp_total:
                if comp_total<player_total:
                    print("your total run",player_total)
                    print("you won")
                    time.sleep(3.5)
                    break
                if out:
                    if comp_total>player_total:
                        print("you lost")
                    elif comp_total==player_total:
                        print("Match drawn")
                    time.sleep(3.5)
        else:
            print("please pay a valid shot")
    print()
    if section=="batting":
        print("now you are balling")
        ball_part(section,player_total)

def ball_part(section,player_total=None):
    out=False
    comp_total=0
    while not out:
        run=random.choice(score_list)
        ball=int(input("player ball: "))
        print("comp bat:",run)
        if ball in score_list:
            if run==ball:
                print("out")
                out=True
                print("comp's total run",comp_total)
            else:
                comp_total+=run
            if player_total:
                if comp_total>player_total:
                    print("comp's total run",comp_total)
                    print("you lost")
                    time.sleep(3.5)
                    break
                if out:
                    if comp_total<player_total:
                        print("you won")
                    elif comp_total==player_total:
                        print("Match drawn")
                    time.sleep(3.5)
        else:
            print("please throw a valid ball")
    print()
    if section=="balling":
        print("now you are batting")
        bat_part(section,comp_total)

start()




