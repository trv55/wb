#!/usr/bin/env python
#-*- coding: euc-kr -*-

import cgi
import cgitb    #스크립트 오류 등의 에러발생시 브라우저에 에러 내용을 보여준다.
cgitb.enable()
print("Content-type: text/html\n")    #\n 을 안하면 Internal Server Error 발생!


import time
from datetime import datetime
from random import randint
from winsound import Beep


now = datetime.now()
print ("%s시 %s분" %(now.hour, now.minute))

i = randint(1,3)
time.sleep(i)
print(i)

Beep(524,700)
Beep(587,700)
Beep(659,700)
Beep(698,700)
Beep(784,700)
