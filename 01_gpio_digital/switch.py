import RPi.GPIO as GPIO
import time

#Hello World!
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
val = 0
try:
    while 1:
        i = val
        val  = GPIO.input(LED_PIN)
        if(i != val):
            print("누른다!  " if val else "안누른다!", end = "\r")
    
finally:
    GPIO.cleanup()