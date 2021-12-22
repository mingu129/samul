import RPi.GPIO as GPIO
import time


LED_PIN1 = 20
LED_PIN2 = 16
GPIO.setmode(GPIO.BCM)

li = [LED_PIN1, LED_PIN2]
li1 = ["RED", "YELLOW"]


for t in range(2):
    GPIO.setup(li[t], GPIO.OUT)

try:
    for j in range(31001203):
        for i in range(2):
            GPIO.output(li[i], GPIO.HIGH)
            print(li1[i] + " led on")
            time.sleep(0.08)
            GPIO.output(li[i], GPIO.LOW)
finally:

    GPIO.cleanup()
