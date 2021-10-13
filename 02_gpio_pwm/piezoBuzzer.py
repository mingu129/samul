import RPi.GPIO as gpio
import time

buzzerPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(buzzerPin, gpio.OUT)

pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)
time.sleep(2)

pwm.ChangeDutyCycle(0)

pwm.stop()
    gpio.cleanup()