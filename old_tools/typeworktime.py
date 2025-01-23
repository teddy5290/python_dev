##sleep五秒後 自動填入085x 180x 五次 (填一周工時用)

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random

time.sleep(5)
k = PyKeyboard()

for round in range(1,6,1):
    type_str=str('085'+str(random.randint(0,9))+'180'+str(random.randint(0,9)))
    k.type_string(type_str)