import RPi.GPIO as gpio
import time

buzzerPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(buzzerPin, gpio.OUT)

pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)

melody = {"도":262,"레":294,"미":330,"파":349,"솔":392,"라":440,"시":494,"높도":523}
sheet = "솔솔라라솔솔미"
sheet2 = "솔솔미미레"
sheet3 = "솔미레미도"

try:
    # 솔솔라라솔솔미
    for s in sheet:                         
        pwm.ChangeFrequency(melody[s])
        time.sleep(0.5)
    time.sleep(0.5)

    # 솔솔미미레
    for s1 in sheet2:
        pwm.ChangeFrequency(melody[s1])
        time.sleep(0.5)
    time.sleep(1.5)

    # 솔솔라라솔솔미
    for s2 in sheet:
        pwm.ChangeFrequency(melody[s2])
        time.sleep(0.5)
    time.sleep(0.5)

    # 솔미레미도
    for s3 in sheet3:
        pwm.ChangeFrequency(melody[s3])
        time.sleep(0.5)
    time.sleep(1.5)
    
        

finally:
    pwm.stop()
    gpio.cleanup()