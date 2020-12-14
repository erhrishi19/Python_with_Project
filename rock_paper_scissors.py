# A Project on rock paper scissors
#(A course on Python projects by @Kyle_ying source:(Youtube))
"""
Created by @Hrishikesh_Salunkhe
"""
import random

def play():
    user = input("r for rock, p for paper, and s for scissors")
    computer= random.choice(['r','p','s'])
    if(user == computer):
        return 'It\'s a tie'
    if(is_win(user,computer)):
        return "You won!"
    return "You Lost"
#Rules are as follows
#r>s, s>p, p>r
def is_win(player, opponent):
    if((player == 'r' and opponent== 's') or (player == 's' and opponent== 'p') \
        or  (player == 'p' and opponent== 'r')):
        return True


print(play())