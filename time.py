import time
from datetime import datetime
from random import randint
from winsound import Beep
import sys
input=sys.argv[1]
print(input)


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
