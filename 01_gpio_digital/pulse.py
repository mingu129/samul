
from gpiozero import PWMLED 
import time

#Hello World!
pwmled = PWMLED(4)

for i in range(10):
   print("켰다!")
   for k in range(100):
      pwmled.value = 0.01 * k
      time.sleep(0.01)
   
   print("껐다!")
   for j in range(100):
      pwmled.value = 0.01*(100 - j)
      time.sleep(0.01)


