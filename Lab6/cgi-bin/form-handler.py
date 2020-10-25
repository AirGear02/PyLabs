# -*- coding: cp1251 -*-
import cgi

form = cgi.FieldStorage()
num1 = int(form.getfirst('num1'))
num2 = int(form.getfirst('num2'))

result = max(num1, num2)/min(num1, num2)

print('Content-type: text/html\n')
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Варіант 8</title>
            <link rel="stylesheet" href="./../bootstrap.min.css">
        </head>
        <body>""")

print('<h1  align="center">Результат: {}</h1>'.format(result))
print('</body></html>')

