#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
values = form.getlist('operand')

body = ""

try:
    total = sum(map(float, values))
    equation = " + ".join(values) + " = " + str(total)
    body = """\
    <html>
    <head>
    <title>Lab 1 - CGI experiments</title>
    </head>
    <h3>CGI Sums</h3>
    <body>
    <p>{}</p>
    </body>
    </html>""".format(equation)

except (ValueError, TypeError):
    body = "Operands are not numbers."

print("Content-type: text/html")
print()
print(body)
