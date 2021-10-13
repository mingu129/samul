import RPi.GPIO as gpio
import time

buzzerPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(buzzerPin, gpio.OUT)

pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)

melody = {"도":262,"레":294,"미":330,"파":349,"솔":392,"솹" : 415, "라":440,"시":494,"높도":523, "렢":587, "싲" : 247}
sheet = ["레레","렢", "라","솹","솔", "파","미파솔", "도도", "싲싲"]


try:
    for t in range(2):

        # 솔솔라라솔솔미
        for j in sheet[0]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        for j in sheet[1]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.25)
        for j in sheet[2]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.25)

        time.sleep(0.25)
        pwm.ChangeFrequency(1)
        
        for j in sheet[3]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[4]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[5]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[6]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)

        for j in sheet[7]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        for j in sheet[1]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.25)
        for j in sheet[2]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.25)
        time.sleep(0.25)
        pwm.ChangeFrequency(1)
        for j in sheet[3]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[4]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[5]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[6]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)

        for j in sheet[8]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        for j in sheet[1]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.25)
        for j in sheet[2]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.25)
        time.sleep(0.25)
        pwm.ChangeFrequency(1)
        for j in sheet[3]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[4]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[5]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)
        time.sleep(0.25)
        for j in sheet[6]:
            pwm.ChangeFrequency(melody[j])
            time.sleep(0.125)

    
    
    
    
    
        

finally:
    pwm.stop()
    gpio.cleanup()