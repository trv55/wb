#!/usr/bin/env python
#-*- coding: euc-kr -*-

import cgi
import cgitb    #스크립트 오류 등의 에러발생시 브라우저에 에러 내용을 보여준다.
cgitb.enable()

print("Content-type: text/html\n")    #\n 을 안하면 Internal Server Error 발생!

print('<html>')
print('<head>')
print('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')

form = cgi.FieldStorage()

if "email" not in form:
    print("Error!")
else:
    print("Your email address is " + form["email"].value)


print('</body>')
print('</html>')
