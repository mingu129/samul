import RPi.GPIO as GPIO

LED_PIN = 22
switchPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(LED_PIN, GPIO.OUT) 

try:
    while 1:
        val  = GPIO.input(4)
        GPIO.output(LED_PIN, val)
    
finally:
    GPIO.cleanup()