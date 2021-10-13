import RPi.GPIO as gpio
import time

buzzerPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(buzzerPin, gpio.OUT)

pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)

melody = [262,294,330,349,392,440,494,523]

try:
    for i in melody:
        pwm.ChangeFrequency(int(i))
        time.sleep(1)

finally:
    pwm.stop()
    gpio.cleanup()