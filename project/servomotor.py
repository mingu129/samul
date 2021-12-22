import RPi.GPIO as GPIO
import time

# Hello World!
switch_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
val = 0
try:
    while 1:
        val = GPIO.input(LED_PIN)
        print(val)

finally:
    GPIO.cleanup()
