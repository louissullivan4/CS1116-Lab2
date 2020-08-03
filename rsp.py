#!/usr/local/bin/python3
            
from cgitb import enable
enable()

from cgi import FieldStorage

from random import randint

from html import escape

print('Content-Type: text/html')
print()


form_data = FieldStorage()
user_choice = form_data.getfirst('game')

com_choice = randint(0,2)
outcome = ''
answers = ['rock', 'paper', 'scissors']

if user_choice in answers:
    if user_choice == 'rock' and com_choice == 0:
        outcome = "Computer's Rock ties with User's Rock"

    elif user_choice == 'rock' and com_choice == 1:
        outcome = "User's Rock beats Computer's Scissors"

    elif user_choice == 'rock' and com_choice == 2:
        outcome = "Computer's Paper beats User's Rock"

    elif user_choice == 'scissors' and com_choice == 0:
        outcome = "Computer's Rock beats User's Scissors"

    elif user_choice == 'scissors' and com_choice == 1:
        outcome = "Computer's Scissors ties with User's Scissors"

    elif user_choice == 'scissors' and com_choice == 2:
        outcome = "User's Scissors beats Computer's Paper"

    elif user_choice == 'paper' and com_choice == 0:
        outcome = "User's Paper beats Computer's Rock"

    elif user_choice == 'paper' and com_choice == 1:
        outcome = "Computer's Scissors beats User's paper"

    elif user_choice == 'paper' and com_choice == 2:
        outcome = "Computer's Paper ties with User's Paper"
else:
    outcome = 'Error! Please enter a valid input'


print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Rock, Paper, Scissors</title>
        </head>
        <body>
            <p>
                %s
            </p>
        </body>
    </html>""" % (outcome))
    


    
