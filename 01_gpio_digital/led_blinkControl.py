import RPi.GPIO as GPIO
import time

#Hello World!
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT) 
print("----------------------\n1: led on\n0: led off\n2: exit\n----------------------")

p = 0
try:

    while 1:

        p = int(input("Input: "))
        if p == 0:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("led off!\n----------------------")

            
        elif p == 1:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("led on\n----------------------")


        elif p == 2:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("exit!\n----------------------\n")
            break
finally :
    GPIO.cleanup()
    print("\n-----cleanUpAndExit-----")