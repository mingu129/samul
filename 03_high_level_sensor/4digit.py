import RPi.GPIO as GPIO
import time



SEGMENT_PINS = [3, 21, 8, 6, 5, 2, 9] #2,3,4,5,6,7,8
DIGIT_PINS = [4, 16, 20, 10] #4,11,12,13

GPIO.setmode(GPIO.BCM)


for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)


for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9
def display(digit, number): 
    for i in range(4):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])
    time.sleep(0.001)

try:
    while True:
        display(1,7)
        display(2,0)
        display(3,2)
        display(4,1)
finally:
    GPIO.cleanup()
    print('bye')