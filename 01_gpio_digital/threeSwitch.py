import RPi.GPIO as GPIO

# LED_PIN1 = 2
# LED_PIN2 = 3
# LED_PIN3 = 4
# switchPin1 = 17
# switchPin2 = 27
# switchPin3 = 22

switchArr = [17, 27, 22]
ledArr = [2, 3, 4]

GPIO.setmode(GPIO.BCM)

for i in range(0,3):
    GPIO.setup(switchArr[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(ledArr[i], GPIO.OUT) 

try:
    while 1:
        
        val  = GPIO.input(17)
        val2 = GPIO.input(27)
        val3 = GPIO.input(22)
        GPIO.output(2, val)
        GPIO.output(3, val2)
        GPIO.output(4, val3)
    
finally:
    GPIO.cleanup()