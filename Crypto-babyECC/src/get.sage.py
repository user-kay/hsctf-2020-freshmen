

# This file was *autogenerated* from the file ./src/get.sage
from sage.all_cmdline import *   # import sage library

_sage_const_125102209 = Integer(125102209); _sage_const_24 = Integer(24); _sage_const_23 = Integer(23); _sage_const_78828931 = Integer(78828931); _sage_const_83986478 = Integer(83986478); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_2707776 = Integer(2707776); _sage_const_3395364 = Integer(3395364); _sage_const_2543722 = Integer(2543722); _sage_const_1380876 = Integer(1380876); _sage_const_154210 = Integer(154210); _sage_const_3200829 = Integer(3200829); _sage_const_1154664 = Integer(1154664); _sage_const_3677561 = Integer(3677561); _sage_const_4119120 = Integer(4119120); _sage_const_728104 = Integer(728104); _sage_const_2177970 = Integer(2177970); _sage_const_3270750 = Integer(3270750); _sage_const_1017120 = Integer(1017120); _sage_const_1885455 = Integer(1885455); _sage_const_6209675 = Integer(6209675); _sage_const_3960926 = Integer(3960926); _sage_const_2937552 = Integer(2937552); _sage_const_5915490 = Integer(5915490); _sage_const_6040860 = Integer(6040860); _sage_const_6604794 = Integer(6604794); _sage_const_543906 = Integer(543906); _sage_const_172056 = Integer(172056); _sage_const_6854750 = Integer(6854750); _sage_const_0 = Integer(0); _sage_const_16 = Integer(16)
from gmpy2 import invert
import random

p = _sage_const_125102209 
a = _sage_const_24 
b = _sage_const_23 
E = EllipticCurve(GF(p), [a, b])
g = E([_sage_const_78828931 , _sage_const_83986478 ])
order = g.order()
print(order)  # little order

gs = [g]  # G
for i in range(order-_sage_const_1 ):
  gs.append(g*(i+_sage_const_2 ))

c = [_sage_const_2707776 , _sage_const_3395364 , _sage_const_2543722 , _sage_const_1380876 , _sage_const_154210 , _sage_const_3200829 , _sage_const_1154664 , _sage_const_3677561 , _sage_const_4119120 , _sage_const_728104 , _sage_const_2177970 , _sage_const_3270750 , _sage_const_1017120 , _sage_const_1885455 , _sage_const_6209675 , _sage_const_3960926 , _sage_const_2937552 , _sage_const_5915490 , _sage_const_6040860 , _sage_const_6604794 , _sage_const_543906 , _sage_const_172056 , _sage_const_6854750 ]
for xkinv in range(_sage_const_1 , order):
  kPoint = xkinv*g
  kp = kPoint.xy()
  random.seed((int(kp[_sage_const_0 ])*int(kp[_sage_const_1 ])))

  try:
    result = chr(c[_sage_const_0 ]//random.getrandbits(_sage_const_16 ))
  except:
    pass
  if result != 'H':
    pass

  try:
    for ci in c[_sage_const_1 :]:
      result += chr(ci//random.getrandbits(_sage_const_16 ))
  except:
    pass

  if 'HSCTF' in result:
    print(xkinv)
    print(kp)
    print(result)
    
   



