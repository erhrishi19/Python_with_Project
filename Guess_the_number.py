# A Project to Guess the number generated by computer
#(A course on Python projects by @Kyle_ying source:(Youtube))
"""
Created by @Hrishikesh_Salunkhe
"""

#Import random module to generate a random number 
import random

#Define a function to guess the number
def guess(x):
    ran_num = random.randint(1, x)
    guess_num =0
    while (guess_num != ran_num):
        guess_num = int(input("Enter a number to check for guessing : "))
        if(guess_num <ran_num):
            print("Number is High")
        elif (guess_num > ran_num):
            print("Number is Low")
    print("Your guess is write")       

number = int(input("number to guess in between "))
guess(number) 

