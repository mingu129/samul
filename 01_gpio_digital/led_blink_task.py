import RPi.GPIO as GPIO
import time


LED_PIN1 = 17
LED_PIN2 = 27
LED_PIN3 = 4
GPIO.setmode(GPIO.BCM)

li = [LED_PIN1, LED_PIN2, LED_PIN3]
li1 = ["RED", "YELLOW", "GREEN"]


for t in range(3):
    GPIO.setup(li[t], GPIO.OUT)

for j in range(31001203):
    for i in range(3):
        GPIO.output(li[i], GPIO.HIGH)
        print(li1[i] + " led on")
        time.sleep(0.08)
        GPIO.output(li[i], GPIO.LOW)

   
   
GPIO.cleanup()
