#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage

print('Content-Type: text/html')
print()

form_data = FieldStorage()
fruit = form_data.getlist('fruit')
outcome = 0
fruit_dict = {'apples': 1.59, 'bananas': 1.25, 'jujubes':27.81, 'rambutans': 20.84}
try:
    for values in fruit:
        outcome += fruit_dict[values]
except ValueError:
    outcome = 'Error! lol'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Rock, Paper, Scissors</title>
        </head>
        <body>
            <p>
                %.2f
            </p>
        </body>
    </html>""" % (outcome))

