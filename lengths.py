#!/usr/local/bin/python3

from cgitb import enable

enable()

from cgi import FieldStorage
from html import escape

print('Content-Type: text/html')
print()

form_data = FieldStorage()
length = escape(form_data.getfirst('length', '').strip())
units = form_data.getfirst('units')


outcome = ''

try:
    length = float(length)
    inches = 0.0
    feet = 0.0
    yards = 0.0

    if units in ['inches', 'feet', 'yards']:
        if units == 'inches':
            inches = length
            feet = length / 12
            yards = length / 36

        elif units == 'feet':
            inches = length * 12
            feet = length
            yards = length / 3

        else:
            inches = length * 36
            feet = length * 3
            yards = length
        outcome = """
            <table>
                <tr>
                    <th>Inches: </th><td>%.2f</td>
                </tr>
                <tr>
                    <th>Feet: </th><td>%.2f</td>
                </tr>
                <tr>
                    <th>Yards: </th><td>%.2f</td>
                </tr>
            </table>""" % (inches, feet, yards)
    else:
        outcome = 'Error! Enter a valid unit.'

except ValueError:
    outcome = 'Error! Enter a valid number.'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Length</title>
        </head>
        <body>
            <p>
                %s
            </p>
        </body>
    </html>""" % (outcome))
